#!/usr/bin/env python3
"""
Social Media Username Checker
Check username availability across social platforms
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import requests
from colorama import Fore, Style

def check_username(username):
    """Check username across social media platforms"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                   {Fore.YELLOW}SOCIAL MEDIA CHECKER{Fore.CYAN}                       ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[+] Username Analysis:{Style.RESET_ALL}")
        print(f"    Username: {Fore.YELLOW}{username}{Style.RESET_ALL}")
        
        # Social media platforms to check
        platforms = {
            'GitHub': f'https://github.com/{username}',
            'Twitter/X': f'https://x.com/{username}',
            'Instagram': f'https://www.instagram.com/{username}',
            'Reddit': f'https://www.reddit.com/user/{username}',
            'LinkedIn': f'https://www.linkedin.com/in/{username}',
            'YouTube': f'https://www.youtube.com/@{username}',
            'Facebook': f'https://www.facebook.com/{username}',
            'TikTok': f'https://www.tiktok.com/@{username}',
            'Pinterest': f'https://www.pinterest.com/{username}',
            'Medium': f'https://medium.com/@{username}',
            'Telegram': f'https://t.me/{username}',
            'Discord': f'https://discord.com/users/{username}'
        }
        
        print(f"\n{Fore.GREEN}[+] Platform Availability:{Style.RESET_ALL}")
        
        for platform, url in platforms.items():
            try:
                response = requests.get(url, timeout=10, allow_redirects=True)
                
                if response.status_code == 200:
                    # Check if it's a real profile or redirect/error page
                    if platform == 'GitHub' and 'Not Found' in response.text:
                        status = f"{Fore.GREEN}Available{Style.RESET_ALL}"
                    elif platform == 'Twitter' and 'This account doesn' in response.text:
                        status = f"{Fore.GREEN}Available{Style.RESET_ALL}"
                    elif platform == 'Instagram' and 'Sorry, this page' in response.text:
                        status = f"{Fore.GREEN}Available{Style.RESET_ALL}"
                    elif platform == 'Reddit' and 'page not found' in response.text.lower():
                        status = f"{Fore.GREEN}Available{Style.RESET_ALL}"
                    else:
                        status = f"{Fore.RED}Taken{Style.RESET_ALL}"
                elif response.status_code == 404:
                    status = f"{Fore.GREEN}Available{Style.RESET_ALL}"
                else:
                    status = f"{Fore.YELLOW}Unknown ({response.status_code}){Style.RESET_ALL}"
                
                print(f"    {platform:12} - {status} - {Fore.CYAN}{url}{Style.RESET_ALL}")
                
            except requests.RequestException:
                print(f"    {platform:12} - {Fore.YELLOW}Timeout{Style.RESET_ALL} - {Fore.CYAN}{url}{Style.RESET_ALL}")
        
        # Additional checks
        print(f"\n{Fore.GREEN}[+] Additional Resources:{Style.RESET_ALL}")
        print(f"    Namechk: {Fore.MAGENTA}https://namechk.com/{username}{Style.RESET_ALL}")
        print(f"    KnowEm: {Fore.MAGENTA}https://knowem.com/checkusernames.php?u={username}{Style.RESET_ALL}")
        print(f"    UserSearch: {Fore.MAGENTA}https://usersearch.org/user/{username}{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Unexpected error in social media check: {str(e)}{Style.RESET_ALL}")
