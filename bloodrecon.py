#!/usr/bin/env python3
"""
OSINT Intelligence Gathering Tool
A comprehensive OSINT toolkit for cybersecurity professionals 
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

import argparse
import sys
import os
import time
from modules.colors import *
from modules import (
    ip_lookup, whois_lookup, dns_lookup, http_headers, 
    robots_scanner, wayback_machine, leak_search, reverse_dns,
    port_scanner, email_validator, social_checker, exif_extractor,
    url_analyzer, subdomain_finder, useragent_detector, temp_email_checker,
    google_dorking, github_intel, pastebin_search, doc_metadata, 
    google_drive_leaks, phone_intel, ip_range_scanner, 
    ssl_scanner, tech_fingerprint, 
    common_crawl, directory_bruteforce, js_endpoint_scanner, sitemap_parser,
    favicon_hash, asn_resolver, shodan_lookup, isp_tracker, maps_parser
)

VERSION = "1.0"
AUTHOR = "Alex Butler [Vritra Security Organization]"
TOOL_NAME = "BloodRecon"

def display_banner():
    """Display futuristic ASCII banner"""
    banner = f"""
{BANNER}╔═════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                         ║
║  {MENU_HEADER}██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗{BANNER}  ║
║  {MENU_HEADER}██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║{BANNER}  ║
║  {MENU_HEADER}██████╔╝██║     ██║   ██║██║   ██║██║  ██║██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║{BANNER}  ║
║  {MENU_HEADER}██╔══██╗██║     ██║   ██║██║   ██║██║  ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║{BANNER}  ║
║  {MENU_HEADER}██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║{BANNER}  ║
║  {MENU_HEADER}╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝{BANNER}  ║
║                                                                                         ║
║  {ERROR}                    ⚡ OSINT Intelligence Framework ⚡                       {BANNER}          ║
║  {WARNING_TEXT}                         🩸 Blood is the Key 🩸                          {BANNER}              ║
║                                                                                         ║
║  {VERSION_INFO}▶ Intelligence Reconnaissance & Analysis Framework v{VERSION}                                {BANNER}║
║  {AUTHOR_INFO}▶ Developer: {MENU_HEADER}{AUTHOR}                                {BANNER}║
║  {WARNING_TEXT}▶ [DISCLAIMER] For Educational and Authorized Security Testing Only                    {BANNER}║
╚═════════════════════════════════════════════════════════════════════════════════════════╝{RESET_ALL}
    """
    print(banner)

def display_menu():
    """Display interactive menu"""
    menu = f"""
{BANNER}╔═════════════════════════════════════════════════════════════════════╗
║                         {MENU_HEADER}BLOODRECON MODULES MENU{BANNER}                     ║
╠═════════════════════════════════════════════════════════════════════╣
║  {MENU_OPTION}[1]{MENU_TEXT}  IP Address Intelligence     {MENU_OPTION}[18]{MENU_TEXT} GitHub Intelligence          ║
║  {MENU_OPTION}[2]{MENU_TEXT}  WHOIS Domain Lookup         {MENU_OPTION}[19]{MENU_TEXT} Pastebin Dump Search         ║
║  {MENU_OPTION}[3]{MENU_TEXT}  DNS Records Analysis        {MENU_OPTION}[20]{MENU_TEXT} Document Metadata Extractor  ║
║  {MENU_OPTION}[4]{MENU_TEXT}  HTTP Headers Analysis       {MENU_OPTION}[21]{MENU_TEXT} Google Drive Leak Finder     ║
║  {MENU_OPTION}[5]{MENU_TEXT}  Robots.txt Scanner          {MENU_OPTION}[22]{MENU_TEXT} Phone Number Intelligence    ║
║  {MENU_OPTION}[6]{MENU_TEXT}  Wayback Machine Search      {MENU_OPTION}[23]{MENU_TEXT} IP Range Scanner             ║
║  {MENU_OPTION}[7]{MENU_TEXT}  Data Breach Search          {MENU_OPTION}[24]{MENU_TEXT} SSL Certificate Scanner      ║
║  {MENU_OPTION}[8]{MENU_TEXT}  Reverse DNS Lookup          {MENU_OPTION}[25]{MENU_TEXT} Technology Fingerprint       ║
║  {MENU_OPTION}[9]{MENU_TEXT}  Port Scanner                {MENU_OPTION}[26]{MENU_TEXT} Common Crawl Data Search     ║
║  {MENU_OPTION}[10]{MENU_TEXT} Email Validation            {MENU_OPTION}[27]{MENU_TEXT} Directory Bruteforcer        ║
║  {MENU_OPTION}[11]{MENU_TEXT} Social Media Checker        {MENU_OPTION}[28]{MENU_TEXT} JavaScript Endpoint Scanner  ║
║  {MENU_OPTION}[12]{MENU_TEXT} EXIF Metadata Extractor     {MENU_OPTION}[29]{MENU_TEXT} Sitemap Parser               ║
║  {MENU_OPTION}[13]{MENU_TEXT} URL Threat Analysis         {MENU_OPTION}[30]{MENU_TEXT} Favicon Hash Identifier      ║
║  {MENU_OPTION}[14]{MENU_TEXT} Subdomain Discovery         {MENU_OPTION}[31]{MENU_TEXT} ASN to IP Range Resolver     ║
║  {MENU_OPTION}[15]{MENU_TEXT} User-Agent Analyzer         {MENU_OPTION}[32]{MENU_TEXT} Shodan Intelligence Lookup   ║
║  {MENU_OPTION}[16]{MENU_TEXT} Temp Email Detector         {MENU_OPTION}[33]{MENU_TEXT} IP to ISP Tracker            ║
║  {MENU_OPTION}[17]{MENU_TEXT} Google Dorking              {MENU_OPTION}[34]{MENU_TEXT} Google Maps Link Parse       ║
╠═════════════════════════════════════════════════════════════════════╣
║  {INFO}[35]{MENU_TEXT} About This Tool             {INFO}[36]{MENU_TEXT} Connect with Us              ║
║  {ERROR}[0]{MENU_TEXT}  Exit Program                                                  ║
╠═════════════════════════════════════════════════════════════════════╣
║  {MENU_HEADER}▶ Enter your choice [0-36]:{MENU_TEXT}                                        ║
╚═════════════════════════════════════════════════════════════════════╝{RESET_ALL}
    """
    print(menu)

def display_about():
    """Display detailed information about the tool"""
    about_text = f"""
{BANNER}╔═══════════════════════════════════════════════════════════════════════════════╗
║                                {MENU_HEADER}ABOUT BLOODRECON{BANNER}                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝{RESET_ALL}

