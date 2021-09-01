#!/usr/bin/env python

from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.105',
    'username': 'admin',
    'password': 'xgroup1',
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.102',
    'username': 'admin',
    'password': 'xgroup1',
}



R1NET=["router ospf 1","network 192.168.1.0 0.0.0.255 area 0","network 192.168.2.0 0.0.0.255 area 0","network 192.168.3.0 0.0.0.255 area 0","router-id 1.1.1.1","exit","int gig2","ip ospf authentication"
        ,"ip ospf auth message-digest","ip ospf message-digest-key 1 MD5 xgroup"]

R2NET=["router ospf 1","network 192.168.1.0 0.0.0.255 area 0","network 192.168.2.0 0.0.0.255 area 0","network 192.168.4.0 0.0.0.255 area 0","router-id 2.2.2.2","exit","int gig2","ip ospf authentication"
        ,"ip ospf auth message-digest","ip ospf message-digest-key 1 MD5 xgroup"]


net_connect = ConnectHandler(**R1)
outputR1 = net_connect.send_config_set(R1NET)
print(outputR1)

net_connect = ConnectHandler(**R2)
outputR2 = net_connect.send_config_set(R2NET)
print(outputR2)