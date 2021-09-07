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



R1NET=["router ospf 1","network 192.168.2.0 0.0.0.255 area 0","network 192.168.3.0 0.0.0.255 area 0","router-id 1.1.1.1","exit","int gig2","ip ospf authentication"
        ,"ip ospf auth message-digest","ip ospf message-digest-key 1 MD5 xgroup"]

R2NET=["router ospf 1","network 192.168.2.0 0.0.0.255 area 0","network 192.168.4.0 0.0.0.255 area 0","router-id 2.2.2.2","exit","int gig2","ip ospf authentication"
        ,"ip ospf auth message-digest","ip ospf message-digest-key 1 MD5 xgroup"]


net_connect = ConnectHandler(**R1)
outputR1 = net_connect.send_config_set(R1NET)
print(outputR1)

net_connect = ConnectHandler(**R2)
outputR2 = net_connect.send_config_set(R2NET)
print(outputR2)


#Markdown message
import requests
access_token = 'MThlNTc2MzUtNGRkNy00YThhLThlNTgtZGQwN2YyNmRmZjk1ZWU4ZWNlNGQtZDBh_P0A1_449e6dbf-9e56-4a02-b469-235f2959d30d'
room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
message = 'Hello **xGroup Team**!! \n The OSPF configuration have been updated on R1 and R2 devices.'
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
