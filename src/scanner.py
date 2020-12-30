#!/usr/bin/env python3

import nmap

# create a scanner object
scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("==============================================")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is:", ip_addr)