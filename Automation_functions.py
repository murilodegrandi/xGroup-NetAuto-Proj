import main
import requests

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
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")



#######################################################################################################################
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
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")


########################################################################################################################
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
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

########################################################################################################################
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

        # webex update
        access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
        room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
        message = 'Hello **xGroup Team**!! \n. Time synchronization has been verified.'
        url = 'https://webexapis.com/v1/messages'
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'markdown': message}
        res = requests.post(url, headers=headers, json=params)
        print(res.json())
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

########################################################################################################################
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

# Webex update
        access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
        room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
        message = 'Hello **xGroup Team**!! \n. A new interface has been created on R1!'
        url = 'https://webexapis.com/v1/messages'
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'markdown': message}
        res = requests.post(url, headers=headers, json=params)
        print(res.json())
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

########################################################################################################################
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
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")


########################################################################################################################
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

# Webex update
        access_token = 'MGIyNzFhOTMtNWQ5OC00OTI3LTgxMzctYjZkZDZmOTQ3OTkzMjY2Y2IyMjktNTMx_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
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
    except:
        print("Error while processing your request! Please try again or contact the system administrator.")

########################################################################################################################

