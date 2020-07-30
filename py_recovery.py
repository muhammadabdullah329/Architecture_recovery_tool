
def process_file(lines):
    class_list = []
    def_list = []
    var_list = []
    relation = []
    comment_state = False
    for x in lines:
        if comment_state is True:
            if x.find("\'\'\'") != -1:
                comment_state = False
                continue
            if x.find("\"\"\"") != -1:
                comment_state = False
                continue
            continue
        # skipping comments, print and if statements
        if x.find("\'\'\'") != -1:
            comment_state = True
            continue
        if x.find("\"\"\"") != -1:
            comment_state = True
            continue
        if x.find("for") != -1:
            continue
        if x.find("while") != -1:
            continue
        if x.startswith("#") is True:
            continue
        if x.find("#") != -1:
            trim = x.find("#")
            x = x[:trim]
        if x.startswith("if") is True:
            continue
        if x.startswith(" ") is True:
            if x.find("if") != -1:
                continue

        if x.find("print ") != -1:
            continue
        if x.find("print(") != -1:
            continue

        # finding classes
        if x.find("class ") != -1:
            temp = ""
            class_name_start = x.find("class ") + len("class ")
            class_name_end = x.find("(")
            if class_name_end != -1:
                start = x.find("(") + len("(")
                end = x[start:].find(")") + start
                temp = x[start:end]

            if class_name_end == -1:
                class_name_end = x.find(":")
            # print(class_name_end)
            class_name = x[class_name_start:class_name_end]
            class_list.append(class_name)

            if temp != "":
                relation.append([temp, class_name])
                # print("parent: ", relation)

            # print(class_name)

        # finding functions
        if x.find("def ") != -1:
            func_name_start = x.find("def ") + len("def ")
            func_name_end = x.find("(")
            func_name = x[func_name_start:func_name_end]
            func_tuple = func_name, class_list[-1]
            if x.startswith(" ") is True:
                def_list.append(func_tuple)
            else:
                func_tuple = func_name, "Main"
                def_list.append(func_tuple)

        # finding variables
        if x.find("=") != -1:
            var_name_end = x.find("=")
            if x.find(" =") != -1:
                var_name_end = x.find(" =")

            if x.startswith(" ") is True:
                x = x.lstrip()
                var_name_end = x.find("=")
                if x.find(" =") != -1:
                    var_name_end = x.find(" =")
                var_name_start = 0
                var_name = x[var_name_start:var_name_end]

                if x[:var_name_end].find("[") != -1:
                    var_name_end = x[:var_name_end].find("[")
                    var_name = x[var_name_start:var_name_end]

                # striping self from variable name
                if var_name.find("self.") != -1:
                    var_name = var_name.replace("self.", "")
                flag = False
                for values in var_list:
                    if values[0] == var_name:
                        if values[1] == class_list[-1]:
                            flag = True
                            continue
                if flag is True:
                    continue
                var_tuple = var_name, class_list[-1]
                var_list.append(var_tuple)
            else:
                var_name = x[0:var_name_end]
                if x[:var_name_end].find("[") != -1:
                    var_name_end = x[:var_name_end].find("[")
                    var_name = x[0:var_name_end]
                flag = False
                for values in var_list:
                    if values[0] == var_name:
                        if values[1] == class_list[-1]:
                            flag = True
                            continue
                if flag is True:
                    continue
                var_tuple = var_name, "Main"
                var_list.append(var_tuple)

    return class_list, def_list, var_list, relation
