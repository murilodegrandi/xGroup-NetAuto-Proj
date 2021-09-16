import tkinter as tk
from PIL import Image, ImageTk
import Automation_functions
#import main
#import yaml



root = tk.Tk()
root.title("xGroup Network Automation Tool")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('x1.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#Instructions
instructions = tk.Label(root, text='Please select a configuration option', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

#Building buttons
runConf = tk.StringVar()
button = tk.Button(root, textvariable=runConf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35, command=lambda:Automation_functions.sh_run())
runConf.set('Show Running Configuration')
button.grid(column=1, row=2)

show_OSPF = tk.StringVar()
button = tk.Button(root, textvariable=show_OSPF, font='Raleway', bg='#3399FF', fg='white', height=2, width=35, command=lambda:Automation_functions.sh_ospf())
show_OSPF.set('Show OSPF Configurations')
button.grid(column=1, row=3)

NTP_conf = tk.StringVar()
button = tk.Button(root, textvariable=NTP_conf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35, command=lambda:Automation_functions.ntp_conf())
NTP_conf.set('NTP Configuration')
button.grid(column=1, row=4)

OSPF_conf = tk.StringVar()
button = tk.Button(root, textvariable=OSPF_conf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35, command=lambda:Automation_functions.ospf_conf())
OSPF_conf.set('OSPF Configuration')
button.grid(column=1, row=5)

OSPF_conf = tk.StringVar()
button = tk.Button(root, textvariable=OSPF_conf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35, command=lambda:Automation_functions.sh_routes())
OSPF_conf.set('Show IP Route')
button.grid(column=1, row=6)

root.mainloop()

