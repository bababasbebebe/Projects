
from PyQt6 import QtCore, QtGui, QtWidgets
import elemoperations
import pyclipper

pc = pyclipper.Pyclipper()
list = [1, 1, 4, 1, 4, 3, 2, 3, 2, 5, 8, 5, 8, 3, 5, 3, 5, 1, 9, 1, 9, 6, 1, 6]

list1 = [0, 0, 3, 0, 5, 0, 5, 5, 0, 5]
list1 = elemoperations.elem_to_points(list1)
list = elemoperations.elem_to_points(list)

pc.AddPath(list1, pyclipper.PT_CLIP, True)
pc.AddPath(list, pyclipper.PT_CLIP, True)

solution = pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD)

print(solution)

#string = "dsdsd*dsdsd+fdgfdgd/sdadsa)"
"""
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

class Ui_Pattern(object):
    def __init__(self):
        super().__init__()
        self.DS = []
        self.L = []
        self.P = []

    def setupUi(self, Pattern, path):
        Pattern.setObjectName("Pattern")
        Pattern.resize(895, 516)
        self.path = path
        self.gridLayout = QtWidgets.QGridLayout(Pattern)
        self.gridLayout.setObjectName("gridLayout")
        self.treeViewYScrollBar_2 = QtWidgets.QScrollBar(parent=Pattern)
        self.treeViewYScrollBar_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.treeViewYScrollBar_2.setObjectName("treeViewYScrollBar_2")
        self.gridLayout.addWidget(self.treeViewYScrollBar_2, 0, 0, 3, 1)

        self.treeView = QtWidgets.QTreeView(parent=Pattern)
        self.treeView.setMaximumSize(QtCore.QSize(150, 16777215))
        self.treeView.setObjectName("treeView")
        self.treeView.setHeaderHidden(True)
        self.treeModel = QtGui.QStandardItemModel()
        self.gridLayout.addWidget(self.treeView, 0, 1, 3, 3)
        self.rootNode = self.treeModel.invisibleRootItem()

        self.labelTextBox_2 = QtWidgets.QLabel(parent=Pattern)
        self.labelTextBox_2.setObjectName("labelTextBox_2")
        self.gridLayout.addWidget(self.labelTextBox_2, 0, 4, 1, 1)
        self.textBox_2 = QtWidgets.QPlainTextEdit(parent=Pattern)
        self.textBox_2.setObjectName("textBox_2")
        self.gridLayout.addWidget(self.textBox_2, 1, 4, 1, 3)
        self.textYBoxScrollBar_2 = QtWidgets.QScrollBar(parent=Pattern)
        self.textYBoxScrollBar_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.textYBoxScrollBar_2.setObjectName("textYBoxScrollBar_2")
        self.gridLayout.addWidget(self.textYBoxScrollBar_2, 1, 7, 1, 1)
        self.textXBoxScrollBar_2 = QtWidgets.QScrollBar(parent=Pattern)
        self.textXBoxScrollBar_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.textXBoxScrollBar_2.setObjectName("textXBoxScrollBar_2")
        self.gridLayout.addWidget(self.textXBoxScrollBar_2, 2, 4, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(32, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.pushFocusedButton_2 = QtWidgets.QPushButton(parent=Pattern)
        self.pushFocusedButton_2.setObjectName("pushFocusedButton_2")
        self.gridLayout.addWidget(self.pushFocusedButton_2, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(32, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 4, 1, 1)
        self.inputExpressionButton_2 = QtWidgets.QPushButton(parent=Pattern)
        self.inputExpressionButton_2.setObjectName("inputExpressionButton_2")
        self.gridLayout.addWidget(self.inputExpressionButton_2, 3, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(287, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 6, 1, 1)

        self.retranslateUi(Pattern)
        QtCore.QMetaObject.connectSlotsByName(Pattern)

    def retranslateUi(self, Pattern):
        _translate = QtCore.QCoreApplication.translate
        Pattern.setWindowTitle(_translate("Pattern", "Form"))
        self.labelTextBox_2.setText(_translate("Pattern", "TextLabel"))
        self.pushFocusedButton_2.setText(_translate("Pattern", "PushButton"))
        self.inputExpressionButton_2.setText(_translate("Pattern", "PushButton"))


    def file_parser(self):
        DS_key = 0
        L_key = 0
        print("AAAA")
        # self.grab_set()
        with open(self.path, "r") as file:
            for line in file:
                if line[0] == "L":
                    self.treeView.insert(parent, tk.END, text=line[2:line.find(';')])
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
                    parent = QStandardItem(line[3:line.find(";")])
                    self.rootNode.appendRow(line[3:line.find(";")])
                    self.DS.append([line[3:line[3:].find(" ") + 3], DS_key])
                    DS_key += 1
                    self.L.append([])

        self.DS.sort()
        self.L.sort()
        print("!!!!!!DS: ", self.DS)
        print("!!!!!!L: ", self.L)
        print("!!!!!!P: ", self.P)

"""
"""
def segment_intersection(x11, y11, x12, y12, x21, y21, x22, y22):
    intersect = []
 
    # segment2 horizontal | segment1 vert
    if x11 == x12 and y21 == y22:
        if max(x21, x22) >= x11 >= min(x21, x22):
            if min(y11, y12) <= y21:
                intersect.append(x11)
                intersect.append(y21)

    # segment1 horizontal | segment2 vert
    elif y11 == y12 and x21 == x22:
        if max(x11, x12) >= x21 >= min(x11, x12):
            if min(y21, y22) <= y11:
                intersect.append(x21)
                intersect.append(y11)

    return intersect

def point_in_elem(x_point, y_point, x1, y1, x2, y2):
    if x1 == x2:
        if min(y1, y2) < y_point < max(y1, y2):
            if x_point < x1:
                return True

"""

