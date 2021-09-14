import main
import requests
devices = main.inventory() #load devices

# load device information and send show command.
for device in devices:
    for i in devices[device]:
        show = main.functions(i, ["show ip ospf database", "show ip ospf neighbor"])
        show.send_show_command()
        print("-"*100)

#Webex update
access_token = 'YjFhMDZkNDItYWZkMC00MTE0LTgyYWItNjg3ODAzMjhiNmVmM2Q3ZjQxMTktNmI1_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
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
