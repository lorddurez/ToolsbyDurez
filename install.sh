#!/bin/bash

echo "====================================="
echo " Installing DUREZ TRACKER v2.0"
echo "====================================="

# Update and install base dependencies
pkg update -y && pkg upgrade -y
pkg install python git curl wget ruby figlet lolcat nmap dnsutils -y
pkg install ffuf sqlmap whatweb wafw00f -y

# Install Python libraries
pip install requests phonenumbers dnspython colorama
pip install sherlock-project maigret holehe

# Install Go tools (Subfinder, Dalfox, Trufflehog)
pkg install golang -y
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/hahwul/dalfox/v2@latest
go install -v github.com/trufflesecurity/trufflehog/v3@latest

# Move Go binaries to a path Termux can access
cp $HOME/go/bin/* $PREFIX/bin/ 2>/dev/null

echo ""
echo "====================================="
echo " Installation Complete!"
echo " Run: python3 durez_tracker.py"
echo "====================================="