{INFO}🔍 WHAT IS BLOODRECON?{RESET_ALL}
{MENU_TEXT}BloodRecon is a comprehensive Open Source Intelligence (OSINT) gathering framework
designed for cybersecurity professionals, penetration testers, bug bounty hunters,
and digital forensics investigators. This tool provides a unified interface to
perform various reconnaissance and intelligence collection techniques.{RESET_ALL}

{INFO}🎯 KEY FEATURES:{RESET_ALL}
{MENU_OPTION}•{MENU_TEXT} 34 Specialized OSINT Modules
{MENU_OPTION}•{MENU_TEXT} Network & Infrastructure Analysis (IP, DNS, WHOIS, SSL, Ports)
{MENU_OPTION}•{MENU_TEXT} Web Application Security Testing (Headers, Robots, Directories)
{MENU_OPTION}•{MENU_TEXT} Social Media & Personal Intelligence (GitHub, Social Platforms)
{MENU_OPTION}•{MENU_TEXT} Document & Metadata Analysis (EXIF, Document Properties)
{MENU_OPTION}•{MENU_TEXT} Advanced Search Capabilities (Google Dorking, Wayback Machine)
{MENU_OPTION}•{MENU_TEXT} Communication Intelligence (Email, Phone Number Analysis)
{MENU_OPTION}•{MENU_TEXT} Threat Intelligence Integration (Shodan)
{MENU_OPTION}•{MENU_TEXT} Data Breach & Leak Detection
{MENU_OPTION}•{MENU_TEXT} Interactive CLI Interface with Target Input Examples{RESET_ALL}

{INFO}👨‍💻 DEVELOPER INFORMATION:{RESET_ALL}
{DATA_LABEL}Name:{DATA_VALUE}         Alex Butler [Vritra Security Organization]
{DATA_LABEL}Organization: {DATA_VALUE}Vritra Security Organization
{DATA_LABEL}Version:{DATA_VALUE}      {VERSION}
{DATA_LABEL}License:{DATA_VALUE}      Educational & Authorized Testing Only
{DATA_LABEL}Platform:{DATA_VALUE}     Cross-platform (Linux, Windows, macOS){RESET_ALL}

