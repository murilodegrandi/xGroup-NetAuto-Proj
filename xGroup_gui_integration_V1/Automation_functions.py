import main
import requests

# This function loads device information and send show command to verify show running config.
def sh_run():
    devices = main.inventory()  # load devices

    for device in devices: # send show command
        for i in devices[device]:
            show = main.functions(i, ["show run"])
            show.send_show_command()
            print("-" * 100)

    # webex update
    access_token = 'YTg3Y2ZiZTgtMWRjYi00MDUxLTkxNWItNGVlNzQ3MTQxYzRmYjIxZTdkYmEtMzJm_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
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

def sh_ospf():
    devices = main.inventory()  # load devices

    for device in devices: # send show commands
        for i in devices[device]:
            show = main.functions(i, ["show ip ospf database", "show ip ospf neighbor"])
            show.send_show_command()
            print("-" * 100)

    # Webex update
    access_token = 'YTg3Y2ZiZTgtMWRjYi00MDUxLTkxNWItNGVlNzQ3MTQxYzRmYjIxZTdkYmEtMzJm_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
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
# This function loads device information and send configuration for OSPF

def ospf_conf(router):
    try:
        config_ospf = main.config()
        devices = main.inventory()
        device = router

        for dev in devices[device]: # configure OSPF on R1
            if device == 'R1':
                commands = config_ospf['OSPF_R1']
            elif device == 'R2':
                commands = config_ospf['OSPF_R2']
            else:
                print("Device not found!")
            config = main.functions(dev, commands)
            config.send_config()
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")


    # Webex update
    access_token = 'YTg3Y2ZiZTgtMWRjYi00MDUxLTkxNWItNGVlNzQ3MTQxYzRmYjIxZTdkYmEtMzJm_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
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

def ntp_conf():
    devices = main.inventory()  # load devices

    for device in devices['R1']:  # configure R1 as NTP Server
        R1 = device
        commands = ["clock timezone AEST +10", "ntp server 216.239.35.0"]
        config = main.functions(R1, commands)
        config.send_config()

    for device in devices['R2']:  # configure R2 as NTP Client
        R2 = device
        commands = ["clock timezone AEST +10", "ntp server 192.168.255.255"]
        config = main.functions(R2, commands)
        config.send_config()

    # Webex update
    access_token = 'YTg3Y2ZiZTgtMWRjYi00MDUxLTkxNWItNGVlNzQ3MTQxYzRmYjIxZTdkYmEtMzJm_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. Time synchronization has been configured for R1 and R2!'
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

def sh_routes():
    devices = main.inventory()  # load devices


    for device in devices: # load device information and send show command.
        for i in devices[device]:
            show = main.functions(i, ["show ip route"])
            show.send_show_command()
            print("-" * 100)

    # webex update
    access_token = 'YTg3Y2ZiZTgtMWRjYi00MDUxLTkxNWItNGVlNzQ3MTQxYzRmYjIxZTdkYmEtMzJm_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
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

################################ below are NEW FUNCTIONS TO BE ADDED to GUI######################################

########################################################################################################################
#This function loads device information and send configuration to create a new interface.

def interf_conf():
    devices = main.inventory()  # load devices

    for device in devices['R1']: #create new interface on R1
        R1 = device
        commands = ["interface loopback 0", "description This interface stays always UP for the NTP server.",
        "ip address 192.168.255.255 255.255.255.255"
        ]
        config = main.functions(R1, commands)
        config.send_config()

    # Webex update
    access_token = 'YTg3Y2ZiZTgtMWRjYi00MDUxLTkxNWItNGVlNzQ3MTQxYzRmYjIxZTdkYmEtMzJm_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. A Loopback interface has been created on R1!'
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

def sh_time(): # load devices
    devices = main.inventory()

    for device in devices: # load device information and send show command.
        for i in devices[device]:
            show = main.functions(i, ["show clock"])
            show.send_show_command()
            print("-" * 100)

    # webex update
    access_token = 'YTg3Y2ZiZTgtMWRjYi00MDUxLTkxNWItNGVlNzQ3MTQxYzRmYjIxZTdkYmEtMzJm_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
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