"""
elem = [0, 0, 3, 0, 3, 3, 0, 3]
elem1 = [-1, 0, 2, 0, 2, 1, -1, 1]


elem_copy = elem.copy()
elem_copy.append(elem[0])
elem_copy.append(elem[1])

elem1_copy = elem1.copy()
elem1_copy.append(elem1[0])
elem1_copy.append(elem1[1])
plt.plot(elem_copy[0::2], elem_copy[1::2], c="r")
plt.plot(elem1_copy[0::2], elem1_copy[1::2], c="b")
print(elem_copy)
for i in range(0,len(elem1)-1, 2):
    count = 0
    for j in range(0,len(elem_copy)-2, 2):
        if func2(elem1[i], elem1[i+1], elem_copy[j], elem_copy[j+1], elem_copy[j+2], elem_copy[j+3]):
            count += 1
    if count % 2 == 1: plt.scatter(elem1[i], elem1[i+1], marker='X', c="black")
plt.show()
"""


# segment1 = [0, 0, 0, 5]
# segment2 = [0, 1, 0, 6]

# segment1 = [0, 0, 0, 5]
# segment2 = [0, 0, 6, 0]

# segment1 = [0, 0, 5, 0]
# segment2 = [1, 0, 6, 0]
"""
segment3 = func(0, -1, 0, 5, -1, 0, 6, 0)
if len(segment3) == 0: segment3 = [-5, -5, 5, 5]
print(segment3)
plt.plot([0, 0], [-1, 5], c="r")
plt.plot([-1, 6], [0, 0], c="b")
if len(segment3) == 4:
    plt.plot([segment3[0], segment3[2]], [segment3[1], segment3[3]], c="black", ls=":")
else:
    plt.scatter(segment3[0], segment3[1], c="black")

plt.show()
"""
""" 
list1 = [11, 255, 4]
for i in range(3):
    print('I{:0>3}'.format(format(list1[i], 'X')), (type('I{:0>3}'.format(list1[i]))))
    print(format(list1[i], 'X'))

print(" ")
print(" ")
print(" ")

list2 = ["I001", "I0A1", "IFFF"]

for i in range(3):
    print(re.search(r"([1-9]|[A-F]){1}", list2[i]).span()[0])
"""