{INFO}🛡️ ETHICAL USE POLICY:{RESET_ALL}
{WARNING_TEXT}This tool is designed exclusively for:{RESET_ALL}
{FOUND}✓{MENU_TEXT} Educational purposes and learning OSINT techniques
{FOUND}✓{MENU_TEXT} Authorized penetration testing and security assessments
{FOUND}✓{MENU_TEXT} Bug bounty programs with proper scope authorization
{FOUND}✓{MENU_TEXT} Digital forensics investigations by authorized personnel
{FOUND}✓{MENU_TEXT} Security research within legal boundaries{RESET_ALL}

{ERROR}⚠️  PROHIBITED USES:{RESET_ALL}
{NOT_FOUND}✗{MENU_TEXT} Unauthorized surveillance or stalking
{NOT_FOUND}✗{MENU_TEXT} Illegal data collection or privacy violations
{NOT_FOUND}✗{MENU_TEXT} Malicious reconnaissance or attack preparation
{NOT_FOUND}✗{MENU_TEXT} Any activity violating local, state, or federal laws{RESET_ALL}

{INFO}🔧 TECHNICAL SPECIFICATIONS:{RESET_ALL}
{DATA_LABEL}Language:{DATA_VALUE}     Python 3.x
{DATA_LABEL}Dependencies:{DATA_VALUE} See requirements.txt for full list
{DATA_LABEL}Modules:{DATA_VALUE}      37 specialized OSINT modules
{DATA_LABEL}Interface:{DATA_VALUE}    Command-line and Interactive menu
{DATA_LABEL}Output:{DATA_VALUE}       Colored terminal output with structured data{RESET_ALL}"""
    print(about_text)

def display_connect():
    """Display developer social media and contact information"""
    connect_text = f"""
{BANNER}╔═══════════════════════════════════════════════════════════════════════════════╗
║                           {MENU_HEADER}CONNECT WITH THE DEVELOPER{BANNER}                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝{RESET_ALL}

{INFO}👨‍💻 DEVELOPER: Alex Butler [Vritra Security Organization]{RESET_ALL}

{MENU_HEADER}🌐 SOCIAL MEDIA & PROFESSIONAL LINKS:{RESET_ALL}

{LIGHTBLUE_EX}🐙 GitHub:{MENU_TEXT}
   {URL_COLOR}https://github.com/VritraSecz
   {MENU_TEXT}• Open-source tools and code contributions
   • Follow for latest tool updates and releases
   • Projects focused on OSINT and crypto recovery{RESET_ALL}

{LIGHTBLUE_EX}🌐 Website:{MENU_TEXT}
   {URL_COLOR}https://vritrasec.com
   {MENU_TEXT}• Explore software, services, and pricing
   • Crypto-based secure checkout system
   • Learn about Vritra Security Organization{RESET_ALL}

{LIGHTBLUE_EX}📸 Instagram:{MENU_TEXT}
   {URL_COLOR}https://instagram.com/haxorlex
   {MENU_TEXT}• Occasionally shares software or tool updates
   • No regular posts — strictly for presence
   • DM open for informal convos or queries{RESET_ALL}

{LIGHTBLUE_EX}▶️ YouTube:{MENU_TEXT}
   {URL_COLOR}https://youtube.com/@Technolex
   {MENU_TEXT}• Tool demos, walkthroughs, and guides
   • Topics include Termux, Linux, and OSINT
   • Subscribe for useful and honest content drops{RESET_ALL}

{LIGHTBLUE_EX}📢 Telegram (Central):{MENU_TEXT}
   {URL_COLOR}https://t.me/LinkCentralX
   {MENU_TEXT}• All important links and updates in one place
   • Easy access to tools, bots, and channels
   • Regular software promotions and quick links{RESET_ALL}

{LIGHTBLUE_EX}⚡ Telegram (Main Channel):{MENU_TEXT}
   {URL_COLOR}https://t.me/VritraSec
   {MENU_TEXT}• Core channel for official announcements
   • Software updates, features, and patch notes
   • Lifetime users and buyers should follow here{RESET_ALL}

