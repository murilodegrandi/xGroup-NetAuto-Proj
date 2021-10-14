import tkinter as tk
from PIL import Image, ImageTk
import Automation_functions
import main
import tkinter.messagebox

root = tk.Tk()
root.title("xGroup Network Automation Tool")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3) #canvas.grid(columnspan=3, rowspan=3)

def cmd():
    if e1.get() == 'admin' and e2.get() == 'xgroup1':
        messagebox.showinfo('SUCCESFULL LOGIN ', 'WELCOME TO XGROUP')

        root.mainloop()

        exec(open('xGroupGUI.py').read())

    else:
        messagebox.showinfo('WRONG CREDENTIALS', 'PLEASE TRY AGAIN ')

Button(root, width=20, height=2, fg='white', bg='#2832C2', border=0, command=cmd, text='L O G I N').place(x=100, y=375)

#logo
logo = Image.open('img.png')
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

####################3Building buttons##################################3
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


#Show configurations

e1 = tk.Text(root, height=5, width=50, borderwidth=5)
e1.grid(row=9, column=1, padx=10, pady=10)
e1.insert(tk.END, 'TO DISPALY R1 INFO')

e2 = tk.Text(root, height=5, width=50, borderwidth=5)
e2.grid(row=9, column=2, padx=10, pady=10)
e2.insert(tk.END, 'TO DISPALY R2 INFO')




root.mainloop()

