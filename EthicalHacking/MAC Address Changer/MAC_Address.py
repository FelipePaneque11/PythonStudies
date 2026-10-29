#!/usr/bin/evn python
#MAC Address is used to identify hardware within the network

#Why change the MAC(Media access control) Address?
#1-Increase anonymity
#2-Impersonate other devices
#3-Bypass filters

## LINUX MAC address change command
#sudo ifconfig eth0(network) down - disable network first
#sudo ifconfig eth0 hw ether 00:11:22:33:44:55 - change mac address
#sudo ifconfig eth0 up - enable network

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address", required=True)
    parser.add_argument("-m", "--mac", dest="new_macAddress", help="New MAC address", required=True)
    options = parser.parse_args()
    return options

def change_mac_address(interface, new_macAddress):
    print("[+] Changing MAC address for " + interface + " to " + new_macAddress)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_macAddress])
    subprocess.call(["ifconfig", "eth0", "up"])

def get_current_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return "[!] Could not find MAC address"


options = get_arguments()
#capturing current mac address
current_mac = get_current_mac_address(options.interface)
print("[+] Current MAC address: " + str(current_mac))
#changing mac address
change_mac_address(options.interface, options.new_macAddress)
#validating if mac address was changed
current_mac = get_current_mac_address(options.interface)
if current_mac == options.new_macAddress:
    print("[+] MAC Address was successfully changed to " + current_mac)
else:
    print("[!] Could not change MAC address to " + current_mac)
