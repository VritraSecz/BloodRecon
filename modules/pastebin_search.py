#!/usr/bin/env python3
"""
Pastebin Dump Search Module
Search for leaked data in Pastebin and similar services
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import requests
import json
import re
from datetime import datetime
from colorama import Fore, Style
import time

def search_pastebin(query):
    """Search for data in Pastebin and similar services"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                    {Fore.YELLOW}PASTEBIN DUMP SEARCH{Fore.CYAN}                      ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[+] Searching for: {Fore.YELLOW}{query}{Style.RESET_ALL}")
        
        # Search multiple paste services
        search_google_for_pastes(query)
        search_paste_sites_directly(query)
        provide_manual_search_links(query)
        
        # Security recommendations
        print(f"\n{Fore.GREEN}[+] Security Recommendations:{Style.RESET_ALL}")
        print(f"    {Fore.RED}• If sensitive data is found, take immediate action{Style.RESET_ALL}")
        print(f"    {Fore.RED}• Change passwords and API keys immediately{Style.RESET_ALL}")
        print(f"    {Fore.RED}• Contact the paste service to request removal{Style.RESET_ALL}")
        print(f"    {Fore.YELLOW}• Monitor for future data exposures{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Implement better data protection practices{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Unexpected error in Pastebin search: {str(e)}{Style.RESET_ALL}")

def search_google_for_pastes(query):
    """Use Google search to find pastes"""
    try:
        print(f"\n{Fore.GREEN}[+] Google Search Results:{Style.RESET_ALL}")
        
        # Generate search URLs for different paste services
        paste_sites = [
            "pastebin.com",
            "paste.ee",
            "hastebin.com",
            "ghostbin.com",
            "justpaste.it",
            "dpaste.org",
            "paste.org",
            "rentry.co"
        ]
        
        for site in paste_sites:
            search_url = f"https://www.google.com/search?q=site:{site} \"{query}\""
            print(f"    🔗 {site}: {Fore.MAGENTA}{search_url}{Style.RESET_ALL}")
        
        # Additional search patterns
        print(f"\n{Fore.GREEN}[+] Advanced Search Patterns:{Style.RESET_ALL}")
        advanced_patterns = [
            f"site:pastebin.com \"{query}\" \"password\"",
            f"site:pastebin.com \"{query}\" \"email\"",
            f"site:pastebin.com \"{query}\" \"database\"",
            f"site:pastebin.com \"{query}\" \"dump\"",
            f"site:pastebin.com \"{query}\" \"leak\""
        ]
        
        for pattern in advanced_patterns:
            encoded_pattern = requests.utils.quote(pattern)
            search_url = f"https://www.google.com/search?q={encoded_pattern}"
            print(f"    🔗 {Fore.CYAN}{pattern}{Style.RESET_ALL}")
            print(f"      URL: {Fore.MAGENTA}{search_url}{Style.RESET_ALL}")
            print()
            
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Error generating search URLs: {str(e)}{Style.RESET_ALL}")

def search_paste_sites_directly(query):
    """Attempt direct search on paste services"""
    try:
        print(f"\n{Fore.GREEN}[+] Direct Service Search:{Style.RESET_ALL}")
        
        # Note: Most paste services don't provide public search APIs
        # This section provides guidance for manual searching
        
        paste_services = {
            "Pastebin.com": {
                "url": "https://pastebin.com/search",
                "note": "Requires account for search",
                "manual_url": f"https://pastebin.com/search?q={requests.utils.quote(query)}"
            },
            "Paste.ee": {
                "url": "https://paste.ee/",
                "note": "No public search available",
                "manual_url": None
            },
            "Ghostbin.com": {
                "url": "https://ghostbin.com/",
                "note": "No public search available", 
                "manual_url": None
            },
            "JustPaste.it": {
                "url": "https://justpaste.it/",
                "note": "No public search available",
                "manual_url": None
            }
        }
        
        for service, info in paste_services.items():
            print(f"    {Fore.CYAN}{service}:{Style.RESET_ALL}")
            print(f"      Status: {Fore.YELLOW}{info['note']}{Style.RESET_ALL}")
            if info['manual_url']:
                print(f"      Search: {Fore.MAGENTA}{info['manual_url']}{Style.RESET_ALL}")
            print()
        
        # Simulate potential findings (educational)
        simulate_paste_findings(query)
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Error in direct search: {str(e)}{Style.RESET_ALL}")

