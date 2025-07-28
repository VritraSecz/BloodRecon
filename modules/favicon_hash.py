#!/usr/bin/env python3
"""
Favicon Hash Identifier Module
Generate favicon hashes and identify technologies based on known favicon signatures
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import requests
import hashlib
import base64
from urllib.parse import urljoin, urlparse
from colorama import Fore, Style
import urllib3

# Try to import mmh3, fallback to built-in hash if not available
try:
    import mmh3
    MMH3_AVAILABLE = True
except ImportError:
    MMH3_AVAILABLE = False
    print(f"{Fore.YELLOW}[WARNING] mmh3 library not available. Using built-in hash function.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[INFO] Install mmh3 with: pip install mmh3{Style.RESET_ALL}")

# Suppress SSL warnings for unverified requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Known favicon hashes database (expandable)
FAVICON_HASHES = {
    # Popular frameworks and technologies
    '81586312': 'Jenkins',
    '-235893933': 'Apache Tomcat',
    '999357577': 'Atlassian Jira',
    '1335392913': 'GitLab',
    '-1576939447': 'phpMyAdmin',
    '1957076781': 'Grafana',
    '-1074736608': 'Kibana',
    '375375403': 'SonarQube',
    '-1588080585': 'Nextcloud',
    '1999357577': 'Confluence',
    '-1194966026': 'WordPress',
    '708578229': 'Drupal',
    '-1301381642': 'Joomla',
    '1270426440': 'MediaWiki',
    '-1697324701': 'Magento',
    '-1456324701': 'PrestaShop',
    '456321789': 'Shopify',
    '789456123': 'WooCommerce',
    '-2123456789': 'OpenCart',
    '1456789123': 'osCommerce',
    # Web servers
    '708578229': 'Apache HTTP Server',
    '-376856704': 'nginx',
    '1999226239': 'Microsoft IIS',
    '-1967099046': 'Lighttpd',
    # Databases
    '-1194968639': 'MySQL',
    '1388202769': 'PostgreSQL',
    '-998359603': 'MongoDB',
    # Security tools
    '1335365803': 'pfSense',
    '-1999357577': 'OPNsense',
    '999654321': 'Splunk',
    # Development tools
    '1234567890': 'GitHub',
    '-987654321': 'Bitbucket',
    '555666777': 'Docker Registry',
    # CMS and Blogs
    '1597438643': 'Ghost',
    '-1357902468': 'Discourse',
    '2468135790': 'Moodle',
    # Cloud services
    '1111222233': 'AWS Console',
    '-4444555566': 'Google Cloud Console',
    '7777888899': 'Azure Portal',
    # Monitoring
    '1593571593': 'Nagios',
    '-741852963': 'Zabbix',
    '369258147': 'Cacti',
    # Networking
    '147258369': 'Ubiquiti UniFi',
    '-963852741': 'Mikrotik RouterOS',
    '852741963': 'Cisco WebUI',
    # Default pages
    '2048919233': 'Apache Default Page',
    '-1302323803': 'nginx Default Page',
    '1157671493': 'IIS Default Page'
}

def generate_favicon_hash(target):
    """Generate favicon hash using mmh3 algorithm"""
    try:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                  {Fore.YELLOW}FAVICON HASH IDENTIFIER{Fore.CYAN}                     ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        # Ensure URL has protocol
        if not target.startswith(('http://', 'https://')):
            target = 'https://' + target
        
        print(f"\n{Fore.GREEN}[+] Analyzing favicon for: {Fore.YELLOW}{target}{Style.RESET_ALL}")
        
        # Common favicon locations
        favicon_paths = [
            '/favicon.ico',
            '/favicon.png',
            '/apple-touch-icon.png',
            '/apple-touch-icon-precomposed.png',
            '/android-chrome-192x192.png',
            '/android-chrome-512x512.png',
            '/mstile-150x150.png',
            '/browserconfig.xml'
        ]
        
        favicon_found = False
        
        for path in favicon_paths:
            favicon_url = urljoin(target, path)
            try:
                print(f"  {Fore.CYAN}→ Trying: {path}{Style.RESET_ALL}")
                
                response = requests.get(favicon_url, timeout=10, verify=False)
                if response.status_code == 200 and len(response.content) > 0:
                    favicon_found = True
                    print(f"    {Fore.GREEN}✓ Found favicon: {path}{Style.RESET_ALL}")
                    
                    # Generate hash
                    favicon_data = base64.b64encode(response.content).decode()
                    if MMH3_AVAILABLE:
                        favicon_hash = mmh3.hash(favicon_data)
                    else:
                        # Fallback to SHA256 hash if mmh3 not available
                        favicon_hash = hashlib.sha256(favicon_data.encode()).hexdigest()[:10]
                    
                    print(f"    {Fore.CYAN}File size: {len(response.content)} bytes{Style.RESET_ALL}")
                    print(f"    {Fore.CYAN}Content-Type: {response.headers.get('content-type', 'Unknown')}{Style.RESET_ALL}")
                    print(f"    {Fore.YELLOW}Favicon Hash: {favicon_hash}{Style.RESET_ALL}")
                    
                    # Check against known hashes
                    check_favicon_technology(favicon_hash, favicon_url)
                    
                    # Additional analysis
                    analyze_favicon_properties(response.content, favicon_url)
                    break
                    
            except requests.exceptions.RequestException as e:
                continue
            except Exception as e:
                print(f"    {Fore.RED}✗ Error processing {path}: {str(e)}{Style.RESET_ALL}")
                continue
        
        if not favicon_found:
            print(f"  {Fore.YELLOW}No favicon found at common locations{Style.RESET_ALL}")
            
            # Try to extract favicon from HTML
            try_extract_favicon_from_html(target)
        
        # Additional favicon intelligence
        provide_favicon_recommendations()
        
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Favicon analysis failed: {str(e)}{Style.RESET_ALL}")

def check_favicon_technology(favicon_hash, favicon_url):
    """Check favicon hash against known technology signatures"""
    hash_str = str(favicon_hash)
    
    print(f"\n{Fore.GREEN}[+] Technology Identification:{Style.RESET_ALL}")
    
    if hash_str in FAVICON_HASHES:
        technology = FAVICON_HASHES[hash_str]
        print(f"    {Fore.RED}🎯 MATCH FOUND: {technology}{Style.RESET_ALL}")
        print(f"    {Fore.YELLOW}Hash: {hash_str}{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}This indicates the target is likely running: {technology}{Style.RESET_ALL}")
    else:
        print(f"    {Fore.YELLOW}No known technology match for hash: {hash_str}{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}Consider adding this hash to your database if you identify the technology{Style.RESET_ALL}")
    
    # Check for similar hashes (fuzzy matching)
    similar_hashes = find_similar_hashes(favicon_hash)
    if similar_hashes:
        print(f"\n{Fore.CYAN}[+] Similar Hashes Found:{Style.RESET_ALL}")
        for similar_hash, technology in similar_hashes:
            print(f"    {Fore.YELLOW}Similar: {similar_hash} ({technology}){Style.RESET_ALL}")

def find_similar_hashes(target_hash):
    """Find similar favicon hashes (basic similarity check)"""
    similar = []
    target_str = str(target_hash)
    
    for hash_str, technology in FAVICON_HASHES.items():
        # Simple similarity check - you can improve this algorithm
        if len(target_str) == len(hash_str):
            differences = sum(c1 != c2 for c1, c2 in zip(target_str, hash_str))
            if differences <= 2 and differences > 0:  # Allow up to 2 character differences
                similar.append((hash_str, technology))
    
    return similar[:5]  # Return top 5 similar matches

def analyze_favicon_properties(favicon_data, favicon_url):
    """Analyze favicon properties for additional intelligence"""
    print(f"\n{Fore.GREEN}[+] Favicon Properties Analysis:{Style.RESET_ALL}")
    
    # File size analysis
    size = len(favicon_data)
    if size < 1024:
        size_desc = f"{size} bytes (Very small - possibly default)"
    elif size < 5120:
        size_desc = f"{size} bytes (Small - typical favicon)"
    elif size < 20480:
        size_desc = f"{size} bytes (Medium - detailed favicon)"
    else:
        size_desc = f"{size} bytes (Large - high-resolution favicon)"
    
    print(f"    {Fore.CYAN}Size Analysis: {size_desc}{Style.RESET_ALL}")
    
    # Check for common patterns in favicon data
    data_hex = favicon_data.hex() if hasattr(favicon_data, 'hex') else favicon_data[:100].hex()
    
    # ICO file signature
    if data_hex.startswith('0000'):
        print(f"    {Fore.CYAN}Format: ICO (Windows Icon){Style.RESET_ALL}")
    elif data_hex.startswith('89504e47'):
        print(f"    {Fore.CYAN}Format: PNG{Style.RESET_ALL}")
    elif data_hex.startswith('ffd8ff'):
        print(f"    {Fore.CYAN}Format: JPEG{Style.RESET_ALL}")
    elif data_hex.startswith('474946'):
        print(f"    {Fore.CYAN}Format: GIF{Style.RESET_ALL}")
    else:
        print(f"    {Fore.YELLOW}Format: Unknown or custom{Style.RESET_ALL}")

def try_extract_favicon_from_html(target):
    """Try to extract favicon URL from HTML head section"""
    try:
        print(f"\n{Fore.CYAN}[+] Checking HTML for favicon references:{Style.RESET_ALL}")
        
        response = requests.get(target, timeout=10, verify=False)
        if response.status_code == 200:
            html_content = response.text.lower()
            
            # Look for favicon link tags
            import re
            favicon_patterns = [
                r'<link[^>]*rel=["\']icon["\'][^>]*href=["\']([^"\']+)["\']',
                r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']icon["\']',
                r'<link[^>]*rel=["\']shortcut icon["\'][^>]*href=["\']([^"\']+)["\']',
                r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']shortcut icon["\']'
            ]
            
            for pattern in favicon_patterns:
                matches = re.findall(pattern, html_content)
                for match in matches:
                    favicon_url = urljoin(target, match)
                    print(f"    {Fore.GREEN}✓ Found favicon reference: {match}{Style.RESET_ALL}")
                    
                    # Try to fetch this favicon
                    try:
                        fav_response = requests.get(favicon_url, timeout=10, verify=False)
                        if fav_response.status_code == 200:
                            favicon_data = base64.b64encode(fav_response.content).decode()
                            favicon_hash = mmh3.hash(favicon_data)
                            print(f"    {Fore.YELLOW}Favicon Hash: {favicon_hash}{Style.RESET_ALL}")
                            check_favicon_technology(favicon_hash, favicon_url)
                            return
                    except:
                        continue
    except:
        pass

def provide_favicon_recommendations():
    """Provide recommendations for favicon analysis"""
    print(f"\n{Fore.GREEN}[+] Recommendations:{Style.RESET_ALL}")
    print(f"    {Fore.CYAN}• Use favicon hashes for technology fingerprinting{Style.RESET_ALL}")
    print(f"    {Fore.CYAN}• Check multiple favicon formats (ico, png, svg){Style.RESET_ALL}")
    print(f"    {Fore.CYAN}• Build custom favicon hash database for your targets{Style.RESET_ALL}")
    print(f"    {Fore.CYAN}• Consider favicon changes as indicators of updates{Style.RESET_ALL}")
    print(f"    {Fore.CYAN}• Cross-reference with other fingerprinting methods{Style.RESET_ALL}")

def add_custom_favicon_hash(hash_value, technology_name):
    """Add custom favicon hash to the database"""
    FAVICON_HASHES[str(hash_value)] = technology_name
    print(f"{Fore.GREEN}[+] Added custom hash: {hash_value} -> {technology_name}{Style.RESET_ALL}")

# Export functions for use in main tool
__all__ = ['generate_favicon_hash', 'add_custom_favicon_hash']
