from tkinter import *


class newEntry(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color="grey"):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color

    def foc_in(self, *args):
        if self.get() == self.placeholder:
            self.delete("0", "end")
            self["fg"] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class newText(Text):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color="grey"):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert('1.0', self.placeholder)
        self.tag_configure("placeholder", foreground=self.placeholder_color)

        # 将标签应用于整个文本框
        self.tag_add("placeholder", "1.0", "end")

    def foc_in(self, *args):
        if self.get('1.0', 'end-1c') == self.placeholder:
            self.delete("1.0", "end")
            self["fg"] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get('1.0', 'end-1c'):
            self.put_placeholder()


# 创建带有默认文本的Text对象
def Gen_Text(frame: Frame, text: str):
    return newText(frame, text)


def Gen_Entry(frame: Frame, text: str):
    return newEntry(frame, text)

