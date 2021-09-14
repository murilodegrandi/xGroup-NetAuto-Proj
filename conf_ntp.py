import main
import requests
devices = main.inventory() #load devices

for device in devices['R1']: #configure R1 as NTP Server
    R1 = device
    commands = ["clock timezone AEST +10","ntp server 216.239.35.0"]
    config = main.functions(R1, commands)
    config.send_config()

for device in devices['R2']: #configure R2 as NTP Client
    R2 = device
    commands = ["clock timezone AEST +10", "ntp server 192.168.2.1"]
    config = main.functions(R2, commands)
    config.send_config()


#Webex update
access_token = 'YjFhMDZkNDItYWZkMC00MTE0LTgyYWItNjg3ODAzMjhiNmVmM2Q3ZjQxMTktNmI1_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
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
