from netmiko import ConnectHandler
device = ConnectHandler(device_type='cisco_ios', ip='192.168.255.249', username='cisco', password='cisco')


output = device.send_command("show version")
print (output)


#Note: the user 'cisco' has priviledge level 15, normal user need to provide 'secret="cisco123!"' as part of the connection request paramiter
#After the connection, normal user need to use 'device.enable()' to enter to the enable mode


print ("Before config push")

output = device.send_command("show running-config interface GigabitEthernet 1")
print (output)

#for config push, we do not have to perform any additional configurations but just specify the commands in the same order as we send them manually to the router in a list, and pass that list as an argument to the send_config_set function. 
configcmds=["interface G1", "description my test"]
device.send_config_set(configcmds)

print ("After config push")
output = device.send_command("show running-config interface GigabitEthernet 1")
print (output)

device.send_command("write memory")

device.disconnect()
