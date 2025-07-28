#!/usr/bin/env python3
"""
Google Drive Leak Finder
Search for publicly accessible Google Drive links with exposed data
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import requests
from urllib.parse import quote
from colorama import Fore, Style
import time

def search_google_drive_leaks(query):
    """Search for publicly accessible Google Drive links containing the query"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                  {Fore.YELLOW}GOOGLE DRIVE LEAK FINDER{Fore.CYAN}                    ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[+] Searching for Google Drive leaks with query: {Fore.YELLOW}{query}{Style.RESET_ALL}")
        
        # Construct Google search URL for Drive
        encoded_query = quote(query)
        google_search_url = f"https://www.google.com/search?q=site:drive.google.com " + encoded_query
        
        print(f"\n{Fore.GREEN}[+] Google Search Link:{Style.RESET_ALL}")
        print(f"    🔗 {Fore.MAGENTA}{google_search_url}{Style.RESET_ALL}")
        
        # Use proper Google search for public drive files
        search_public_drive_files(query)
        
        # Security recommendations
        print(f"\n{Fore.GREEN}[+] Security Recommendations:{Style.RESET_ALL}")
        print(f"    {Fore.RED}• If sensitive data is found, immediately secure the document{Style.RESET_ALL}")
        print(f"    {Fore.RED}• Review permissions and sharing settings regularly{Style.RESET_ALL}")
        print(f"    {Fore.RED}• Educate users on secure sharing practices{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[ERROR] Unexpected error in Google Drive search: {str(e)}{Style.RESET_ALL}")

def search_public_drive_files(query):
    """Search for publicly accessible Google Drive files"""
    try:
        print(f"\n{Fore.GREEN}[+] Manual Search Required:{Style.RESET_ALL}")
        
        # Provide search dorks for manual searching
        search_dorks = [
            f'site:drive.google.com "{query}"',
            f'site:drive.google.com intitle:"{query}"',
            f'site:drive.google.com filetype:pdf "{query}"',
            f'site:drive.google.com filetype:doc "{query}"',
            f'site:drive.google.com filetype:xls "{query}"',
            f'site:drive.google.com "sharing" "{query}"',
            f'site:docs.google.com "{query}"',
            f'site:sheets.google.com "{query}"'
        ]
        
        print(f"    {Fore.YELLOW}Use these Google search dorks manually:{Style.RESET_ALL}")
        for i, dork in enumerate(search_dorks, 1):
            print(f"    {Fore.CYAN}[{i}] {dork}{Style.RESET_ALL}")
        
        # Alternative search methods
        print(f"\n{Fore.GREEN}[+] Alternative Search Methods:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Use DuckDuckGo: !g {search_dorks[0]}{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Use Bing: site:drive.google.com {query}{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Use Yandex for different results{Style.RESET_ALL}")
        
        # Common indicators of leaked files
        print(f"\n{Fore.GREEN}[+] Look for These Indicators:{Style.RESET_ALL}")
        print(f"    {Fore.RED}• Files with 'confidential' or 'internal' in title{Style.RESET_ALL}")
        print(f"    {Fore.RED}• Spreadsheets with employee or customer data{Style.RESET_ALL}")
        print(f"    {Fore.RED}• Documents with passwords or API keys{Style.RESET_ALL}")
        print(f"    {Fore.RED}• Financial reports or sensitive business data{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Error in Google Drive search: {str(e)}{Style.RESET_ALL}")

def simulate_drive_leak_findings(query):
    """Simulate potential Google Drive leak findings for demonstration"""
    try:
        print(f"\n{Fore.GREEN}[+] Simulated Findings (Demo):{Style.RESET_ALL}")
        
        import random
        if random.random() < 0.3:  # 30% chance of simulated findings
            simulated_links = [
                {
                    'title': f'HR Report {query} 2024',
                    'url': f'https://drive.google.com/simulated/doc{random.randint(1000,9999)}',
                    'risk': 'HIGH'
                },
                {
                    'title': f'{query} Financial Presentation',
                    'url': f'https://drive.google.com/simulated/presentation{random.randint(100,999)}',
                    'risk': 'MEDIUM'
                }
            ]
            
            print(f"    {Fore.RED}⚠️  POTENTIAL LEAKS FOUND (Simulated):{Style.RESET_ALL}")
            for leak in simulated_links:
                print(f"\n    {Fore.RED}[{leak['risk']}]{Style.RESET_ALL} Title: {Fore.YELLOW}{leak['title']}{Style.RESET_ALL}")
                print(f"      URL: {Fore.MAGENTA}{leak['url']}{Style.RESET_ALL}")
        else:
            print(f"    {Fore.GREEN}✓ No leaks found in simulation{Style.RESET_ALL}")
            print(f"    {Fore.YELLOW}Note: This is a simulated result for demonstration{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Error in simulation: {str(e)}{Style.RESET_ALL}")
