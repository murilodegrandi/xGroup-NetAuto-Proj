import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("xGroup Network Automation Tool")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('topolog.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#Instructions
instructions = tk.Label(root, text='Please choose a device to start the configuration', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

#Building buttons


runConf = tk.StringVar()
button = tk.Button(root, textvariable=runConf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35)
runConf.set('Router 1')
button.grid(column=1, row=2)

show_OSPF = tk.StringVar()
button = tk.Button(root, textvariable=show_OSPF, font='Raleway', bg='#3399FF', fg='white', height=2, width=35)
show_OSPF.set('Router 2')
button.grid(column=1, row=3)

root.mainloop()