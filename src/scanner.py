#!/usr/bin/env python3

import nmap
import re

# create a scanner object
scanner = nmap.PortScanner()

# define the regex for a valid IP address (IPv4)
regexIP = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

# function to validate a string IP
def validateIP(strIP): 
    if(re.search(regexIP, strIP)):
        return True
    else: 
        return False

# generic scan (called by detailed scans)
def generic_scan(scan_str, scan_flags):
    # message to confirm scan is starting
    print("\nnmap version: %d.%d" % (scanner.nmap_version()))
    message = "Carrying out " + scan_str + " scan on IP address " + ip_addr
    if int(resp) % 2 == 1:
        print(message, "(common ports only)")
        scanner.scan(ip_addr, '0-1023', scan_flags)
    else:
        print(message, "(all ports)")
        scanner.scan(ip_addr, '0-65535', scan_flags)
    
    # scaninfo() probably not being used, leave in for now "in case"
    # print(scanner.scaninfo())

    # report the state
    ip_state = scanner[ip_addr].state()
    print("\nIP Status: %s" % ip_state.title() )

    # if IP address is up ...
    if  ip_state == "up":
        protocols = scanner[ip_addr].all_protocols()
        # print(scanner[ip_addr].all_protocols())

        # for each protocol that has been checked, print the list of open ports
        for protocol in protocols:
            print("Open Ports (%s):" % protocol.upper(), scanner[ip_addr][protocol].keys(), "\n")

# SYN ACK Scan - convenience method
def syn_ack_scan():
    scan_str = "SYN ACK"
    scan_flags = "-v -sS"
    generic_scan(scan_str, scan_flags)

# welcome message
print("\nWelcome, this is a simple nmap automation tool")
print("==============================================\n")

# get the IP address
ip_addr = input("Please enter the IP address you want to scan: ")

# if valid, check for scan type
if validateIP(ip_addr):
    resp = input("""\nPlease enter the type of scan you want to run
    1) SYN ACK Scan - common ports
    2) SYN ACK Scan - all ports
    3) UDP Scan - common ports
    4) UDP Scan - all ports
    5) Comprehensive Scan - common ports
    6) Comprehensive Scan - all ports\n
    Your choice: """)
    
    if resp == '1' or resp == '2':
        syn_ack_scan()
    elif resp == '3' or resp == '4':
        print("\nTo be written\n")
    elif resp == '5' or resp == '6':
        print("\nTo be written\n")
    else:
        print("\nInvalid choice\n")

else:
    #we didn't get a valid IP address, exit
    print("\nIP address invalid\n")




