import main
import requests

def sh_run():
    devices = main.inventory()  # load devices

    # load device information and send show command.
    for device in devices:
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


def sh_ospf():
    devices = main.inventory()  # load devices

    # load device information and send show command.
    for device in devices:
        for i in devices[device]:
            show = main.functions(i, ["show ip ospf database", "show ip ospf neighbor"])
            show.send_show_command()
            print("-" * 100)

    # Webex update
    access_token = 'YTg3Y2ZiZTgtMWRjYi00MDUxLTkxNWItNGVlNzQ3MTQxYzRmYjIxZTdkYmEtMzJm_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
    room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
    message = 'Hello **xGroup Team**!! \n. OSPF configuration has been checked.'
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())


def ospf_conf():
    devices = main.inventory()  # load devices

    for device in devices['R1']:
        R1 = device
        commands = ["router ospf 2", "router-id 1.1.1.1", "network 192.168.2.0 0.0.0.255 area 0"
            , "network 192.168.3.0 0.0.0.255 area 0", "exit", "int gig2", "ip ospf authentication"
            , "ip ospf auth message-digest", "ip ospf message-digest-key 1 MD5 xgroup"]
        config = main.functions(R1, commands)
        config.send_config()

    for device in devices['R2']:
        R2 = device
        commands = ["router ospf 2", "router-id 2.2.2.2", "network 192.168.2.0 0.0.0.255 area 0"
            , "network 192.168.4.0 0.0.0.255 area 0", "exit", "int gig2", "ip ospf authentication"
            , "ip ospf auth message-digest", "ip ospf message-digest-key 1 MD5 xgroup"]
        config = main.functions(R2, commands)
        config.send_config()

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


def ntp_conf():
    devices = main.inventory()  # load devices

    for device in devices['R1']:  # configure R1 as NTP Server
        R1 = device
        commands = ["clock timezone AEST +10", "ntp server 216.239.35.0"]
        config = main.functions(R1, commands)
        config.send_config()

    for device in devices['R2']:  # configure R2 as NTP Client
        R2 = device
        commands = ["clock timezone AEST +10", "ntp server 192.168.2.1"]
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


def sh_routes():
    devices = main.inventory()  # load devices

    # load device information and send show command.
    for device in devices:
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

