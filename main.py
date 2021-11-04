import os
import datetime
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

    def send_show_command(self):# function to perform show commands
        try:
            with ConnectHandler(**self.device) as ssh:
                ssh.enable()
                for command in self.commands:
                    output = ssh.send_command(command)
                    #print(output)
                    t = datetime.datetime.now().strftime("%d.%m.%Y - %H;%M;%S")
                    with open("show_" + str(t) + ".txt", "w") as file:
                        file.write(output)
            os.startfile("C:\\Users\\muril\\PycharmProjects\\Network Automation\\xGroup\\xGroup_gui_integration_V1\\" + file.name)
            return output
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)

    def send_config(self): # function to add new configurations to devices
        try:
            with ConnectHandler(**self.device) as ssh:
                ssh.enable()
                output = ssh.send_config_set(self.commands)
                #print(output)
                t = datetime.datetime.now().strftime("%d.%m.%Y - %H;%M;%S")
                with open("config_" + str(t) + ".txt", "w") as file:
                    file.write(output)
            os.startfile("C:\\Users\\muril\\PycharmProjects\\Network Automation\\xGroup\\xGroup_gui_integration_V1\\" + file.name)
            return output

        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)

def inventory(): #loads information from devices
    try:
        with open("devices.yaml") as f:
            devices = f.read()
        inventory_dict = yaml.safe_load(devices)
        return inventory_dict
    except:
        print("Error while loading inventory from file!")

def config(): #loads device configurations file
    try:
        with open("config.yaml") as f:
            config = f.read()
        config_list = yaml.safe_load(config)
        return config_list
    except:
        print("Error while loading configs from file!")