import main
import requests

########################################################################################################################
############################################   Automation Functions   ##################################################
########################################################################################################################

# This function loads device information and send show command to verify show running config.
def sh_run(router):
    try:
        file = main.config()
        devices = main.inventory()
        device = router
        for dev in devices[device]:
            commands = file['SHOW_RUN']
            config = main.functions(dev, commands)
            config.send_show_command()
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

    # webex update
    access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. Running configuration has been checked.'
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

########################################################################################################################
# This function loads device information and send show commands to verify OSPF

def sh_ospf(router):
    try:
        file = main.config()
        devices = main.inventory()
        device = router
        for dev in devices[device]:
            commands = file['SHOW_OSPF']
            config = main.functions(dev, commands)
            config.send_show_command()
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

    # Webex update
    access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. OSPF configuration has been checked'
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

########################################################################################################################
#This function loads device information and send show command to verify the routing tables.

def sh_routes(router):
    try:
        file = main.config()
        devices = main.inventory()
        device = router
        for dev in devices[device]:
            commands = file['SHOW_ROUTE']
            config = main.functions(dev, commands)
            config.send_show_command()
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

    # webex update
    access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. Routes have been checked.'
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

########################################################################################################################
# This function loads device information and send show command to verify the Time synchronization.

def sh_time(router): # load devices
    try:
        file = main.config()
        devices = main.inventory()
        device = router
        for dev in devices[device]:
            commands = file['SHOW_TIME']
            config = main.functions(dev, commands)
            config.send_show_command()
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

    # webex update
    access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. Time synchronization has been checked.'
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

########################################################################################################################
#This function loads device information and send configuration to create a new interface.

def interf_conf(router):
    try:
        file = main.config()
        devices = main.inventory()
        device = router

        for dev in devices[device]:  # configure OSPF on R1
            if device == 'R1':
                commands = file['INTERF_R1']
                config = main.functions(dev, commands)
                config.send_config()
            elif device == 'R2':
                commands = file['INTERF_R2']
                config = main.functions(dev, commands)
                config.send_config()
            else:
                print("Device not found!")

    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

    # Webex update
    access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. A Loopback interface has been created.'
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

########################################################################################################################
# This function loads device information and send configuration for OSPF

def ospf_conf(router):
    try:
        file = main.config()
        devices = main.inventory()
        device = router

        for dev in devices[device]: # configure OSPF on R1
            if device == 'R1':
                commands = file['OSPF_R1']
                config = main.functions(dev, commands)
                config.send_config()
            elif device == 'R2':
                commands = file['OSPF_R2']
                config = main.functions(dev, commands)
                config.send_config()
            else:
                print("Device not found!")

    except:
        print("Error while processing your request! Please try again or contact the system administrator.")


    # Webex update
    access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. OSPF configuration has been updated!'
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

########################################################################################################################
#This function loads device information and send configuration for NTP

def ntp_conf(router):
    try:
        file = main.config()
        devices = main.inventory()
        device = router

        for dev in devices[device]: # configure OSPF on R1
            if device == 'R1':
                commands = file['NTP_R1']
                config = main.functions(dev, commands)
                config.send_config()
            elif device == 'R2':
                commands = file['NTP_R2']
                config = main.functions(dev, commands)
                config.send_config()
            else:
                print("Device not found!")

    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

    # Webex update
    access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. The NTP service has been configured.'
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

#END of Automation Functions


########################################################################################################################
############################################   GUI Interface   #########################################################
########################################################################################################################

import tkinter as tk
from PIL import Image, ImageTk
import main


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
button = tk.Button(root, textvariable=runConf_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:sh_run('R1'))
runConf_R1.set('Show Running Configuration R1')
button.grid(column=1, row=2)

runConf_R2 = tk.StringVar()
button = tk.Button(root, textvariable=runConf_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:sh_run('R2'))
runConf_R2.set('Show Running Configuration R2')
button.grid(column=2, row=2)

###

show_OSPF_R1 = tk.StringVar()
button = tk.Button(root, textvariable=show_OSPF_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:sh_ospf('R1'))
show_OSPF_R1.set('Show OSPF Configurations R1')
button.grid(column=1, row=3)

show_OSPF_R2 = tk.StringVar()
button = tk.Button(root, textvariable=show_OSPF_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:sh_ospf('R2'))
show_OSPF_R2.set('Show OSPF Configurations R2')
button.grid(column=2, row=3)

###

NTP_conf_R1 = tk.StringVar()
button = tk.Button(root, textvariable=NTP_conf_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:ntp_conf('R1'))
NTP_conf_R1.set('NTP Configuration R1')
button.grid(column=1, row=4)

NTP_conf_R2 = tk.StringVar()
button = tk.Button(root, textvariable=NTP_conf_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:ntp_conf('R2'))
NTP_conf_R2.set('NTP Configuration R2')
button.grid(column=2, row=4)

###

OSPF_conf_R1 = tk.StringVar()
button = tk.Button(root, textvariable=OSPF_conf_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:ospf_conf('R1'))
OSPF_conf_R1.set('OSPF Configuration R1')
button.grid(column=1, row=5)

OSPF_conf_R2 = tk.StringVar()
button = tk.Button(root, textvariable=OSPF_conf_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:ospf_conf('R2'))
OSPF_conf_R2.set('OSPF Configuration R2')
button.grid(column=2, row=5)

###

sh_ip_Route_R1 = tk.StringVar()
button = tk.Button(root, textvariable=sh_ip_Route_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:sh_routes('R1'))
sh_ip_Route_R1.set('Show IP Route R1')
button.grid(column=1, row=6)

sh_ip_Route_R2 = tk.StringVar()
button = tk.Button(root, textvariable=sh_ip_Route_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:sh_routes('R2'))
sh_ip_Route_R2.set('Show IP Route R2')
button.grid(column=2, row=6)

###

int_conf_R1 = tk.StringVar()
button = tk.Button(root, textvariable=int_conf_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:interf_conf('R1'))
int_conf_R1.set('Create Interface R1')
button.grid(column=1, row=7)

int_conf_R2 = tk.StringVar()
button = tk.Button(root, textvariable=int_conf_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:interf_conf('R2'))
int_conf_R2.set('Create Interface R2')
button.grid(column=2, row=7)

###

sh_Time_R1 = tk.StringVar()
button = tk.Button(root, textvariable=sh_Time_R1, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:sh_time('R1'))
sh_Time_R1.set('Show Clock R1')
button.grid(column=1, row=8)

sh_Time_R2 = tk.StringVar()
button = tk.Button(root, textvariable=sh_Time_R2, font='Raleway', bg='#3399FF', fg='white', height=1, width=30, command=lambda:sh_time('R2'))
sh_Time_R2.set('Show Clock R2')
button.grid(column=2, row=8)

root.mainloop()
