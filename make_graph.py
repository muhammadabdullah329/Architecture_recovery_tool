import pydot


def make_graph_function(class_list, def_list, var_list, relation):
    graph = pydot.Dot(graph_type='digraph')
    f = open("HTMLS/outputfile.txt", "w")
    temp = "Class" + "," + "Total_Functions" + "," + "Total_variables"
    f.write(temp + "\n")

    # loop for making graphs
    for name in class_list:
        temp_list1 = ["\n*Variables*"]
        for var_name in var_list:
            if name == var_name[1]:
                temp_list1.append(var_name[0])
                # print(var_name[0])

        temp_list = ["*Functions*"]
        for def_name in def_list:
            if name == def_name[1]:
                temp_list.append(def_name[0])
                # print(def_name[0])

        # -1 because of reformatting
        num_func = len(temp_list) - 1
        num_var = len(temp_list1) - 1

        temp = name+"," + str(num_func)+"," + str(num_var)
        f.write(temp + "\n")

        listToStr1 = '\n'.join([str(elem) for elem in temp_list1])
        listToStr = '\n'.join([str(elem) for elem in temp_list])

        finalStr = name + "\n\n" + listToStr + "\n" + listToStr1
        node = name
        graph.add_node(pydot.Node(node, shape='box', label=finalStr))

        for n in relation:
            if n[1] == name:
                edge = pydot.Edge(n[0], n[1])
                graph.add_edge(edge)

    graph.write_png('HTMLS/output.png')
    f.close()
