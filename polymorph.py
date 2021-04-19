from abc import ABC, abstractclassmethod


class UIControl(ABC):
    def __init__(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Draw method of TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("Draw method of DropDownList")


def draw(control):
    control.draw()


def drawgroup(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw(ddl)
draw(tb)
drawgroup([tb, ddl])
