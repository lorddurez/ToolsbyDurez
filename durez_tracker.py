import os
import sys
import hashlib
import subprocess
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# ==========================================
# 🔒 WATERMARK PROTECTION - DO NOT EDIT
# ==========================================
EXPECTED_HASH = "4ee531caf62442b5c4f3d8bb5e1f0750757a4f1e6ff55fb0f1b5327db8f20dab"

CREDIT_1 = "Made By DUREZ"
CREDIT_2 = "Contact me on Telegram @DU7EZ"

def _verify():
    combined = CREDIT_1 + "\n" + CREDIT_2
    if hashlib.sha256(combined.encode()).hexdigest() != EXPECTED_HASH:
        os.system('clear' if os.name != 'nt' else 'cls')
        print(Fore.RED + "[!] SYSTEM ERROR: Unable to connect to DUREZ secure server.")
        print(Fore.RED + "[!] Error Code: 0x5F_CONNECTION_TIMEOUT")
        print(Fore.YELLOW + "\nPlease check your internet connection or try again later.")
        print(Fore.WHITE + "\nTroubleshooting: Ensure your device has a stable network.")
        sys.exit(1)

# ==========================================

def banner():
    _verify()  # Lock check
    os.system('clear' if os.name != 'nt' else 'cls')
    print(Fore.BLUE + Style.BRIGHT + """
    ██████╗ ██╗   ██╗██████╗ ███████╗███████╗
    ██╔══██╗██║   ██║██╔══██╗██╔════╝╚══███╔╝
    ██║  ██║██║   ██║██████╔╝█████╗    ███╔╝ 
    ██║  ██║██║   ██║██╔══██╗██╔══╝   ███╔╝  
    ██████╔╝╚██████╔╝██║  ██║███████╗███████╗
    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
    """ + Style.RESET_ALL)
    print(Fore.CYAN + "          © Made By DUREZ")
    print(Fore.CYAN + "     Contact me on Telegram @DU7EZ\n")

def run_command(command):
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(Fore.RED + f"Error running command: {e}")
    input(Fore.GREEN + "\nPress Enter to return to the menu...")

def explain(tool_name, description):
    _verify()  # Lock check
    os.system('clear')
    print(Fore.YELLOW + f"[*] Running {tool_name}...")
    print(Fore.WHITE + f"[!] Purpose: {description}\n")
    print(Fore.CYAN + "-" * 50)

def tool_ip_tracker():
    explain("IP Tracker", "Gets location, ISP, VPN detection, and Google Maps link.")
    ip = input("Enter IP address (or press Enter for your own): ")
    data = requests.get(f"http://ip-api.com/json/{ip}").json()
    if data.get('status') == 'success':
        print(f"\nIP: {data.get('query')}\nCity: {data.get('city')}\nRegion: {data.get('regionName')}\nCountry: {data.get('country')}\nISP: {data.get('isp')}")
        print(Fore.CYAN + f"Map: https://www.google.com/maps/search/?api=1&query={data.get('lat')},{data.get('lon')}")
    else:
        print(Fore.RED + "Could not find that IP.")
    input(Fore.GREEN + "\nPress Enter to return...")

def tool_phone_tracker():
    explain("Phone Tracker", "Gets carrier, country, and timezone from a phone number.")
    number = input("Enter phone number with country code (e.g., +234...): ")
    try:
        parsed = phonenumbers.parse(number, None)
        print(f"\nCountry: {geocoder.description_for_number(parsed, 'en')}")
        print(f"Carrier: {carrier.name_for_number(parsed, 'en')}")
        print(f"Timezone: {timezone.time_zones_for_number(parsed)}")
    except:
        print(Fore.RED + "Invalid number.")
    input(Fore.GREEN + "\nPress Enter to return...")

def tool_sherlock():
    explain("Sherlock", "Hunts a username across 300+ social networks.")
    user = input("Enter username: ")
    run_command(f"sherlock {user}")

def tool_maigret():
    explain("Maigret", "Deep search for a username across 3000+ sites with data extraction.")
    user = input("Enter username: ")
    run_command(f"maigret {user}")

def tool_subfinder():
    explain("Subfinder", "Finds hidden subdomains of a target website.")
    domain = input("Enter domain (e.g., example.com): ")
    run_command(f"subfinder -d {domain}")

def tool_nmap():
    explain("Port Scanner (Nmap)", "Scans a server for open ports and running services.")
    target = input("Enter IP or domain: ")
    run_command(f"nmap -F {target}")

def tool_ffuf():
    explain("Directory Brute-Forcer (FFUF)", "Finds hidden folders and files on a website.")
    url = input("Enter URL (e.g., http://site.com/FUZZ): ")
    run_command(f"ffuf -w /usr/share/wordlists/dirb/common.txt -u {url}")

def tool_sqlmap():
    explain("SQL Injection Scanner", "Detects and tests for SQL injection flaws.")
    url = input("Enter URL with parameter (e.g., http://site.com/page?id=1): ")
    run_command(f"sqlmap -u {url} --batch --dbs")

def tool_dalfox():
    explain("XSS Scanner (Dalfox)", "Scans a website for Cross-Site Scripting vulnerabilities.")
    url = input("Enter URL: ")
    run_command(f"dalfox url {url}")

def tool_whatweb():
    explain("Web Tech Fingerprinter", "Identifies the technology a website is built with.")
    url = input("Enter URL: ")
    run_command(f"whatweb {url}")

