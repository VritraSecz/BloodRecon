#!/usr/bin/env python3
"""
Wayback Machine Snapshot Finder
Locate historical snapshots of a URL from the Internet Archive
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import requests
from colorama import Fore, Style
from urllib.parse import quote

def search_wayback(url):
    """Search Internet Archive for wayback snapshots"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                  {Fore.YELLOW}WAYBACK MACHINE FINDER{Fore.CYAN}                      ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        # Ensure URL has proper format
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        # Query the Wayback Machine
        api_url = f"http://archive.org/wayback/available?url={quote(url)}"
        try:
            response = requests.get(api_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'archived_snapshots' in data and data['archived_snapshots']:
                    print(f"\n{Fore.GREEN}[+] Latest Snapshot:{Style.RESET_ALL}")
                    snapshot = data['archived_snapshots']['closest']
                    
                    if 'available' in snapshot and snapshot['available']:
                        print(f"    Snapshot URL: {Fore.YELLOW}{snapshot['url']}{Style.RESET_ALL}")
                        print(f"    Timestamp: {Fore.YELLOW}{snapshot['timestamp']}{Style.RESET_ALL}")
                        print(f"    Status: {Fore.GREEN}Available{Style.RESET_ALL}")
                    else:
                        print(f"    {Fore.RED}No available snapshot found.{Style.RESET_ALL}")
                else:
                    print(f"    {Fore.RED}No snapshots found for this URL.{Style.RESET_ALL}")
            else:
                print(f"    {Fore.RED}Failed to contact Wayback Machine.{Style.RESET_ALL}")
        except requests.RequestException as e:
            print(f"{Fore.RED}[ERROR] Network error while contacting Wayback Machine: {str(e)}{Style.RESET_ALL}")
            
        # Advanced search
        print(f"\n{Fore.GREEN}[+] Advanced Search:{Style.RESET_ALL}")
        timeline_url = f"http://web.archive.org/web/*/{quote(url)}"
        print(f"    Explore full timeline: {Fore.CYAN}{timeline_url}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[ERROR] Unexpected error in Wayback Machine search: {str(e)}{Style.RESET_ALL}")
