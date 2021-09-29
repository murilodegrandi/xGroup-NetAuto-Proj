import tkinter as tk
from PIL import Image, ImageTk
import Automation_functions
#import main

root = tk.Tk()
root.title("xGroup Network Automation Tool")

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

sh_ip_Route = tk.StringVar()
button = tk.Button(root, textvariable=sh_ip_Route, font='Raleway', bg='#3399FF', fg='white', height=2, width=35, command=lambda:Automation_functions.sh_routes())
sh_ip_Route.set('Show IP Route')
button.grid(column=1, row=6)

int_conf = tk.StringVar()
button = tk.Button(root, textvariable=int_conf, font='Raleway', bg='#3399FF', fg='white', height=2, width=35, command=lambda:Automation_functions.interf_conf())
int_conf.set('Create Interface')
button.grid(column=1, row=7)

sh_Time = tk.StringVar()
button = tk.Button(root, textvariable=sh_Time, font='Raleway', bg='#3399FF', fg='white', height=2, width=35, command=lambda:Automation_functions.sh_time())
sh_Time.set('Show Time')
button.grid(column=1, row=8)


#Show configurations
e = tk.Text(root, height=15, width=60, borderwidth=5)
e.grid(row=9, column=1, padx=10, pady=10)


root.mainloop()

