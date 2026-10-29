#MAC Address is used to identify hardware within the network

#Why change the MAC(Media access control) Address?
#1-Increase anonymity
#2-Impersonate other devices
#3-Bypass filters

## LINUX MAC address change command
#sudo ifconfig eth0(network) down - disable network first
#sudo ifconfig eth0 hw ether 00:11:22:33:44:55 - change mac address
#sudo ifconfig eth0 up - enable network

#!/usr/bin/evn python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_macAddress", help="New MAC address")
    (options, arguments) = parser.parse_args()
    # validate if user entered interface and new mac address
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info")
    elif not options.new_macAddress:
        parser.error("Please specify a new MAC address, use --help for more info")
    return options

def change_mac_address(interface, new_macAddress):
    print("[+] Changing MAC address for " + interface + " to " + new_macAddress)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_macAddress])
    subprocess.call(["ifconfig", interface, "up"])

#run the function
options = get_arguments()
change_mac_address(options.interface, options.new_macAddress)