# 1
"""
str = "DS\\131 1 1\\CDA+DS\\ad sa 89 sda\\M1+DS\\вап ав 1 ва\\MK"


print(re.findall(r"DS\\([\w|\s]+)\\(\w+)([+*/])", str))


first_x = [[2,2], [3,2], [4,2]]
second_x = [[2,2], [3,2], [4,2]]

x_first_count = 0
x_second_count = first_x[0][0]-second_x[0][0]
while x_first_count < len(first_x)-first_x[-1][0]+second_x[-1][0]:
    print(x_first_count, len(first_x))
    first_x[x_first_count][1] += second_x[x_second_count][1]
    x_first_count += 1
    x_second_count += 1

print(first_x)

# item to int нужно для общего выделения всех элементов под слоем

df3 = pd.DataFrame(columns=['y1'], index=[5,7,2,5], data=[1,2,3,4])
df4 = df3.copy()
print(df3)
a = df4.index
df4.index = df4['y1']
df4['y1'] = a
print(df3)
df3.plot(subplots=True, figsize=(3,6))
df4.plot(subplots=True, figsize=(3,6))

plt.show()
"""
"""
root = tk.Tk()
# root.attributes('-fullscreen', True)
root.geometry('800x800+100+100')
# root.maxsize(width=1920, height=1080)
Y = LabelFrame(root, bg="red")
PIC = LabelFrame(root, bg="yellow")
X = LabelFrame(root, bg="blue")
SPACE = LabelFrame(root, bg="white")

for c in range(6): root.columnconfigure(index=c, weight=1)
for r in range(6): root.rowconfigure(index=r, weight=1)

Y.grid(row=0, column=0, rowspan=5, sticky=NSEW)
PIC.grid(row=0, column=1, rowspan=5, columnspan=5, sticky=NSEW)
X.grid(row=5, column=1, columnspan=5, sticky=NSEW)
SPACE.grid(row=5, column=0, sticky=NSEW)


print("!")
root.mainloop()
"""

"""
def mf1(event):
    global squares
    for i in range(30):
        canvas.create_line(event.x+randint(-10, 10),
                           event.y+randint(-10, 10),
                           event.x+randint(-10, 10),
                           event.y+randint(-10, 10))
        for j in range(len(squares)):
            pass
            

def mf(event):
    global line_v, line_h, i, squares
    i += 1

    if i % 10 == 0:
        x_circ = randint(-400, 400)
        y_circ = randint(-400, 400)
        canvas.create_rectangle(x_circ, y_circ, x_circ+10, y_circ+10)
        squares.append([x_circ, y_circ])
        print(squares)

    x, y = event.x, event.y
    if canvas.old_coords:
        canvas.delete(line_v, line_h)
        x1, y1 = canvas.old_coords
        line_v = canvas.create_line(-400, y, 400, y1)
        line_h = canvas.create_line(x, -400, x1, 400)
        # canvas.create_line(-400, y, 400, y1)
        # canvas.create_line(x, -400, x1, 400)
    canvas.old_coords = x, y
    root.bind('<Button-1>', mf1)


root = tk.Tk()
print(tk.Tk())
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.old_coords = None

line_v = canvas.create_line(-400, 0, 400, 0)
line_h = canvas.create_line(0, -400, 0, 400)
squares = []
i = 0

root.bind('<Motion>', mf)

root.mainloop()"""
"""
class MainWindow(tk.Tk):
    def __init__(self, ):
        super().__init__()
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()
        self.canvas.old_coords = None

        self.line_v = self.canvas.create_line(-400, 0, 400, 0)
        self.line_h = self.canvas.create_line(0, -400, 0, 400)
        self.canvas.bind('<Motion>', self.mf)

    def mf(self, event):
        x, y = event.x, event.y
        if self.canvas.old_coords:
            self.canvas.delete(self.line_v, self.line_h)
            x1, y1 = self.canvas.old_coords
            self.line_v = self.canvas.create_line(-400, y, 400, y1)
            self.line_h = self.canvas.create_line(x, -400, x1, 400)
            # canvas.create_line(-400, y, 400, y1)
            # canvas.create_line(x, -400, x1, 400)
        self.canvas.old_coords = x, y

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
"""

"""df = pd.DataFrame(columns=[1,2,3], index=[2,3,4])
df[1][2] = ["DS321", "DS124"]
print(df[1][2][1])
print(type(df[1][2][0]), type(df[1][2][1]))
if isinstance(df[1][2][1], str): print("123")
if "DS321" in df[1][2]: print("!@#")
if "DS124" in df[1][2]: print("!@2")
if "DS" in df[1][2]: print("!@3")"""

"""
class Class():
    def __init__(self):
        int a = 1
    def __init__(self):
        int a = 2
    def ssprint(self):
        print(a)

Class.ssprint()
"""