def tool_wafw00f():
    explain("WAF Detector", "Checks if a website is protected by a Web Application Firewall.")
    url = input("Enter URL: ")
    run_command(f"wafw00f {url}")

def tool_url_expander():
    explain("URL Expander", "Unshortens links (like bit.ly) to reveal the real destination.")
    url = input("Enter shortened URL: ")
    try:
        response = requests.get(url, allow_redirects=True)
        print(Fore.GREEN + f"\nReal URL: {response.url}")
    except:
        print(Fore.RED + "Could not expand URL.")
    input(Fore.GREEN + "\nPress Enter to return...")

def tool_dns_recon():
    explain("DNS Recon", "Gathers all DNS records (MX, TXT, etc.) for a domain.")
    domain = input("Enter domain: ")
    run_command(f"nslookup -type=any {domain}")

def tool_trufflehog():
    explain("GitHub Secret Scanner", "Scans a GitHub repo for leaked API keys and passwords.")
    repo = input("Enter GitHub repo URL: ")
    run_command(f"trufflehog git {repo}")

def tool_holehe():
    explain("Email Breach Checker", "Checks if an email is registered on compromised sites.")
    email = input("Enter email: ")
    run_command(f"holehe {email}")

def tool_domain_lookup():
    explain("Domain Lookup", "Gets WHOIS information and DNS records for a website.")
    domain = input("Enter domain: ")
    run_command(f"whois {domain}")

def tool_header_analyzer():
    explain("HTTP Header Analyzer", "Checks a website's headers for security misconfigurations.")
    url = input("Enter URL: ")
    try:
        headers = requests.get(url).headers
        for key, value in headers.items():
            print(Fore.CYAN + f"{key}: {value}")
    except:
        print(Fore.RED + "Could not fetch headers.")
    input(Fore.GREEN + "\nPress Enter to return...")

def tool_scam_analyzer():
    explain("Phishing Analyzer", "Analyzes a URL for common phishing patterns.")
    url = input("Enter URL: ")
    score = 0
    if len(url) > 75: score += 1
    if "@" in url: score += 1
    if "-" in url: score += 1
    if any(word in url.lower() for word in ["login", "verify", "update", "secure"]): score += 2
    print(Fore.YELLOW + f"\nRisk Score: {score}/5")
    if score >= 3:
        print(Fore.RED + "⚠️ WARNING: High risk of phishing!")
    else:
        print(Fore.GREEN + "✅ Looks relatively safe.")
    input(Fore.GREEN + "\nPress Enter to return...")

def tool_web_sift():
    explain("WebSift", "Scrapes a website to extract emails, phone numbers, and social links.")
    url = input("Enter URL: ")
    try:
        html = requests.get(url).text
        import re
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)
        phones = re.findall(r'\+?\d[\d -]{8,12}\d', html)
        print(Fore.CYAN + f"\nEmails found: {set(emails)}")
        print(Fore.CYAN + f"Phone numbers found: {set(phones)}")
    except:
        print(Fore.RED + "Could not scrape website.")
    input(Fore.GREEN + "\nPress Enter to return...")

def menu():
    while True:
        banner()
        print(Fore.CYAN + "[+] OSINT & Information Gathering")
        print("  [1] IP Tracker          [2] Phone Tracker")
        print("  [3] Sherlock            [4] Maigret")
        print("  [5] WebSift             [6] Email Breach Checker")
        print("  [7] Domain Lookup")
        print(Fore.CYAN + "\n[+] Website & Web App Analysis")
        print("  [8] Subdomain Finder    [9] Port Scanner (Nmap)")
        print("  [10] Dir Brute-Forcer   [11] XSS Scanner")
        print("  [12] SQL Injection      [13] Web Tech Fingerprinter")
        print("  [14] WAF Detector       [15] HTTP Header Analyzer")
        print(Fore.CYAN + "\n[+] Scam & Phishing Detection")
        print("  [16] URL Expander       [17] Phishing Analyzer")
        print("  [18] Threat Intel")
        print(Fore.CYAN + "\n[+] Network & Recon")
        print("  [19] DNS Recon          [20] GitHub Secret Scanner")
        print(Fore.RED + "\n  [0] Exit")

        choice = input(Fore.YELLOW + "\nSelect a tool: ")

        if choice == '1': tool_ip_tracker()
        elif choice == '2': tool_phone_tracker()
        elif choice == '3': tool_sherlock()
        elif choice == '4': tool_maigret()
        elif choice == '5': tool_web_sift()
        elif choice == '6': tool_holehe()
        elif choice == '7': tool_domain_lookup()
        elif choice == '8': tool_subfinder()
        elif choice == '9': tool_nmap()
        elif choice == '10': tool_ffuf()
        elif choice == '11': tool_dalfox()
        elif choice == '12': tool_sqlmap()
        elif choice == '13': tool_whatweb()
        elif choice == '14': tool_wafw00f()
        elif choice == '15': tool_header_analyzer()
        elif choice == '16': tool_url_expander()
        elif choice == '17': tool_scam_analyzer()
        elif choice == '18': print(Fore.YELLOW + "Threat Intel: (Feature coming soon)"); input()
        elif choice == '19': tool_dns_recon()
        elif choice == '20': tool_trufflehog()
        elif choice == '0': sys.exit()
        else: print(Fore.RED + "Invalid choice."); input()

if __name__ == "__main__":
    menu()
