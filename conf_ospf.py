import main
import requests
devices = main.inventory() #load devices

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


#Webex update
access_token = 'YjFhMDZkNDItYWZkMC00MTE0LTgyYWItNjg3ODAzMjhiNmVmM2Q3ZjQxMTktNmI1_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
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
