#!/usr/bin/env python

from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.108',
    'username': 'admin',
    'password': 'xgroup1',
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.107',
    'username': 'admin',
    'password': 'xgroup1',
}


R1NET="show ip route | begin Gateway"
R2NET="show ip route | begin Gateway"


net_connect = ConnectHandler(**R1)
outputR1 = net_connect.send_command(R1NET)
print(outputR1)

net_connect = ConnectHandler(**R2)
outputR2 = net_connect.send_command(R2NET)
print(outputR2)

with open("R1routes.txt", "w") as f1:
    f1.write(outputR1)
with open("R2routes.txt", "w") as f2:
    f2.write(outputR2)

#Markdown message
"""import requests
access_token = 'ZWVlZmY4ZGQtNGRhNC00MzEyLTgwNzQtYjQwY2Q3M2YwZDNiOTNhNTdkZGQtZTI3_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
message = 'Hello **xGroup Team**!! \n Routing Tables contain the following routes: \n ***R1*** \n {} \n\n\n \
          ***R2*** \n {}'.format(outputR1, outputR2)
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())"""
