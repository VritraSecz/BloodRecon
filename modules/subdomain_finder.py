#!/usr/bin/env python3
"""
Subdomain Finder Module
Discover subdomains using various techniques
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import requests
import dns.resolver
import time
from colorama import Fore, Style

def find_subdomains(domain):
    """Find subdomains for a domain"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                    {Fore.YELLOW}SUBDOMAIN DISCOVERY{Fore.CYAN}                       ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        domain = domain.lower().strip()
        if domain.startswith(('http://', 'https://')):
            domain = domain.split('//')[1].split('/')[0]
        
        print(f"\n{Fore.GREEN}[+] Subdomain Discovery:{Style.RESET_ALL}")
        print(f"    Target Domain: {Fore.YELLOW}{domain}{Style.RESET_ALL}")
        
        # Common subdomain prefixes
        common_subdomains = [
            'www', 'mail', 'ftp', 'admin', 'test', 'dev', 'staging', 'api',
            'blog', 'shop', 'store', 'secure', 'vpn', 'remote', 'support',
            'help', 'docs', 'cdn', 'assets', 'img', 'images', 'static',
            'beta', 'demo', 'portal', 'wiki', 'forum', 'news', 'mobile',
            'm', 'app', 'apps', 'db', 'database', 'sql', 'mysql', 'backup'
        ]
        
        found_subdomains = []
        
        print(f"\n{Fore.GREEN}[+] Testing Common Subdomains:{Style.RESET_ALL}")
        
        for subdomain in common_subdomains:
            full_domain = f"{subdomain}.{domain}"
            time.sleep(0.1)  # Rate limiting
            try:
                # Try DNS resolution
                answers = dns.resolver.resolve(full_domain, 'A')
                for answer in answers:
                    ip_str = str(answer)
                    if not is_private_ip_address(ip_str):  # Ensure it's not private IP
                        print(f"    {Fore.GREEN}✓ {full_domain}{Style.RESET_ALL} -> {Fore.CYAN}{answer}{Style.RESET_ALL}")
                        found_subdomains.append((full_domain, str(answer)))
                        break
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except Exception:
                pass
        
        # Expand wordlist for deeper scanning
        print(f"\n{Fore.GREEN}[+] Extended Subdomain Wordlist:{Style.RESET_ALL}")
        extended_subdomains = [
            'staging', 'prod', 'production', 'dev', 'development', 'qa', 'testing',
            'sandbox', 'demo2', 'beta2', 'alpha', 'preview', 'temp', 'old',
            'new', 'v1', 'v2', 'api-v1', 'api-v2', 'webmail', 'mail2', 'smtp',
            'imap', 'pop', 'ns1', 'ns2', 'dns1', 'dns2', 'mx1', 'mx2'
        ]
        
        for subdomain in extended_subdomains:
            full_domain = f"{subdomain}.{domain}"
            time.sleep(0.05)  # Faster rate limiting for extended scan
            try:
                answers = dns.resolver.resolve(full_domain, 'A')
                for answer in answers:
                    ip_str = str(answer)
                    if not is_private_ip_address(ip_str):
                        print(f"    {Fore.GREEN}✓ {full_domain}{Style.RESET_ALL} -> {Fore.CYAN}{answer}{Style.RESET_ALL}")
                        found_subdomains.append((full_domain, str(answer)))
                        break
            except:
                pass
        
        # Try certificate transparency logs (simulated)
        print(f"\n{Fore.GREEN}[+] Certificate Transparency Logs:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}Manual check recommended:{Style.RESET_ALL}")
        print(f"    crt.sh: {Fore.MAGENTA}https://crt.sh/?q={domain}{Style.RESET_ALL}")
        print(f"    censys.io: {Fore.MAGENTA}https://censys.io/certificates?q={domain}{Style.RESET_ALL}")
        
        # Try DNS enumeration with wildcards
        print(f"\n{Fore.GREEN}[+] Wildcard Test:{Style.RESET_ALL}")
        try:
            wildcard_test = f"nonexistent-{domain.replace('.', '-')}.{domain}"
            dns.resolver.resolve(wildcard_test, 'A')
            print(f"    {Fore.YELLOW}⚠️  Wildcard DNS detected - results may include false positives{Style.RESET_ALL}")
        except:
            print(f"    {Fore.GREEN}✓ No wildcard DNS detected{Style.RESET_ALL}")
        
        # Results summary
        if found_subdomains:
            print(f"\n{Fore.GREEN}[+] Discovery Summary:{Style.RESET_ALL}")
            print(f"    Found Subdomains: {Fore.YELLOW}{len(found_subdomains)}{Style.RESET_ALL}")
            
            print(f"\n{Fore.GREEN}[+] All Discovered Subdomains:{Style.RESET_ALL}")
            for subdomain, ip in found_subdomains:
                print(f"    {Fore.CYAN}{subdomain:<30} {Fore.YELLOW}{ip}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}[!] No subdomains found using common prefixes{Style.RESET_ALL}")
        
        # Additional tools suggestions
        print(f"\n{Fore.GREEN}[+] Advanced Tools:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Use subfinder, amass, or sublist3r for comprehensive scanning{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Check DNS brute force tools like dnsrecon{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Monitor passive DNS databases{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Unexpected error in subdomain discovery: {str(e)}{Style.RESET_ALL}")

def is_private_ip_address(ip):
    """Check if IP address is private/internal"""
    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        
        first = int(parts[0])
        second = int(parts[1])
        
        # Private IP ranges
        # 10.0.0.0/8
        if first == 10:
            return True
        # 172.16.0.0/12
        elif first == 172 and 16 <= second <= 31:
            return True
        # 192.168.0.0/16
        elif first == 192 and second == 168:
            return True
        # 127.0.0.0/8 (loopback)
        elif first == 127:
            return True
        
        return False
    except:
        return False
