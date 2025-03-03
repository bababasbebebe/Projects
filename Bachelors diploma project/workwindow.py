import tkinter as tk
from tkinter import *
from tkinter import ttk
import re
import conjunction
import disjunction
import substraction
from graphwindow import GraphWindow



def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint][0] == item:
            return alist[midpoint][1]
        else:
            if item < alist[midpoint][0]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)

# проверка перед закидыванием в функцию правильно ли расставлены скобки и знаки
# -на все открвающиеся "(" есть ")"
# -знаки не могут стоять перед ")" и перед друг другом
def test(self):
    pass

class DevWorkWindow(tk.Toplevel):
    def __init__(self, parent, path):
        super().__init__(parent)

        self.DS = []
        self.L = []
        self.P = []

        self.path = path
        self.frame_tree = ttk.LabelFrame(self, text="Список:")
        self.top_of_frame_tree = ttk.Frame(self.frame_tree)
        self.bottom_of_frame_tree = ttk.Frame(self.frame_tree)
        self.tree_list = ttk.Treeview(self.top_of_frame_tree)
        self.y_scrollbar_tree = ttk.Scrollbar(self.top_of_frame_tree, orient="vertical", command=self.tree_list.yview)
        self.button_push = ttk.Button(self.bottom_of_frame_tree, text="Выбрать",
                                      command=self.push_focused)

        self.frame_tree.pack(anchor=W, side=LEFT, pady=5, padx=5, fill=Y, expand=1)
        self.top_of_frame_tree.pack(side=TOP, fill=Y, expand=1)
        self.bottom_of_frame_tree.pack(side=TOP)
        self.tree_list.pack(side=LEFT, pady=10, padx=10, fill=Y, expand=1)
        self.y_scrollbar_tree.pack(side=LEFT, pady=2, padx=2, fill=Y, expand=1)
        self.button_push.pack(side=TOP, pady=10)

        self.tree_list.configure(yscrollcommand=self.y_scrollbar_tree.set)

        self.frame_textbox = ttk.LabelFrame(self, text="Формула:")
        self.top_of_frame_textbox = ttk.Frame(self.frame_textbox)
        self.bottom_of_frame_textbox = ttk.Frame(self.frame_textbox)
        self.label_info = ttk.Label(self, text="Для ввода...")
        self.text_box = tk.Text(self.top_of_frame_textbox, wrap=NONE)
        self.y_scrollbar_textbox = ttk.Scrollbar(self.top_of_frame_textbox,
                                                 orient="vertical", command=self.text_box.yview)
        self.x_scrollbar_textbox = ttk.Scrollbar(self.bottom_of_frame_textbox,
                                                 orient="horizontal", command=self.text_box.xview)
        self.button_input = ttk.Button(self.bottom_of_frame_textbox, text="Ввод", command=self.input_expressions)

        # self.label_info.pack(side=TOP, pady=10, padx=10, fill=X, expand=1)
        self.frame_textbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.top_of_frame_textbox.pack(side=TOP, fill=BOTH, expand=1)
        self.bottom_of_frame_textbox.pack(side=BOTTOM, fill=X, expand=1)
        self.text_box.pack(side=LEFT, pady=10, padx=10, fill=BOTH, expand=1)
        self.y_scrollbar_textbox.pack(side=LEFT, pady=10, padx=10, fill=Y, expand=1)
        self.x_scrollbar_textbox.pack(side=TOP, pady=10, padx=10, fill=X, expand=1)
        self.button_input.pack(side=TOP, pady=10)

        self.text_box.configure(yscrollcommand=self.y_scrollbar_textbox.set)
        self.text_box.configure(xscrollcommand=self.x_scrollbar_textbox.set)

    def file_parser(self):
        DS_key = 0
        L_key = 0
        # self.grab_set()
        self.tree_list.heading('#0', text=self.path[self.path.rfind('\\') + 1:])
        with open(self.path, "r") as file:
            for line in file:
                if line[0] == "L":
                    self.tree_list.insert(parent, tk.END, text=line[2:line.find(';')])
                    self.L[DS_key - 1].append([line[2:line.find(';')], L_key])
                    L_key += 1
                # НЕ ДОДЕЛАНО
                elif line[0] == "P" or line[0] == "W":
                    self.P.append([int(line[2:line[2:].find(" ") + 3])])
                    coord = ""
                    i = line[2:].find(" ") + 3
                    while line[i] != ';':
                        if line[i] != " ":
                            coord = coord + line[i]
                        else:
                            self.P[L_key - 1].append(int(coord))
                            coord = ""
                        i += 1
                    self.P[L_key - 1].append(int(coord))
                elif line[0:2] == "DS":
                    parent = self.tree_list.insert('', tk.END, text=line[3:line.find(";")])
                    self.DS.append([line[3:line[3:].find(" ") + 3], DS_key])
                    DS_key += 1
                    self.L.append([])

        self.DS.sort()
        self.L.sort()
        print("!!!!!!DS: ", self.DS)
        print("!!!!!!L: ", self.L)
        print("!!!!!!P: ", self.P)

    def get_selection(self):
        selected_items = self.tree_list.selection()
        list_of_values = []

        for item in selected_items:
            if len(self.tree_list.item(self.tree_list.parent(item)).get("text")) == 0:
                child_idd = int(item[re.search(r"([1-9]|[A-F])", item).start():], 16) + 1
                while len(self.tree_list.item(self.tree_list.parent('I{:0>3}'.format(format(child_idd, 'X')))).get(
                        "text")) > 0:
                    item_child = 'I{:0>3}'.format(format(child_idd, 'X'))
                    current_item = self.tree_list.item(item_child)
                    current_value = current_item.get("text")

                    current_parent_of_item = self.tree_list.item(self.tree_list.parent(item_child))
                    current_value_of_parent = current_parent_of_item.get("text")
                    list_of_values.extend((current_value_of_parent[0:current_value_of_parent.find(' ')], current_value))
                    child_idd += 1
            else:
                current_parent_of_item = self.tree_list.item(self.tree_list.parent(item))
                if current_parent_of_item.get("open"):
                    current_value_of_parent = current_parent_of_item.get("text")
                    current_item = self.tree_list.item(item)
                    current_value = current_item.get("text")
                    list_of_values.extend((current_value_of_parent[0:current_value_of_parent.find(' ')], current_value))
        return list_of_values

    def push_focused(self):
        list_of_selection = self.get_selection()
        for i in range(0, len(list_of_selection) - 1, 2):
            self.text_box.insert(INSERT, list_of_selection[i] + "_" + list_of_selection[i + 1] + " + ")

    def input_expressions(self):
        row_counter = 1
        while re.search('\n', self.text_box.get(str(row_counter) + ".0", END)) is not None:
            string = self.text_box.get(str(row_counter) + ".0", str(row_counter + 1) + ".0")
            if len(string) > 1:
                self.func(string)
            row_counter += 1
        GraphWindow(self).elem_list()


    def func(self, string):
        op = {'*': 2, '/': 2, '+': 1, '(': 0}
        acts = []

        def foo2():
            sign = stack_op.pop()
            if stack_elems[-1] == 0:
                stack_elems.pop()
                elem2 = acts.pop()
            else:
                elem_name = stack_elems.pop()
                num_of_DS = binarySearch(self.DS, elem_name[:elem_name.find('_')])
                num_of_L = binarySearch(self.L[num_of_DS], elem_name[elem_name.find('_')+1:])
                elem2 = self.P[num_of_L]
            if stack_elems[-1] == 0:
                stack_elems.pop()
                elem1 = acts.pop()
            else:
                elem_name = stack_elems.pop()
                num_of_DS = binarySearch(self.DS, elem_name[:elem_name.find('_')])
                num_of_L = binarySearch(self.L[num_of_DS], elem_name[elem_name.find('_')+1:])
                elem1 = self.P[num_of_L]
            if sign == "*":
                acts.append(conjunction.conj(elem1, elem2))
            elif sign == "+":
                acts.append(disjunction.disj(elem1, elem2))
            elif sign == "/":
                acts.append(substraction.substr(elem1, elem2))
            stack_elems.append(0)

        string = string.replace(' ', '')
        string = string[:-1]
        string = '(' + string + ')'
        stack_elems = []
        stack_op = []
        for symb in string:
            if symb not in '*/+()':
                elem += symb
            else:
                if symb == ')':
                    if elem:
                        stack_elems.append(elem)
                    while stack_op[-1] != '(':
                        foo2()
                    stack_op.pop()
                elif symb == '(':
                    stack_op.append('(')
                else:
                    if elem: stack_elems.append(elem)
                    if op[stack_op[-1]] > op[symb]:
                        foo2()
                    stack_op.append(symb)
                elem = ''
        if not stack_op: pass
        print(acts[0])
