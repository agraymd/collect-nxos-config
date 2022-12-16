from netmiko import ConnectHandler
import sys
import time
import argparse
import re
import ipaddress 

# Define function to get and print running config.
def get_running_config(ip):
        device_info = { 
            "device_type": "cisco_nxos",
            "host": ip,
            "username": "admin",
            "password": "cisco!123",
        }

        # Show command that we execute.
        command = "show run | no"

        # Connect to device and execute the command.
        with ConnectHandler(**device_info) as net_connect:
            running_config = net_connect.send_command(command)

        # Test print, this should be replaced with unittest or something better. 
        # print(type(output))
        return running_config


# Defines function for parsing running config for hostname.
def get_switchname_from_config(string):
        # Parses output string for switchname using regex to match everything after 'hostname '. Stores in variable switchname.
        switchname_regex = re.compile('(?<=hostname\s).*|(?<=switchname\s).*')
        switchname_results = switchname_regex.search(string)
        switchname = switchname_results.group()
        # Debug print.
        # print(switchname_results)
        return switchname
        

# Define function for creating file with name of switch-config.log, putting config in the file, saving the file.
def create_file(filename, content):
    f = open(filename, "w")
    f.write(content)


# Take user input and store it for splitting into a list 
input_string = input('Enter device IP addresses in X.X.X.X format separated by a single space: ')

# Split the user input into a list stored in device_ip_list. We need to find a way to validate the user input here!!! 
device_ip_list = input_string.split()

# Use ipaddress module to validate each item in the list is a valid IP address. Exit if any entry fails.

try: 
    for ip in device_ip_list:
        ipaddress.ip_address(ip)

except ValueError:
    print('Invalid input supplied. ' + ip + ' is invalid not a valid IP address.')
    sys.exit(1)

# Loop through each IP in the list and get the running config, get the switchname, and create/save the file  
for ip in device_ip_list:
    config = get_running_config(ip)
    switchname = get_switchname_from_config(config)
    create_file(switchname + '-config.log', config)
    print(switchname + ' completed.')   
