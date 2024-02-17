from tkinter import *
from tkinter import messagebox
from final import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Diabetes Prediction System")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

fields = 'Pregnancies','Glucose','Blood Pressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'

global a
global b
b = []
a = []

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = float(entry[1].get())
        a.append(text)
        print('%s: "%s"' % (field, text))       # tkinter print with field name
    b.append(a)

    BackEnd.knn(BackEnd)                        # calling knn from final
    res = BackEnd.predictor(b)                  # calling predictor from final
    if res == 1:
        positive()
    else:
        negative()


def makeform(root, fields):
    entries = []
    for i in fields:
        row = Frame(root)
        lab = Label(row, width=25, text=i, anchor='w')
        ent = Entry(row)  # get entry
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((i, ent))
    return entries


def positive():
    messagebox.showinfo(title="Prediction", message="Diabetes is Positive")
    root.quit()

def negative():
    messagebox.showinfo(title="Prediction", message="Diabetes is Negative")
    root.quit()


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Exit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)

app = Window(root)
root.mainloop()