def simulate_paste_findings(query):
    """Simulate potential paste findings for demonstration"""
    try:
        print(f"\n{Fore.GREEN}[+] Simulated Findings (Demo):{Style.RESET_ALL}")
        
        # Check if query looks like sensitive data
        sensitive_patterns = {
            'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'domain': r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'api_key': r'[A-Za-z0-9]{20,}',
            'password': r'password|pass|pwd'
        }
        
        # Generate realistic simulated findings
        import random
        if random.random() < 0.3:  # 30% chance of simulated findings
            findings = [
                {
                    'service': 'pastebin.com',
                    'title': f'Database dump containing {query}',
                    'url': f'https://pastebin.com/sim{random.randint(1000,9999)}',
                    'date': '2024-01-15',
                    'risk': 'HIGH'
                },
                {
                    'service': 'paste.ee',
                    'title': f'Configuration file with {query}',
                    'url': f'https://paste.ee/p/sim{random.randint(100,999)}',
                    'date': '2024-02-03',
                    'risk': 'MEDIUM'
                }
            ]
            
            print(f"    {Fore.RED}⚠️  POTENTIAL EXPOSURES FOUND (Simulated):{Style.RESET_ALL}")
            for finding in findings:
                print(f"\n    {Fore.RED}[{finding['risk']}]{Style.RESET_ALL} {finding['service']}")
                print(f"      Title: {Fore.YELLOW}{finding['title']}{Style.RESET_ALL}")
                print(f"      URL: {Fore.MAGENTA}{finding['url']}{Style.RESET_ALL}")
                print(f"      Date: {Fore.CYAN}{finding['date']}{Style.RESET_ALL}")
        else:
            print(f"    {Fore.GREEN}✓ No exposures found in simulation{Style.RESET_ALL}")
            print(f"    {Fore.YELLOW}Note: This is a simulated result for demonstration{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Error in simulation: {str(e)}{Style.RESET_ALL}")

def provide_manual_search_links(query):
    """Provide manual search links and tools"""
    try:
        print(f"\n{Fore.GREEN}[+] Manual Search Tools:{Style.RESET_ALL}")
        
        # Third-party search engines
        search_engines = {
            "IntelX.io": f"https://intelx.io/?s={requests.utils.quote(query)}",
            "Dehashed.com": f"https://dehashed.com/search?query={requests.utils.quote(query)}",
            "LeakCheck.io": f"https://leakcheck.io/",
            "HaveIBeenPwned": "https://haveibeenpwned.com/",
            "Snusbase": "https://snusbase.com/"
        }
        
        for tool, url in search_engines.items():
            print(f"    🔗 {tool}: {Fore.MAGENTA}{url}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[+] Specialized Search Commands:{Style.RESET_ALL}")
        
        # GitHub searches
        github_searches = [
            f"site:github.com \"{query}\" password",
            f"site:github.com \"{query}\" \"api_key\"",
            f"site:github.com \"{query}\" \"secret\"",
            f"site:github.com \"{query}\" \"token\""
        ]
        
        for search in github_searches:
            encoded_search = requests.utils.quote(search)
            url = f"https://www.google.com/search?q={encoded_search}"
            print(f"    🔗 {search}")
            print(f"      {Fore.MAGENTA}{url}{Style.RESET_ALL}")
            print()
        
        # Social media searches
        print(f"\n{Fore.GREEN}[+] Social Media Monitoring:{Style.RESET_ALL}")
        social_platforms = {
            "Twitter": f"https://twitter.com/search?q={requests.utils.quote(query)}",
            "Reddit": f"https://www.reddit.com/search/?q={requests.utils.quote(query)}",
            "Discord": "https://discord.com/ (Manual search required)"
        }
        
        for platform, url in social_platforms.items():
            print(f"    🔗 {platform}: {Fore.MAGENTA}{url}{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Error providing manual links: {str(e)}{Style.RESET_ALL}")

def analyze_paste_content(content):
    """Analyze paste content for sensitive information"""
    try:
        print(f"\n{Fore.GREEN}[+] Content Analysis:{Style.RESET_ALL}")
        
        patterns = {
            'emails': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'passwords': r'password[:\s=]+[^\s\n]+',
            'api_keys': r'api[_\s]*key[:\s=]+[A-Za-z0-9]+',
            'phone_numbers': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            'credit_cards': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
            'ip_addresses': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        }
        
        findings = {}
        for pattern_name, pattern in patterns.items():
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                findings[pattern_name] = len(matches)
        
        if findings:
            print(f"    {Fore.RED}⚠️  SENSITIVE DATA DETECTED:{Style.RESET_ALL}")
            for data_type, count in findings.items():
                print(f"      {data_type}: {Fore.YELLOW}{count} matches{Style.RESET_ALL}")
        else:
            print(f"    {Fore.GREEN}✓ No obvious sensitive patterns detected{Style.RESET_ALL}")
            
        return findings
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Error analyzing content: {str(e)}{Style.RESET_ALL}")
        return {}
