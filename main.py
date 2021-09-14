# This is the core file. Its functions will be called automatically when show/conf files are running.

import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

class functions:
    def __init__(self,device,commands):
        self.device = device
        self.commands = commands

    def send_show_command(self):# function to verify config
        try:
            with ConnectHandler(**self.device) as ssh:
                ssh.enable()
                for command in self.commands:
                    output = ssh.send_command(command)
                    print(output)
            return output
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)

    def send_config(self): # function to configure device
        try:
            with ConnectHandler(**self.device) as ssh:
                ssh.enable()
                output = ssh.send_config_set(self.commands)
                print(output)
            return output
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)

def inventory(): # function to load information from devices
    try:
        with open("devices.yaml") as f:
            devices = f.read()
        inventory_dict = yaml.load(devices)
        return inventory_dict
    except:
        print("Error when loading inventory from file!")




