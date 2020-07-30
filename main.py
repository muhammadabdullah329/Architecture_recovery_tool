import eel
import py_recovery      # This is the module made for python language
import java_recovery    # This is the module made for java language
import make_graph       # This is the module made for making graphs

"""
This is the backend of architecture recovery tool made by the following Students:
    Hafiz Muhammad Abdullah     FA17-BSE-014
    Ali Javed                   FA17-BSE-116
    Haziq Majeed                FA17-BSE-023
"""
'''
This program reads a implementation level file 
and displays the number of classes methods variables used in the program file.
'''

@eel.expose
def main_function(file_names):
    # Lists for storing data
    class_list = ["Main"]  # class name
    def_list = []  # function , class name
    var_list = []  # variable , class name
    relation = []  # parent class , child class

    # multiple files
    files = []

    def handle_lists(class_list_temp, def_list_temp, var_list_temp, relation_temp):
        for c in class_list_temp:
            class_list.append(c)
        for d in def_list_temp:
            def_list.append(d)
        for v in var_list_temp:
            var_list.append(v)
        for r in relation_temp:
            relation.append(r)

    for fnames in file_names:
        fnames = "test_files/" + fnames
        files.append(fnames)
        # print(fnames)

    for path in files:
        file = open(path, "r")

        # read file line by line
        lines = file.readlines()

        # Automatically checking the extension of the file
        if file.name.endswith(".py"):
            class_list_temp, def_list_temp, var_list_temp, relation_temp = py_recovery.process_file(lines)
            handle_lists(class_list_temp, def_list_temp, var_list_temp, relation_temp)

        if file.name.endswith(".java"):
            if class_list[0] == "Main":
                class_list.remove("Main")

            class_list_temp, def_list_temp, var_list_temp, relation_temp = java_recovery.process_file(lines)
            handle_lists(class_list_temp, def_list_temp, var_list_temp, relation_temp)


        # Closing the input file
        file.close()

    #print("Class names: ",class_list)
    #print("method names: ",def_list)
    #print("variable names: ",var_list)

    # The Following function is used to draw graphs from the lists processed by the function above
    make_graph.make_graph_function(class_list, def_list, var_list, relation)


eel.init("HTMLS")
eel.start("index.html",size=(1500,900))