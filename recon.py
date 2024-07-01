import webbrowser
import os
import time
import sys

websites = {
    "OSINT-Framework": "available for any kind of information",
    "Have-i-been-pwned": "if you think your email or phone number has been leaked, it can be used to check this.",
    "Builtwith": "can be used to check if you are curious about which technologies the target website uses.",
    "Shodan": "can be used to obtain information about IP addresses.",
    "Track-Trace": "you may need it in CTFs. Used to determine the location from the container number.",
    "Tineye": "reverse image website, can be used to find the location from the photo and learn detailed information.",
    "Pixelied": "it helps to sharpen blurry photos, to fix the image.",
    "World-License-Plates": "it can be used to get an idea of all the plates in the world.",
    "Flight-Radar24": "available for information about airplanes.",
    "Wayback-Machine": "allows us to see snapshots of websites in use or not in use in the past, IF any.",
    "Barcode-Reader": "barcode scanner that can be used to get detailed information about airfare.",
    "Findip-Address": "it can be used to get detailed information about the IP address.",
    "Aperi'Solve": "it can help to find messages embedded in the image.(Steganography)",
    "Jimpl": "can give details about a picture 'place, device and date, etc.'",
    "Pic2Map": "can give details about a picture 'place, device and date, etc.'",
    "Wigle": "with SSID etc. information, you can scan WIFI devices around the world and check their locations.",
    "Screenshot-Machine": "to take a screenshot of a website without entering it. It can be used for security.",
    "Grabify": "it recreates the URL address of any website and when clicked, many information such as IP information can be obtained.",
    "Browserling": "it allows creating a virtual browser and browsing the website for a few minutes.",
    "Hybrid-Analysis": "can be used to analyze suspicious files",
    "Phishtank": "websites where we can check the URL addresses of phishers.",
    "Checkphish": "websites where we can check the URL addresses of phishers.",
    "Any-Run": "a website that allows you to run malware samples in a virtual environment and observe their behavior.",
    "Hashcat": "a site that can be used to find the hash type.",
    "Crack-Station": "site that can be used to decode hash types.",
    "Network-Chuck": "a browser that provides disposable internet access. cloud based. it doesn't allow access to most places.",
    "DNS-Dumpster": "detailed records related to dns are available for viewing",
    "Receive-SMSS": "can be used where telephone approval is required.",
    "Anonym-SMS": "can be used where telephone approval is required.",
    "Receive-SMS": "can be used where telephone approval is required.",
    "Generator-Email": "clones the existing mail without the need to create a mail and all mails to be sent there are automatically sent to the original address.",
    "Epieos": "the e-mail OSINT tool can be used to get information about e-mail.",
    "Bing-Mobile-Friendliness": "shows the site while testing mobile compatibility, any website can be browsed anonymously.",
    "Asharbinkhalil OSINT tools": "for other OSINT tools",
    "Letsenhance": "can be used to clarify a picture.",
    "Check-Short-URL": "a site where we can find the long version of a shortened URL.",
    "OnWorks Kali Linux Online": "online kali linux machine (also offers many extra machines like windows).",
    "Academo Spectrum Analyzer": "a site that does specturm analysis analyzes the audio file.",
    "Futureboy Steganographic Analysis": "stenagoraphic analysis, revealing the text hidden in the picture.",
    "URL-Scan": "a URL scannerthat provides URL control",
    "Proxy-Check": "a service that allows you to determine whether an IP address is malicious and/or being used for any activity such as proxy, VPN, tor service, etc.",
    "Web-Check": "an OSINT vehicle with 20 vehicles in it works fast.",
    "Link-Shield": "a site where you can scan for risky links.",
    "Whatfontis": "to find a font from a picture. It can be used in CTFs.",
    "Imei-Info": "IMEI can be queried and information can be obtained. It can be used in CTFs.",
    "Dream-Coder": "can be used in URL decode. It can be used in CTFs.",
    "SOC-Radar": "can be used to learn about anything.",
    "Intelx": "search for ip-mail etc. in leaked information.",
    "YopMail": "fast, secure email service.(ideal for single use.)"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.0000001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    banner = """
     ▄▄▄       ██▀███    ██████  ██▓    ▄▄▄       ███▄    █ 
    ▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓██▒   ▒████▄     ██ ▀█   █ 
    ▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒
    ░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒
     ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░██████▒▓█   ▓██▒▒██░   ▓██░
     ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ 
      ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░
      ░   ▒     ░░   ░ ░  ░  ░    ░ ░    ░   ▒      ░   ░ ░ 
          ░  ░   ░           ░      ░  ░     ░  ░         ░ 
    """
    slow_print(banner, delay=0.0000001)
    slow_print("Welcome to Arslan's backpack.", delay=0.0000001)

def open_website(choice):
    website_names = list(websites.keys())
    if 1 <= choice <= len(website_names):
        selected_website = website_names[choice - 1]
        webbrowser.open(f"https://{selected_website.lower().replace(' ', '')}.com/")
        slow_print(f"Launching {selected_website}...")
        slow_print("""
        ──────────▄██▄▄
        ─▄▄█████▄─██▀
        ▀█████████▄██▄
        ▒▒▀██████████▀▒
        ▒▒▒▒▒█▄█▄▄▒▒▒▒▒
        """, delay=0.0000001)
    else:
        slow_print(f"Invalid option. Please enter a number between 1 and {len(website_names)}.")

def main():
    while True:
        clear_screen()
        print_banner()
        
        slow_print("Choose an option:")
        for i, name in enumerate(websites.keys(), 1):
            slow_print(f"{i} - {name} -> \033[94m{websites[name]}\033[0m", delay=0.0000001)
        
        try:
            choice = int(input("\nEnter the number of the option you want to choose: "))
            open_website(choice)
            input("Press Enter to continue...")
        except ValueError:
            slow_print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
