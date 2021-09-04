import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('xGroup logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#Instructions
instructions = tk.Label(root, text='Please select a configuration option', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

#Building buttons
Deployment_runConf = tk.StringVar()
Deployment_button = tk.Button(root, textvariable=Deployment_runConf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35)
Deployment_runConf.set('Running Configuration')
Deployment_button.grid(column=1, row=2)

Deployment_basicConf = tk.StringVar()
Deployment_button = tk.Button(root, textvariable=Deployment_basicConf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35)
Deployment_basicConf.set('Basic Configuration')
Deployment_button.grid(column=1, row=3)

Deployment_interfaceConf = tk.StringVar()
Deployment_button = tk.Button(root, textvariable=Deployment_interfaceConf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35)
Deployment_interfaceConf.set('Interface Configuration')
Deployment_button.grid(column=1, row=4)

Deployment_ospf = tk.StringVar()
Deployment_button = tk.Button(root, textvariable=Deployment_ospf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35)
Deployment_ospf.set('OSPF')
Deployment_button.grid(column=1, row=5)

root.mainloop()