#!/usr/bin/env python3
"""
WHOIS Domain Lookup Module
Provides comprehensive WHOIS information for domains
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import whois
import requests
from colorama import Fore, Style
from datetime import datetime

def get_whois_info(domain):
    """Get comprehensive WHOIS information for a domain"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                     {Fore.YELLOW}WHOIS DOMAIN LOOKUP{Fore.CYAN}                      ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        # Clean domain input
        domain = domain.lower().strip()
        if domain.startswith('http://') or domain.startswith('https://'):
            domain = domain.split('//')[1].split('/')[0]
        
        try:
            # Get WHOIS information
            w = whois.whois(domain)
            
            print(f"\n{Fore.GREEN}[+] Domain Information:{Style.RESET_ALL}")
            print(f"    Domain: {Fore.YELLOW}{domain}{Style.RESET_ALL}")
            
            # Domain registrar info
            if w.registrar:
                print(f"    Registrar: {Fore.CYAN}{w.registrar}{Style.RESET_ALL}")
            
            # Registration dates
            if w.creation_date:
                if isinstance(w.creation_date, list):
                    creation = w.creation_date[0]
                else:
                    creation = w.creation_date
                print(f"    Created: {Fore.YELLOW}{creation.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
            
            if w.expiration_date:
                if isinstance(w.expiration_date, list):
                    expiration = w.expiration_date[0]
                else:
                    expiration = w.expiration_date
                print(f"    Expires: {Fore.YELLOW}{expiration.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
                
                # Check if domain is expiring soon
                days_until_expiry = (expiration - datetime.now()).days
                if days_until_expiry < 30:
                    print(f"    Status: {Fore.RED}Expiring in {days_until_expiry} days!{Style.RESET_ALL}")
                else:
                    print(f"    Status: {Fore.GREEN}Active ({days_until_expiry} days remaining){Style.RESET_ALL}")
            
            if w.updated_date:
                if isinstance(w.updated_date, list):
                    updated = w.updated_date[0]
                else:
                    updated = w.updated_date
                print(f"    Updated: {Fore.YELLOW}{updated.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
            
            # Name servers
            if w.name_servers:
                print(f"\n{Fore.GREEN}[+] Name Servers:{Style.RESET_ALL}")
                for ns in w.name_servers:
                    print(f"    {Fore.CYAN}{ns.lower()}{Style.RESET_ALL}")
            
            # Contact information
            print(f"\n{Fore.GREEN}[+] Contact Information:{Style.RESET_ALL}")
            
            # Registrant info
            if w.name:
                print(f"    Registrant: {Fore.YELLOW}{w.name}{Style.RESET_ALL}")
            if w.org:
                print(f"    Organization: {Fore.YELLOW}{w.org}{Style.RESET_ALL}")
            if w.emails:
                if isinstance(w.emails, list):
                    for email in w.emails:
                        print(f"    Email: {Fore.CYAN}{email}{Style.RESET_ALL}")
                else:
                    print(f"    Email: {Fore.CYAN}{w.emails}{Style.RESET_ALL}")
            
            # Address information
            if w.address:
                print(f"    Address: {Fore.CYAN}{w.address}{Style.RESET_ALL}")
            if w.city:
                print(f"    City: {Fore.CYAN}{w.city}{Style.RESET_ALL}")
            if w.state:
                print(f"    State: {Fore.CYAN}{w.state}{Style.RESET_ALL}")
            if w.zipcode:
                print(f"    ZIP: {Fore.CYAN}{w.zipcode}{Style.RESET_ALL}")
            if w.country:
                print(f"    Country: {Fore.CYAN}{w.country}{Style.RESET_ALL}")
            
            # Domain status
            if w.status:
                print(f"\n{Fore.GREEN}[+] Domain Status:{Style.RESET_ALL}")
                if isinstance(w.status, list):
                    for status in w.status:
                        print(f"    {Fore.MAGENTA}{status}{Style.RESET_ALL}")
                else:
                    print(f"    {Fore.MAGENTA}{w.status}{Style.RESET_ALL}")
                    
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Could not retrieve WHOIS information: {str(e)}{Style.RESET_ALL}")
            
            # Try alternative WHOIS API
            try:
                response = requests.get(f"https://www.whoisxmlapi.com/whoisserver/WhoisService?domainName={domain}&outputFormat=JSON", timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if 'WhoisRecord' in data:
                        record = data['WhoisRecord']
                        print(f"\n{Fore.GREEN}[+] Alternative WHOIS Data:{Style.RESET_ALL}")
                        if 'domainName' in record:
                            print(f"    Domain: {Fore.YELLOW}{record['domainName']}{Style.RESET_ALL}")
                        if 'registrarName' in record:
                            print(f"    Registrar: {Fore.CYAN}{record['registrarName']}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[ERROR] Alternative WHOIS lookup also failed{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}[ERROR] All WHOIS lookup methods failed{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Unexpected error in WHOIS lookup: {str(e)}{Style.RESET_ALL}")
