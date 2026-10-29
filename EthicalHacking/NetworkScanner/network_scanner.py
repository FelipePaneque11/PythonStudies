#discover all devices on the network
#display their IP Address
#Display their MAC Address
import scapy.all as scapy
import argparse

#ARP protocol - asks every device connected to the network for its mac address

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ip",dest="ip",help="IP address")
    options = parser.parse_args()
    return options

def scan(ip):
    #asks "Who has this IP?"
    arp_request = scapy.ARP(pdst=ip)
    #Builds the ethernet frame.
    # "ff:ff:ff:ff:ff:ff" delivers to every device on the local network
    # we need this because we dont know anyone's mac address yet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #in scapy, / stack layers. This wraps the ARP request inside the broadcast Ethernet frame
    arp_request_broadcast = broadcast/arp_request
    #scapy will return 2 lists(answered and unanswered) - [0] gets only the answered list
    #srp - send and received packets. It send my packets, wait for 1 second for replies.
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[0].pdst, "MAC":element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC ADDRESS\n---------------------------------------------------------")
    for element in results_list:
        print(element["ip"] + "\t\t" + element["MAC"])

options = get_arguments()
#your network ip address
#/24 asks all 256 possible IP addresses in the network
scan_result = scan(options.ip) #192.168.0.0/24
print_result(scan_result)

