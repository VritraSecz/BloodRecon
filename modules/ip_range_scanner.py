#!/usr/bin/env python3
"""
IP Range Scanner Module
Perform a simple scan across a range of IP addresses to find active hosts.
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import subprocess
from colorama import Fore, Style
import ipaddress

def scan_ip_range(ip_range):
    """Scan a range of IP addresses and display live hosts"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                      {Fore.YELLOW}IP RANGE SCANNER{Fore.CYAN}                        ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[+] Scanning IP Range: {Fore.YELLOW}{ip_range}{Style.RESET_ALL}")
        
        # Parse the IP range
        network = ipaddress.ip_network(ip_range, strict=False)
        active_hosts = []
        
        for ip in network:
            result = subprocess.run(["ping", "-c", "1", "-W", "1", str(ip)], 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                active_hosts.append(str(ip))
                print(f"    {Fore.GREEN}✓ Active: {str(ip)}{Style.RESET_ALL}")
            else:
                print(f"    {Fore.RED}✗ Inactive: {str(ip)}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[+] Scan Complete. Active Hosts: {len(active_hosts)}{Style.RESET_ALL}")
        for host in active_hosts:
            print(f"    {Fore.CYAN}{host}{Style.RESET_ALL}")
        
        if len(active_hosts) == 0:
            print(f"    {Fore.YELLOW}No active hosts found{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Unexpected error in IP range scan: {str(e)}{Style.RESET_ALL}")

