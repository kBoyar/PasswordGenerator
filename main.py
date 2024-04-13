import tkinter
import random
from tkinter import filedialog
import os


class LabeledCheckbutton(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        self.var = tkinter.BooleanVar(value=True)
        self.checkbutton = tkinter.Checkbutton(self, variable=self.var)
        self.label = tkinter.Label(self)
        self.label.grid(row=0, column=0)
        self.checkbutton.grid(row=1, column=0)


class LabeledEntry(tkinter.Frame):
    def __init__(self):
        tkinter.Frame.__init__(self)
        self.label = tkinter.Label(self)
        self.entry = tkinter.Entry(self)
        # self.label.pack()
        # self.entry.pack()
        self.label.grid(row=0, column=0, sticky='w')
        self.entry.grid(row=0, column=1, sticky='w')

    def get_entry(self):
        entry_text = self.entry.get()
        return entry_text


class InvalidLengthRange(Exception):
    def __init__(self, ln, message="Maximum password length is 84"):
        self.ln = ln
        self.message = message
        super().__init__(self.message)


def display_password():
    upper = cbu.var.get()
    lower = cbl.var.get()
    num = cbn.var.get()
    sym = cbs.var.get()
    arr = create_array(upper, lower, num, sym)
    length = 0
    try:
        length = int(entry.get_entry())
        if length > 84:
            raise InvalidLengthRange(length)
        flag = 1
    except ValueError:
        flag = 0
    except InvalidLengthRange:
        flag = 0
    if (upper or lower or num or sym) and flag:
        password = generate_password(arr, length)
    elif not flag:
        password = "Length error!"
    else:
        password = ""
    output.delete(0, "end")
    output.insert(0, password)


def generate_password(array, length):
    psw = "".join(random.sample(array, length))
    return psw


def create_array(up, lo, nm, sm):
    arr = ""
    if up:
        arr += upper_letters
    if lo:
        arr += lower_letters
    if nm:
        arr += nums
    if sm:
        arr += symbols
    return arr


def savefile():
    if output.get():
        directory = os.getcwd()
        file = filedialog.asksaveasfile(initialdir=directory,
                                        defaultextension='.txt',
                                        filetypes=[("TextFile", ".txt"), ("AllFiles", ".*"),])
        if file:
            text = output.get()
            file.write(text)
            file.close()


def copy_password():
    cp = output.get()
    window.clipboard_clear()
    window.clipboard_append(cp)


window = tkinter.Tk()
window.title("Password Generator")
window.geometry("320x270")
window.resizable(False, False)

output = tkinter.Entry(window,width=23)
output.place(x=160, y=200, anchor="center")


cbu = LabeledCheckbutton(window)
cbu.label.configure(text="Upper letters")
cbu.grid(row=0, column=0)
cbu.place(x=40, y=50, anchor="center")
cbu.setvar("bool", "False")


cbl = LabeledCheckbutton(window)
cbl.label.configure(text="Lower letters")
cbl.grid(row=0, column=0)
cbl.place(x=122, y=50, anchor="center")


cbn = LabeledCheckbutton(window)
cbn.label.configure(text="Numbers")
cbn.grid(row=0, column=0)
cbn.place(x=203, y=50, anchor="center")


cbs = LabeledCheckbutton(window)
cbs.label.configure(text="Symbols")
cbs.grid(row=0, column=0)
cbs.place(x=284, y=50, anchor="center")

entry = LabeledEntry()
entry.label.configure(text="Length (max 84):")
entry.entry.configure(width=5)
entry.entry.insert(0, "8")
entry.place(x=160, y=100, anchor="center")

upper_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_letters = "qwertyuiopasdfghjklzxcvnm"
nums = "0123456789"
symbols = "[]{}();:,.'\\?-_=@#$%^&*"


generate = tkinter.Button(window, text='Generate password', width=20,
                          command=display_password)
generate.place(x=160, y=150, anchor="center")

save = tkinter.Button(window, text="Save", command=savefile)
save.place(x=180, y=240, anchor="center")

copy = tkinter.Button(window, text="Copy",command=copy_password)
copy.place(x=130, y=240, anchor="center")
window.mainloop()
