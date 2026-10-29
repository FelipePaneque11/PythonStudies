#discover all devices on the network
#display their IP Address
#Display their MAC Address
import scapy.all as scapy

#ARP protocol - asks every device connected to the network for its mac address


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

    print("IP\t\t\tMAC ADDRESS\n---------------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc+ "\t\t" + element[1].hwsrc)

#your network ip address
#/24 asks all 256 possible IP addresses in the network
scan("192.168.0.0/24")
