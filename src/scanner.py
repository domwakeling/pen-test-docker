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
    if int(resp) % 3 == 1:
        print(message, "(common ports only)")
        scanner.scan(ip_addr, '0-1023', scan_flags)
    elif int(resp) % 3 == 2:
        print(message, "(all ports)")
        scanner.scan(ip_addr, '0-65535', scan_flags)
    else:
        print(message, "(custom ports, %s-%s)" % (port_low, port_high))
        scanner.scan(ip_addr, f"{port_low}-{port_high}", scan_flags)
    
    # functions to see what information is available when you try ...
    # print("\nscanner.scaninfo() generates:")
    # print(scanner.scaninfo())
    # print("\nscanner.scanstats() generates:")
    # print(scanner.scanstats())
    # print("\nscanner[ip_addr] generates:")
    # print(scanner[ip_addr])

    # report the state
    ip_state = scanner[ip_addr].state()    
    print("\nIP Status: %s" % ip_state.title() )

    # if IP address is up ...
    if  ip_state == "up":
        ip_report = scanner[ip_addr]

        # if comprehensive, attempt display the OS (won't work on a website)
        if int(resp) >= 7:
            try:
                print("OS: %s" % ip_report["osmatch"][0]["name"])
            except:
                print("Unable to determine OS")

        protocols = ip_report.all_protocols()
        # for each protocol that has been checked, print the list of open ports
        for protocol in protocols:
            print("\nOpen Ports (%s):" % protocol.upper())
            for port in ip_report[protocol]:
                # formatted string with protocol, port (5-space aligned) and name
                s = "  %s %d%s " % (protocol.upper(), port, " " * (5 - len(str(port))))
                s = s + ip_report[protocol][port]['name']
                # add the product info if we have it
                if ip_report[protocol][port]['product'] != "":
                    s = s + " (%s)" % ip_report[protocol][port]['product']
                print(s)
    
    print("\nScan complete in %s seconds\n" % scanner.scanstats()['elapsed'])

# SYN ACK Scan - convenience method
def syn_ack_scan():
    scan_str = "SYN ACK"
    scan_flags = "-v -sS"
    generic_scan(scan_str, scan_flags)

# UDP Scan - convenience method
def udp_scan():
    scan_str = "UDP"
    scan_flags = "-v -sU"
    generic_scan(scan_str, scan_flags)

# Comprehensive Scan - convenience method
def comp_scan():
    scan_str = "comprehensive"
    scan_flags = "-v -sS -sV -sC -A -O"
    generic_scan(scan_str, scan_flags)

# welcome message
print("\nPort Scanner : A simple nmap automation tool")
print("============================================\n")

# get the IP address
ip_addr = input("Please enter the IP address you want to scan: ")

# if valid, check for scan type
if validateIP(ip_addr):
    port_low = 0
    port_high = 0
    resp = input("""\nPlease enter the type of scan you want to run
    1) SYN ACK Scan - common ports
    2) SYN ACK Scan - all ports
    3) SYN ACK Scan - specify ports
    4) UDP Scan - common ports
    5) UDP Scan - all ports
    6) UDP Scan - specify ports
    7) Comprehensive Scan - common ports
    8) Comprehensive Scan - all ports
    9) Comprehensive Scan - specify ports\n
    Your choice: """)
    
    if resp == '1' or resp == '2':
        syn_ack_scan()
    elif resp == '4' or resp == '5':
        udp_scan()
    elif resp == '7' or resp == '8':
        comp_scan()
    elif resp == '3' or resp == '6' or resp == '9':
        port_low = input("Please enter the first port to scan: ")
        port_high = input("Please enter the last port to scan: ")
        if resp == '3':
            syn_ack_scan()
        elif resp == '6':
            udp_scan()
        else:
            comp_scan()
    else:
        print("\nInvalid choice\n")

else:
    #we didn't get a valid IP address, exit
    print("\nIP address invalid\n")




