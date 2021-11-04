
########################################################################################################################
############################################   GUI Interface   #########################################################
########################################################################################################################

import tkinter as tk
from PIL import Image, ImageTk
import main
import Automation_functions


root = tk.Tk()
root.title("xGroup Network Automation Tool")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3) #canvas.grid(columnspan=3, rowspan=3)


#logo
logo = Image.open('logo.PNG')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# ###Adding topology####
topology = Image.open('topology.jpg')
topology = ImageTk.PhotoImage(topology)
topology_lab = tk.Label(image=topology)
topology_lab.grid(column=2, row=0)

#Instructions
instructions = tk.Label(root, text='Please select a configuration option', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

##############################################Building buttons##########################################################

runConf_R1 = tk.StringVar()
button = tk.Button(root, textvariable=runConf_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.sh_run('R1'))
runConf_R1.set('Show Running Configuration R1')
button.grid(column=1, row=2)

runConf_R2 = tk.StringVar()
button = tk.Button(root, textvariable=runConf_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.sh_run('R2'))
runConf_R2.set('Show Running Configuration R2')
button.grid(column=2, row=2)

###

show_OSPF_R1 = tk.StringVar()
button = tk.Button(root, textvariable=show_OSPF_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.sh_ospf('R1'))
show_OSPF_R1.set('Show OSPF Configurations R1')
button.grid(column=1, row=3)

show_OSPF_R2 = tk.StringVar()
button = tk.Button(root, textvariable=show_OSPF_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.sh_ospf('R2'))
show_OSPF_R2.set('Show OSPF Configurations R2')
button.grid(column=2, row=3)

###

NTP_conf_R1 = tk.StringVar()
button = tk.Button(root, textvariable=NTP_conf_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.ntp_conf('R1'))
NTP_conf_R1.set('NTP Configuration R1')
button.grid(column=1, row=4)

NTP_conf_R2 = tk.StringVar()
button = tk.Button(root, textvariable=NTP_conf_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.ntp_conf('R2'))
NTP_conf_R2.set('NTP Configuration R2')
button.grid(column=2, row=4)

###

OSPF_conf_R1 = tk.StringVar()
button = tk.Button(root, textvariable=OSPF_conf_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.ospf_conf('R1'))
OSPF_conf_R1.set('OSPF Configuration R1')
button.grid(column=1, row=5)

OSPF_conf_R2 = tk.StringVar()
button = tk.Button(root, textvariable=OSPF_conf_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.ospf_conf('R2'))
OSPF_conf_R2.set('OSPF Configuration R2')
button.grid(column=2, row=5)

###

sh_ip_Route_R1 = tk.StringVar()
button = tk.Button(root, textvariable=sh_ip_Route_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.sh_routes('R1'))
sh_ip_Route_R1.set('Show IP Route R1')
button.grid(column=1, row=6)

sh_ip_Route_R2 = tk.StringVar()
button = tk.Button(root, textvariable=sh_ip_Route_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.sh_routes('R2'))
sh_ip_Route_R2.set('Show IP Route R2')
button.grid(column=2, row=6)

###

int_conf_R1 = tk.StringVar()
button = tk.Button(root, textvariable=int_conf_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.interf_conf('R1'))
int_conf_R1.set('Create Interface R1')
button.grid(column=1, row=7)

int_conf_R2 = tk.StringVar()
button = tk.Button(root, textvariable=int_conf_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.interf_conf('R2'))
int_conf_R2.set('Create Interface R2')
button.grid(column=2, row=7)

###

sh_Time_R1 = tk.StringVar()
button = tk.Button(root, textvariable=sh_Time_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.sh_time('R1'))
sh_Time_R1.set('Show Clock R1')
button.grid(column=1, row=8)

sh_Time_R2 = tk.StringVar()
button = tk.Button(root, textvariable=sh_Time_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:Automation_functions.sh_time('R2'))
sh_Time_R2.set('Show Clock R2')
button.grid(column=2, row=8)

root.mainloop()
