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

# SYN ACK Scan
def syn_ack_scan():
    print("\nNmap Version: ", scanner.nmap_version())
    message = "Carrying out SYN ACK scan on IP address " + ip_addr
    if resp == '1':
        print(message, "(common ports only)")
        scanner.scan(ip_addr, '0-1023', '-v -sS')
    else:
        print(message, "(all ports)")
        scanner.scan(ip_addr, '0-65535', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status:", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports:", scanner[ip_addr]['tcp'].keys())

# welcome message
print("\nWelcome, this is a simple nmap automation tool")
print("==============================================\n")

# get the IP address
ip_addr = input("Please enter the IP address you want to scan: ")

if validateIP(ip_addr):
    resp = input("""\nPlease enter the type of scan you want to run
        1) SYN ACK Scan - common ports
        2) SYN ACK Scan - all ports
        3) UDP Scan
        5) Comprehensive Scan\n
        Your choice: """)
    
    if resp == '1' or resp == '2':
        syn_ack_scan()
    elif resp == '2':
        print("To be written")
    else:
        print("To be written")


else:
    #we didn't get a valid IP address, exit
    print("\nIP address invalid\n")