{LIGHTBLUE_EX}💬 Telegram (Community):{MENU_TEXT}
   {URL_COLOR}https://t.me/VritraSecz
   {MENU_TEXT}• Open chat for discussion and queries
   • Users share feedback, ask doubts, and collaborate
   • Real-time support and casual conversation space{RESET_ALL}

{LIGHTBLUE_EX}🤖 Support Bot:{MENU_TEXT}
   {URL_COLOR}https://t.me/ethicxbot
   {MENU_TEXT}• Manually operated bot for queries and orders
   • Ask about pricing, availability, or license info
   • Direct human interaction — not an automated system{RESET_ALL}

{INFO}💡 SUPPORT THE PROJECT:{RESET_ALL}
{FOUND}⭐{MENU_TEXT} Star the repository on GitHub
{FOUND}🔔{MENU_TEXT} Follow on social media for updates
{FOUND}📢{MENU_TEXT} Share with the cybersecurity community
{FOUND}🐛{MENU_TEXT} Report bugs and suggest improvements
{FOUND}🤝{MENU_TEXT} Contribute code and documentation{RESET_ALL}

{INFO}🎯 COLLABORATION OPPORTUNITIES:{RESET_ALL}
{MENU_TEXT}• Open source contributions welcome
• Security research collaborations
• Educational content creation
• Tool testing and feedback
• Community building initiatives{RESET_ALL}

