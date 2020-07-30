def process_file(lines):
    class_list = []
    def_list = []
    var_list = []
    relation = []
    comment_state = False
    for x in lines:

        # skipping comments, print and if statements
        if x == "\n":
            continue
        if comment_state is True:
            if x.find("*/") != -1:
                comment_state = False
                continue
            continue

        if x.find("/*") != -1:
            comment_state = True
            continue

        if x.startswith("//") is True:
            continue
        if x.find("//") != -1:
            trim = x.find("//")
            x = x[:trim]
        if x.startswith("if") is True:
            continue

        if x.find("if") != -1:
            continue
        if x.find("for") != -1:
            continue
        if x.find("while") != -1:
            continue

        if x.find("System.out.println ") != -1:
            continue
        if x.find("System.out.println(") != -1:
            continue
        if x.find("import") != -1:
            continue
        if x.find("return") != -1:
            continue

        # finding classes
        if x.find("class ") != -1:
            temp = ""
            class_name_start = x.find("class ") + len("class ")
            class_name_end = x.find("{")

            # *****************Inheritance****************
            if x.find("extends ") != -1:
                start = x.find("extends ") + len("extends ")
                end = x[start:].find("{") + start
                if x.find("{") == -1:
                    end = len(x)-1
                temp = x[start:end]
                class_name_end = x.find("extends ") -1
            # *******************************************
            if class_name_end == -1:
                class_name_end = len(x)-1
            class_name = x[class_name_start:class_name_end]
            class_list.append(class_name)

            if temp != "":
                relation.append([temp, class_name])
                #print("parent: ", relation)
            continue

        # finding functions
        if x.find("abstract") != -1:
            if x.find("=") == -1:

                if x.find("void ") != -1:
                    func_name_start = x.find("void ") + len("void ")
                    func_name_end = x.find("(")
                    func_name = x[func_name_start:func_name_end]
                    func_tuple = func_name, class_list[-1]
                    def_list.append(func_tuple)
                    continue

                elif x.find("int ") != -1:
                    func_name_start = x.find("int ") + len("int ")
                    func_name_end = x.find("(")
                    func_name = x[func_name_start:func_name_end]
                    func_tuple = func_name, class_list[-1]
                    def_list.append(func_tuple)
                    continue

                elif x.find("String ") != -1:
                    func_name_start = x.find("String ") + len("String ")
                    func_name_end = x.find("(")
                    func_name = x[func_name_start:func_name_end]
                    func_tuple = func_name, class_list[-1]
                    def_list.append(func_tuple)
                    continue

                elif x.find("float ") != -1:
                    func_name_start = x.find("float ") + len("float ")
                    func_name_end = x.find("(")
                    func_name = x[func_name_start:func_name_end]
                    func_tuple = func_name, class_list[-1]
                    def_list.append(func_tuple)
                    continue

                elif x.find("double ") != -1:
                    func_name_start = x.find("double ") + len("double ")
                    func_name_end = x.find("(")
                    func_name = x[func_name_start:func_name_end]
                    func_tuple = func_name, class_list[-1]
                    def_list.append(func_tuple)
                    continue

                elif x.find("char ") != -1:
                    func_name_start = x.find("char ") + len("char ")
                    func_name_end = x.find("(")
                    func_name = x[func_name_start:func_name_end]
                    func_tuple = func_name, class_list[-1]
                    def_list.append(func_tuple)
                    continue

                elif x.find("boolean ") != -1:
                    func_name_start = x.find("boolean ") + len("boolean ")
                    func_name_end = x.find("(")
                    func_name = x[func_name_start:func_name_end]
                    func_tuple = func_name, class_list[-1]
                    def_list.append(func_tuple)
                    continue

        if x.find("=") and x.find(";") == -1:
            if x.find("void ") != -1:
                func_name_start = x.find("void ") + len("void ")
                func_name_end = x.find("(")
                func_name = x[func_name_start:func_name_end]
                func_tuple = func_name, class_list[-1]
                def_list.append(func_tuple)
                continue

            elif x.find(class_list[-1]) != -1:
                func_tuple = "constructor: "+class_list[-1], class_list[-1]
                def_list.append(func_tuple)
                continue

            elif x.find("int ") != -1:
                func_name_start = x.find("int ") + len("int ")
                func_name_end = x.find("(")
                func_name = x[func_name_start:func_name_end]
                func_tuple = func_name, class_list[-1]
                def_list.append(func_tuple)
                continue

            elif x.find("String ") != -1:
                func_name_start = x.find("String ") + len("String ")
                func_name_end = x.find("(")
                func_name = x[func_name_start:func_name_end]
                func_tuple = func_name, class_list[-1]
                def_list.append(func_tuple)
                continue

            elif x.find("float ") != -1:
                func_name_start = x.find("float ") + len("float ")
                func_name_end = x.find("(")
                func_name = x[func_name_start:func_name_end]
                func_tuple = func_name, class_list[-1]
                def_list.append(func_tuple)
                continue

            elif x.find("double ") != -1:
                func_name_start = x.find("double ") + len("double ")
                func_name_end = x.find("(")
                func_name = x[func_name_start:func_name_end]
                func_tuple = func_name, class_list[-1]
                def_list.append(func_tuple)
                continue

            elif x.find("char ") != -1:
                func_name_start = x.find("char ") + len("char ")
                func_name_end = x.find("(")
                func_name = x[func_name_start:func_name_end]
                func_tuple = func_name, class_list[-1]
                def_list.append(func_tuple)
                continue

            elif x.find("boolean ") != -1:
                func_name_start = x.find("boolean ") + len("boolean ")
                func_name_end = x.find("(")
                func_name = x[func_name_start:func_name_end]
                func_tuple = func_name, class_list[-1]
                def_list.append(func_tuple)
                continue

        # finding variables
        if x.find("=") != -1:
            x = x.lstrip()
            var_name_end = x.find("=")
            if x.find(" =") != -1:
                var_name_end = x.find(" =")
            var_name = x[0:var_name_end]

            if x[:var_name_end].find("[") != -1:
                var_name_end = x[:var_name_end].find("[")
                var_name = x[0:var_name_end]

            if var_name.find("this.") != -1:
                var_name = var_name.replace("this.", "")
            flag = False
            for values in var_list:
                splitvalue = values[0].split()
                tempvalue = splitvalue[-1]
                tempvalue = tempvalue[:tempvalue.find(";")]
                if tempvalue == var_name:
                    if values[1] == class_list[-1]:
                        flag = True
                        continue
                if values[0] == var_name:
                    if values[1] == class_list[-1]:
                        flag = True
                        continue
            if flag is True:
                continue
            var_tuple = var_name, class_list[-1]
            var_list.append(var_tuple)

        if x.find(";") != -1:
            if x.find("(") == -1:
                if x.find("[") != -1:
                    continue

                if x.find("=")== -1:
                    x = x.lstrip()
                    var_name_end = x.find("=")
                    if x.find(" =") != -1:
                        var_name_end = x.find(" =")
                    var_name = x[0:var_name_end]

                    if x[:var_name_end].find("[") != -1:
                        var_name_end = x[:var_name_end].find("[")
                        var_name = x[0:var_name_end]

                    if var_name.find("this.") != -1:
                        var_name = var_name.replace("this.", "")
                    flag = False
                    for values in var_list:
                        splitvalue = values[0].split()
                        tempvalue = splitvalue[-1]
                        tempvalue = tempvalue[:tempvalue.find(";")]
                        if tempvalue == var_name:
                            if values[1] == class_list[-1]:
                                flag = True
                                continue
                        if values[0] == var_name:
                            if values[1] == class_list[-1]:
                                flag = True
                                continue
                    if flag is True:
                        continue
                    var_tuple = var_name, class_list[-1]
                    var_list.append(var_tuple)

    return class_list, def_list, var_list, relation
