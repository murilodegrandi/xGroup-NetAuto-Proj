import main
import yaml
import requests
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
for device in devices:
    show = main.functions(device, ["show run"])
    show.send_show_command()

#webex update
access_token = 'MzJmMjk2OTAtZGQwOC00NDkzLWJmODEtMmViZTVjZDRlNWYwM2Q4MWQxYjUtYWFl_P0A1_4524b9d6-104d-4af3-9067-7d3921fc14da'
room_id = 'bfcc5ae0-f41a-11eb-9094-4d9b22f98f5e'
message = 'Hello **xGroup Team**!! \n.'
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())