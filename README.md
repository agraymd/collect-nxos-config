# collect-nxos-config
Collect the running configuration from a list of NX-OS devices and save in the directory where the script is executed as &lt;devicename-config.log>. 


# Python Script to Quickly Collect Lab Configurations 
# Introduction

The purpose of this script is to quickly collect configurations from lab devices. 

The script will save the configuration of each device you specify in the following format: 
    $DEVICENAME-config.log

The script will save the files in the directory where the script is executed. By using environment variables, we can make this quick and easy.  


# Requirements

-	The script assumes that the devices are using <admin> and <cisco!123> as the username and password. 

-	You must have python3 installed on your machine. 

-	You must install the Netmiko module:
https://pypi.org/project/netmiko/

-	Devices much be reachable via mgmt0 from your machine.

 
# Using the Script (MacOS) 

This step is optional however will make using the script much quicker and easier. 

If you are using BASH as your shell this will work for you, if you are using zsh you will need to adapt accordingly. 


## Setting the environment variable 

My bash profile is stored at /Users/alegray. The contents of the file are as follows: 


export PATH='YOUR-PATH-HERE’
export collectconfig='python3 /Users/username/Documents/path/to-script/collect-lab-config.py'



The bolded portion ensures that each time I open the terminal, I have an environment variable $collectconfig available to me. 

This variable just uses python to execute the script and specifies the full path where the script is saved, which is what you would need to change to match your system. 

This allows for quick collection of lab configurations once you have a list of IP addresses for each switch’s mgmt0 interface. 

 
## Example Usage: 

We have just finished a lab setup and want to collect configurations from 7 devices: 

10.122.176.225 
10.122.176.150 
10.122.176.137 
10.122.177.11 
10.122.176.212 
10.122.176.167 
10.122.176.168

We will create and change to a directory where we want to save the configurations, call the script, and provide the IP addresses in a list with a single space between them: 


YOUR-MACHINE:~ your-user$ mkdir ./test && cd ./test && $collectconfig
Enter device IP addresses in X.X.X.X format separated by a single space: 10.122.176.225 10.122.176.150 10.122.176.137 10.122.177.11 10.122.176.212 10.122.176.167 10.122.176.168
Device1 completed.
Device2 completed.
Device3 completed.
Device4 completed.
Device5 completed.
Device6 completed.
Device7 completed.



# Summary 

This is the basic idea of using the script. You can achieve similar results with windows, or simply specify the full path to the script when you want to run it. To me this is faster than using a terminal program or something else to collect the running configurations. 





 
