Hello friend!

* This is our group project assessment 3 for the Network Automation class at TAFE Meadowbank Sem-2/2021.
* The purpose of this project is to simulate how network management can be simplified when using automation of configuration commands on Cisco Routers. 
* The program uses the Python library Netmiko to enable remote automation of configurations via SSH, and provides a GUI interface for easier interaction.

The following system requirements must be installed to allow the full execution of the application:

- GNS3 v2.2.23 (or above) with Cisco CSR1000 v16.12.3 image (or above) 
- GNS3 VM installed on VMware Workstation
- Network Topology - available at https://tafensw-my.sharepoint.com/:u:/g/personal/murilo_de_studytafensw_edu_au/EZKgmMas1Z5FtTIPlKowPngB3GlKtuySAbkmLL9FvoYSxQ?e=kbDxaf
- Python 3 with an Integrated Development Environment (IDE). Eg: Pycharm
- Cisco Webex 

Step 1: Clone this repository into your IDE
Step 2: Configure devices with initial configurations from file "initial device configurations" 
Step 2: Check IP address of each router and update the file devices.yaml with the corresponding IP addresses.
Note: This program requires SSH connection between your host machine and the VMs. Please make sure host and VMs can establish SSH connection before proceeding.

Step 4: Update the variables "access_token" and "room_id" with your own details in the Automation_functions.py script to enable Webex API to send updates to your group.
Step 5: To start the program, run the Authentication 1.py script
Step 6: Authenticate with USERNAME = admin and PASSWORD = xgroup1
Step 7: Close the Authentication screen
Step 8: You can now select the desired configuration options from the menu

Please feel free to send us any ideas/suggestions of improvements for this project. 
We hope you enjoy it!

