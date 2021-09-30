from tkinter import *
from tkinter import messagebox
import Automation_functions

#from sys import exit

w = Tk()
w.geometry('700x500')
w.title('X-Group LOGIN ACCES')
w.resizable(0, 0)

j = 0
r = 0
for i in range(100):
    # c = str(222222+r)
    Frame(w, width=10, height=500, bg='#2832C2').place(x=j, y=0)
    j = j + 10
    r = r + 1

Frame(w, width=600, height=400, bg='white').place(x=50, y=50)

l1 = Label(w, text='USERNAME', bg='white')
l = ('consoles', 15)
l1.config(font=l)
l1.place(x=80, y=200)

# first label
e1 = Entry(w, width=20, border=0)
e1.config(font=l)
e1.place(x=80, y=230)

# second label

l2 = Label(w, text='PASSWORD', bg='white')
l = ('consoles', 15)
l2.config(font=l)
l2.place(x=80, y=280)

e2 = Entry(w, width=20, border=0, show='*')
e2.config(font=l)
e2.place(x=80, y=310)

Frame(w, width=180, height=2, bg='#141414').place(x=80, y=250)
Frame(w, width=180, height=2, bg='#141414').place(x=80, y=330)

from PIL import ImageTk, Image

image1 = Image.open('img.png')
image2 = ImageTk.PhotoImage(image1)
label1 = Label(image=image2, border=0, justify=CENTER)
label1.place(x=350, y=120)


def cmd():
    if e1.get() == 'admin' and e2.get() == 'xgroup1':
        messagebox.showinfo('SUCCESFULL LOGIN ', 'WELCOME TO XGROUP')

        mainloop()

        exec(open('xGroupGUI.py').read())

    else:
        messagebox.showinfo('WRONG CREDENTIALS', 'PLEASE TRY AGAIN ')

Button(w, width=20, height=2, fg='white', bg='#2832C2', border=0, command=cmd, text='L O G I N').place(x=100, y=375)

w.mainloop()