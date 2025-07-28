#!/usr/bin/env python3
"""
Common Crawl Data Search Module
Search and analyze data from Common Crawl archives
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import requests
import json
from datetime import datetime
from colorama import Fore, Style
from urllib.parse import urlparse

def search_common_crawl(domain):
    """Search Common Crawl data for domain information"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                  {Fore.YELLOW}COMMON CRAWL DATA SEARCH{Fore.CYAN}                    ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        # Clean domain input
        if domain.startswith(('http://', 'https://')):
            domain = urlparse(domain).netloc
        
        print(f"\n{Fore.GREEN}[+] Searching Common Crawl for: {Fore.YELLOW}{domain}{Style.RESET_ALL}")
        
        # Get available crawl indexes
        get_crawl_indexes()
        
        # Search for domain in Common Crawl
        search_domain_data(domain)
        
        # Get URL statistics
        get_url_statistics(domain)
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Unexpected error in Common Crawl search: {str(e)}{Style.RESET_ALL}")

def get_crawl_indexes():
    """Get available Common Crawl indexes"""
    try:
        print(f"\n{Fore.GREEN}[+] Available Common Crawl Indexes:{Style.RESET_ALL}")
        
        # Get list of available crawls
        url = "https://index.commoncrawl.org/collinfo.json"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            crawls = response.json()
            
            # Show recent crawls
            recent_crawls = crawls[:5]  # Show last 5 crawls
            
            for crawl in recent_crawls:
                crawl_id = crawl.get('id', 'Unknown')
                crawl_name = crawl.get('name', 'Unknown')
                
                print(f"    {Fore.CYAN}• {crawl_name} ({crawl_id}){Style.RESET_ALL}")
                
            print(f"    {Fore.YELLOW}Total Available Crawls: {len(crawls)}{Style.RESET_ALL}")
            
        else:
            print(f"    {Fore.RED}✗ Could not retrieve crawl indexes{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"    {Fore.RED}✗ Error retrieving crawl indexes: {str(e)}{Style.RESET_ALL}")

def search_domain_data(domain):
    """Search for domain data in Common Crawl"""
    try:
        print(f"\n{Fore.GREEN}[+] Domain Data Search:{Style.RESET_ALL}")
        
        # Use Common Crawl Index API (try multiple recent indexes)
        recent_indexes = [
            "CC-MAIN-2024-22",
            "CC-MAIN-2024-18",
            "CC-MAIN-2024-10"
        ]
        
        search_successful = False
        for index_name in recent_indexes:
            try:
                base_url = f"https://index.commoncrawl.org/{index_name}-index"
                search_url = f"{base_url}?url=*.{domain}&output=json&limit=100"
                print(f"    {Fore.CYAN}Trying index: {index_name}{Style.RESET_ALL}")
                break
            except:
                continue
        
        print(f"    {Fore.CYAN}Searching recent crawl data...{Style.RESET_ALL}")
        
        response = requests.get(search_url, timeout=15)
        
        if response.status_code == 200:
            lines = response.text.strip().split('\n')
            
            if lines and lines[0]:
                urls_found = []
                content_types = {}
                status_codes = {}
                
                for line in lines[:50]:  # Analyze first 50 results
                    try:
                        data = json.loads(line)
                        url = data.get('url', '')
                        status = data.get('status', '')
                        mime = data.get('mime', 'unknown')
                        timestamp = data.get('timestamp', '')
                        
                        urls_found.append({
                            'url': url,
                            'status': status,
                            'mime': mime,
                            'timestamp': timestamp
                        })
                        
                        # Count content types
                        content_types[mime] = content_types.get(mime, 0) + 1
                        
                        # Count status codes
                        status_codes[status] = status_codes.get(status, 0) + 1
                        
                    except json.JSONDecodeError:
                        continue
                
                print(f"    {Fore.GREEN}✓ Found {len(urls_found)} archived URLs{Style.RESET_ALL}")
                
                # Show content type distribution
                print(f"\n{Fore.GREEN}[+] Content Type Distribution:{Style.RESET_ALL}")
                for mime_type, count in sorted(content_types.items(), key=lambda x: x[1], reverse=True)[:10]:
                    print(f"    {Fore.CYAN}{mime_type}: {Fore.YELLOW}{count} files{Style.RESET_ALL}")
                
                # Show status code distribution
                print(f"\n{Fore.GREEN}[+] HTTP Status Distribution:{Style.RESET_ALL}")
                for status, count in sorted(status_codes.items(), key=lambda x: x[1], reverse=True):
                    color = Fore.GREEN if status == '200' else Fore.YELLOW if status.startswith('3') else Fore.RED
                    print(f"    {color}HTTP {status}: {count} responses{Style.RESET_ALL}")
                
                # Show sample URLs
                print(f"\n{Fore.GREEN}[+] Sample Archived URLs:{Style.RESET_ALL}")
                for i, url_data in enumerate(urls_found[:10]):
                    timestamp = url_data['timestamp']
                    if timestamp:
                        try:
                            # Convert timestamp to readable format
                            dt = datetime.strptime(timestamp, '%Y%m%d%H%M%S')
                            readable_time = dt.strftime('%Y-%m-%d %H:%M:%S')
                        except:
                            readable_time = timestamp
                    else:
                        readable_time = 'Unknown'
                    
                    print(f"    {Fore.CYAN}[{i+1:2d}] {url_data['url']}{Style.RESET_ALL}")
                    print(f"         {Fore.YELLOW}Status: {url_data['status']} | Type: {url_data['mime']} | Time: {readable_time}{Style.RESET_ALL}")
                
            else:
                print(f"    {Fore.YELLOW}No archived data found for {domain}{Style.RESET_ALL}")
                
        else:
            print(f"    {Fore.RED}✗ Search request failed (Status: {response.status_code}){Style.RESET_ALL}")
            
    except Exception as e:
        print(f"    {Fore.RED}✗ Error searching domain data: {str(e)}{Style.RESET_ALL}")

def get_url_statistics(domain):
    """Get URL statistics from Common Crawl"""
    try:
        print(f"\n{Fore.GREEN}[+] URL Analysis:{Style.RESET_ALL}")
        
        # Search for different URL patterns
        patterns = [
            f"*.{domain}/*",
            f"{domain}/*",
            f"www.{domain}/*"
        ]
        
        total_urls = 0
        
        for pattern in patterns:
            try:
                # Use simpler search for statistics
                search_url = f"https://index.commoncrawl.org/CC-MAIN-2024-10-index?url={pattern}&output=json&limit=10"
                response = requests.get(search_url, timeout=10)
                
                if response.status_code == 200:
                    lines = response.text.strip().split('\n')
                    if lines and lines[0]:
                        count = len([line for line in lines if line.strip()])
                        total_urls += count
                        print(f"    {Fore.CYAN}Pattern '{pattern}': {Fore.YELLOW}{count}+ URLs{Style.RESET_ALL}")
                        
            except:
                continue
        
        if total_urls > 0:
            print(f"    {Fore.GREEN}Total Archived URLs Found: {Fore.YELLOW}{total_urls}+{Style.RESET_ALL}")
        
        # Provide additional analysis suggestions
        print(f"\n{Fore.GREEN}[+] Analysis Recommendations:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Use Wayback Machine for historical content analysis{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Check archived robots.txt and sitemap files{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Analyze archived JavaScript files for endpoints{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}• Look for exposed configuration files in archives{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"    {Fore.RED}✗ Error getting URL statistics: {str(e)}{Style.RESET_ALL}")

def search_specific_files(domain, file_types):
    """Search for specific file types in Common Crawl"""
    try:
        print(f"\n{Fore.GREEN}[+] Searching for specific file types:{Style.RESET_ALL}")
        
        for file_type in file_types:
            search_url = f"https://index.commoncrawl.org/CC-MAIN-2024-10-index?url=*.{domain}/*.{file_type}&output=json&limit=20"
            
            try:
                response = requests.get(search_url, timeout=10)
                if response.status_code == 200:
                    lines = response.text.strip().split('\n')
                    if lines and lines[0]:
                        count = len([line for line in lines if line.strip()])
                        print(f"    {Fore.CYAN}.{file_type} files: {Fore.YELLOW}{count} found{Style.RESET_ALL}")
                        
            except:
                continue
                
    except Exception as e:
        print(f"    {Fore.RED}✗ Error searching specific files: {str(e)}{Style.RESET_ALL}")