{WARNING_TEXT}📋 RESPONSIBLE DISCLOSURE:{RESET_ALL}
{MENU_TEXT}If you discover security vulnerabilities in this tool, please report them
responsibly through our GitHub security advisory or direct on instagram.{RESET_ALL}"""
    print(connect_text)

'''
def handle_shodan_lookup(target):
    """Handle Shodan lookup with API key prompt"""
    api_key = os.environ.get('SHODAN_API_KEY')
    if not api_key:
        api_key = input(f"{INPUT_PROMPT}[>] Enter Shodan API key (or press Enter to skip): {RESET_ALL}").strip()
    
    if api_key:
        shodan = shodan_lookup.ShodanLookup(api_key)
        shodan.search_shodan(target)
    else:
        shodan_lookup.search_shodan_host(target, None)
'''


def handle_menu_choice(choice):
    """Handle menu selection"""
    
    if choice == '35':
        display_about()
        return
    elif choice == '36':
        display_connect()
        return
    
    target_examples = {
        '1': "IP address (e.g., 8.8.8.8, 192.168.1.1)",
        '2': "Domain name (e.g., example.com, google.com)",
        '3': "Domain name (e.g., google.com, github.com)",
        '4': "URL (e.g., https://example.com, http://target.com)",
        '5': "URL (e.g., https://example.com, http://target.com/robots.txt)",
        '6': "Domain name (e.g., example.com, archive.org)",
        '7': "Email address (e.g., user@example.com, test@domain.com)",
        '8': "IP address (e.g., 8.8.8.8, 1.1.1.1)",
        '9': "IP address or hostname (e.g., 192.168.1.1, example.com)",
        '10': "Email address (e.g., test@example.com, user@domain.com)",
        '11': "Username (e.g., johndoe, alice_smith, user123)",
        '12': "Image file path (e.g., /path/to/image.jpg, photo.png)",
        '13': "URL (e.g., https://suspicious-site.com, http://malware.com)",
        '14': "Domain name (e.g., example.com, target-domain.org)",
        '15': "User-Agent string (e.g., Mozilla/5.0 (Windows NT 10.0; Win64; x64))",
        '16': "Email address (e.g., test@tempmail.com, user@10minutemail.com)",
        '17': "Search query (e.g., site:example.com filetype:pdf, inurl:admin)",
        '18': "GitHub username or repo (e.g., octocat, microsoft/vscode)",
        '19': "Search term or paste ID (e.g., email, password, API_KEY)",
        '20': "Document file path (e.g., /path/to/document.pdf, file.docx)",
        '21': "Google Drive folder ID or search term (e.g., 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs95J)",
        '22': "Phone number (e.g., +1234567890, +44 20 7946 0958)",
        '23': "IP range (e.g., 192.168.1.0/24, 10.0.0.0/16)",
        '24': "Domain:port (e.g., example.com:443, google.com:443)",
        '25': "URL (e.g., https://example.com, http://webapp.com)",
        '26': "Domain name (e.g., example.com, target-site.org)",
        '27': "URL (e.g., https://example.com, http://target.com)",
        '28': "URL (e.g., https://example.com, http://webapp.com/app.js)",
        '29': "URL (e.g., https://example.com, http://site.com/sitemap.xml)",
        '30': "URL (e.g., https://example.com, http://target.com)",
        '31': "ASN number (e.g., AS15169, AS13335, AS8075)",
        '32': "IP address or hostname (e.g., 8.8.8.8, example.com)",
        '33': "IP address (e.g., 8.8.8.8, 192.168.1.1)",
        '34': "Google Maps URL (e.g., https://maps.google.com/maps?q=...)",
    }
    
    # Get example for the selected choice
    example = target_examples.get(choice, "target")
    target = input(f"{INPUT_PROMPT}[>] Enter target {INPUT_EXAMPLE}({example}){INPUT_PROMPT}: {RESET_ALL}")
    
    modules = {
        '1': lambda: ip_lookup.analyze_ip(target),
        '2': lambda: whois_lookup.get_whois_info(target),
        '3': lambda: dns_lookup.get_dns_records(target),
        '4': lambda: http_headers.get_headers(target),
        '5': lambda: robots_scanner.scan_robots(target),
        '6': lambda: wayback_machine.search_wayback(target),
        '7': lambda: leak_search.search_leaks(target),
        '8': lambda: reverse_dns.reverse_lookup(target),
        '9': lambda: port_scanner.scan_ports(target),
        '10': lambda: email_validator.validate_email(target),
        '11': lambda: social_checker.check_username(target),
        '12': lambda: exif_extractor.extract_exif(target),
        '13': lambda: url_analyzer.analyze_url(target),
        '14': lambda: subdomain_finder.find_subdomains(target),
        '15': lambda: useragent_detector.analyze_useragent(target),
        '16': lambda: temp_email_checker.check_temp_email(target),
        '17': lambda: google_dorking.perform_dorking(target),
        '18': lambda: github_intel.analyze_github_target(target),
        '19': lambda: pastebin_search.search_pastebin(target),
        '20': lambda: doc_metadata.extract_document_metadata(target),
        '21': lambda: google_drive_leaks.search_google_drive_leaks(target),
        '22': lambda: phone_intel.analyze_phone_number(target),
        '23': lambda: ip_range_scanner.scan_ip_range(target),
        '24': lambda: ssl_scanner.scan_ssl_certificate(target),
        '25': lambda: tech_fingerprint.fingerprint_technology(target),
        '26': lambda: common_crawl.search_common_crawl(target),
        '27': lambda: directory_bruteforce.bruteforce_directories(target, 'modules/list-imp/common.txt'),
        '28': lambda: js_endpoint_scanner.scan_js_endpoints(target),
        '29': lambda: sitemap_parser.parse_sitemap(target),
        '30': lambda: favicon_hash.generate_favicon_hash(target),
        '31': lambda: asn_resolver.resolve_asn_to_ranges(target),
        '32': lambda: shodan_lookup.search_shodan_host(target),
#        '32': lambda: handle_shodan_lookup(target),
        '33': lambda: isp_tracker.track_ip_to_isp(target),
        '34': lambda: maps_parser.parse_google_maps_link(target),
    }
    
    if choice in modules:
        try:
            modules[choice]()
        except Exception as e:
            print_error(f"Module execution failed: {str(e)}")
    else:
        print_error("Invalid choice!")

def interactive_mode():
    """Run interactive menu mode"""
    while True:
        display_menu()
        choice = input(f"{INPUT_PROMPT}bloodrecon> {RESET_ALL}").strip()
        
        if choice == '0':
            print_success("Thank you for using BloodRecon!")
            break
        elif choice == "":
            pass
        else:
            handle_menu_choice(choice)
            input(f"\n{URL_COLOR}🔍 Analysis done. {YELLOW}Enter {URL_COLOR}to decode next clue")
            os.system('clear' if os.name == 'posix' else 'cls')
            display_banner()

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description=f'{TOOL_NAME} - Advanced OSINT Intelligence Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  {sys.argv[0]} --ip 8.8.8.8                       # Analyze an IP address
  {sys.argv[0]} --whois example.com                # Perform WHOIS lookup for a domain
  {sys.argv[0]} --dns google.com                   # Get DNS records for a domain
  {sys.argv[0]} --headers https://example.com      # Analyze HTTP headers
  {sys.argv[0]} --robots https://example.com       # Scan for Robots.txt
  {sys.argv[0]} --wayback example.com              # Search Wayback Machine
  {sys.argv[0]} --leak email@example.com           # Search for data breaches
  {sys.argv[0]} --reverse 8.8.8.8                  # Perform reverse DNS lookup
  {sys.argv[0]} --ports 192.168.1.1                # Scan open ports
  {sys.argv[0]} --email test@example.com           # Validate email addresses
  {sys.argv[0]} --social username                  # Check social media presence
  {sys.argv[0]} --exif image.jpg                   # Extract EXIF metadata from an image
  {sys.argv[0]} --url https://suspicious-site.com  # Analyze URLs for threats
  {sys.argv[0]} --subdomains example.com           # Discover subdomains
  {sys.argv[0]} --useragent "Mozilla/5.0..."      # Analyze User-Agent strings
  {sys.argv[0]} --temp-email test@tempmail.com     # Detect temporary emails
  {sys.argv[0]} --dork "site:example.com filetype:pdf"  # Perform Google dorking
  {sys.argv[0]} --github octocat                   # Analyze GitHub user or repo
  {sys.argv[0]} --pastebin pasteID                 # Search Pastebin for dumps
  {sys.argv[0]} --metadata document.pdf            # Extract document metadata
  {sys.argv[0]} --gdrive folderID                  # Search Google Drive for leaks
  {sys.argv[0]} --phone +1234567890                # Analyze phone number intelligence
  {sys.argv[0]} --ip-scan 192.168.1.0/24           # Scan IP range for active hosts
  {sys.argv[0]} --ssl example.com:443              # Analyze SSL certificates
  {sys.argv[0]} --tech https://example.com         # Fingerprint web technologies
  {sys.argv[0]} --common-crawl example.com         # Search Common Crawl archives
  {sys.argv[0]} --dir-brute https://example.com    # Perform directory bruteforcing
  {sys.argv[0]} --js-endpoints https://example.com # Scan JavaScript for endpoints
  {sys.argv[0]} --sitemap https://example.com      # Parse and analyze sitemap
  {sys.argv[0]} --favicon https://example.com      # Generate favicon hash
  {sys.argv[0]} --asn AS15169                      # Resolve ASN to IP ranges
  {sys.argv[0]} --shodan 8.8.8.8                   # Perform Shodan search
  {sys.argv[0]} --isp 8.8.8.8                      # Track IP to ISP information
  {sys.argv[0]} --maps "https://maps.google.com/..." # Parse Google Maps links
  {sys.argv[0]} --about                            # Show detailed tool information
  {sys.argv[0]} --connect                          # Show developer contact info
  {sys.argv[0]} --interactive                      # Run interactive mode

Author: {AUTHOR}
Version: {VERSION}
        """
    )
    
    parser.add_argument('--version', action='version', version=f'{TOOL_NAME} v{VERSION}')
    parser.add_argument('--interactive', '-i', action='store_true', help='Run in interactive menu mode')
    parser.add_argument('--about', action='store_true', help='Display detailed information about the tool')
    parser.add_argument('--connect', action='store_true', help='Display developer contact and social media information')
    
    # Module arguments
    parser.add_argument('--ip', help='Analyze IP address')
    parser.add_argument('--whois', help='WHOIS lookup for domain')
    parser.add_argument('--dns', help='DNS records lookup')
    parser.add_argument('--headers', help='HTTP headers analysis')
    parser.add_argument('--robots', help='Robots.txt scanner')
    parser.add_argument('--wayback', help='Wayback Machine search')
    parser.add_argument('--leak', help='Data breach search')
    parser.add_argument('--reverse', help='Reverse DNS lookup')
    parser.add_argument('--ports', help='Port scanner')
    parser.add_argument('--email', help='Email validation')
    parser.add_argument('--social', help='Social media username check')
    parser.add_argument('--exif', help='EXIF metadata extraction')
    parser.add_argument('--url', help='URL threat analysis')
    parser.add_argument('--subdomains', help='Subdomain discovery')
    parser.add_argument('--useragent', help='User-Agent analysis')
    parser.add_argument('--temp-email', help='Temporary email detection')
    parser.add_argument('--dork', help='Google dorking')
    parser.add_argument('--github', help='Analyze GitHub user or repository')
    parser.add_argument('--pastebin', help='Search Pastebin dumps')
    parser.add_argument('--metadata', help='Extract document metadata')
    parser.add_argument('--gdrive', help='Search Google Drive leaks')
    parser.add_argument('--phone', help='Analyze phone number intelligence')
    parser.add_argument('--ip-scan', help='Scan IP range for active hosts')
    parser.add_argument('--ssl', help='SSL certificate analysis')
    parser.add_argument('--tech', help='Technology fingerprinting')
    parser.add_argument('--common-crawl', help='Search Common Crawl archives')
    parser.add_argument('--dir-brute', help='Directory bruteforcing')
    parser.add_argument('--js-endpoints', help='JavaScript endpoint scanner')
    parser.add_argument('--sitemap', help='Sitemap parser and analyzer')
    parser.add_argument('--favicon', help='Generate favicon hash for website')
    parser.add_argument('--asn', help='Resolve ASN to IP ranges')
    parser.add_argument('--shodan', help='Shodan search (requires API key)')
    parser.add_argument('--isp', help='Track IP to ISP information')
    parser.add_argument('--maps', help='Parse Google Maps links')
    args = parser.parse_args()
    
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    
    if args.about:
        display_about()
        input()
    elif args.connect:
        display_connect()
        input()
    elif args.interactive:
        interactive_mode()
    elif args.ip:
        ip_lookup.analyze_ip(args.ip)
    elif args.whois:
        whois_lookup.get_whois_info(args.whois)
    elif args.dns:
        dns_lookup.get_dns_records(args.dns)
    elif args.headers:
        http_headers.get_headers(args.headers)
    elif args.robots:
        robots_scanner.scan_robots(args.robots)
    elif args.wayback:
        wayback_machine.search_wayback(args.wayback)
    elif args.leak:
        leak_search.search_leaks(args.leak)
    elif args.reverse:
        reverse_dns.reverse_lookup(args.reverse)
    elif args.ports:
        port_scanner.scan_ports(args.ports)
    elif args.email:
        email_validator.validate_email(args.email)
    elif args.social:
        social_checker.check_username(args.social)
    elif args.exif:
        exif_extractor.extract_exif(args.exif)
    elif args.url:
        url_analyzer.analyze_url(args.url)
    elif args.subdomains:
        subdomain_finder.find_subdomains(args.subdomains)
    elif args.useragent:
        useragent_detector.analyze_useragent(args.useragent)
    elif args.temp_email:
        temp_email_checker.check_temp_email(args.temp_email)
    elif args.dork:
        google_dorking.perform_dorking(args.dork)
    elif args.github:
        github_intel.analyze_github_target(args.github)
    elif args.pastebin:
        pastebin_search.search_pastebin(args.pastebin)
    elif args.metadata:
        doc_metadata.extract_document_metadata(args.metadata)
    elif args.gdrive:
        google_drive_leaks.search_google_drive_leaks(args.gdrive)
    elif args.phone:
        phone_intel.analyze_phone_number(args.phone)
    elif args.ip_scan:
        ip_range_scanner.scan_ip_range(args.ip_scan)
    elif args.ssl:
        ssl_scanner.scan_ssl_certificate(args.ssl)
    elif args.tech:
        tech_fingerprint.fingerprint_technology(args.tech)
    elif args.common_crawl:
        common_crawl.search_common_crawl(args.common_crawl)
    elif args.dir_brute:
        directory_bruteforce.bruteforce_directories(args.dir_brute, 'modules/list-imp/common.txt')
    elif args.js_endpoints:
        js_endpoint_scanner.scan_js_endpoints(args.js_endpoints)
    elif args.sitemap:
        sitemap_parser.parse_sitemap(args.sitemap)
    elif args.favicon:
        favicon_hash.generate_favicon_hash(args.favicon)
    elif args.asn:
        asn_resolver.resolve_asn_to_ranges(args.asn)
    elif args.shodan:
        shodan_lookup.search_shodan_host(args.shodan)
#        handle_shodan_lookup(args.shodan)
    elif args.isp:
        isp_tracker.track_ip_to_isp(args.isp)
    elif args.maps:
        maps_parser.parse_google_maps_link(args.maps)
    else:
        interactive_mode()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_warning("Program interrupted by user")
        sys.exit(0)
    except Exception as e:
        print_error(f"Unexpected error: {str(e)}")
        sys.exit(1)
