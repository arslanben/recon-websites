import webbrowser
import os
import time
import sys

websites = {
    "OSINT-Framework -> available for any kind of information": "https://osintframework.com/",
    "Have-i-been-pwned -> if you think your email or phone number has been leaked, it can be used to check this.": "https://haveibeenpwned.com/",
    "Builtwith -> can be used to check if you are curious about which technologies the target website uses.": "https://builtwith.com/",
    "Shodan -> can be used to obtain information about IP addresses.": "https://shodan.io/",
    "Track-Trace -> you may need it in CTFs. Used to determine the location from the container number.": "https://www.track-trace.com/container/",
    "Tineye -> reverse image website, can be used to find the location from the photo and learn detailed information.": "https://tineye.com/",
    "Pixelied -> it helps to sharpen blurry photos, to fix the image.": "https://pixelied.com/",
    "World-License-Plates -> it can be used to get an idea of all the plates in the world.": "http://www.worldlicenseplates.com/",
    "Flight-Radar24 -> available for information about airplanes.": "https://www.flightradar24.com/",
    "Wayback-Machine -> allows us to see snapshots of websites in use or not in use in the past, IF any.": "https://archive.org/web/",
    "Barcode-Reader -> barcode scanner that can be used to get detailed information about airfare.": "https://online-barcode-reader.inliteresearch.com/",
    "Findip-Address ->  it can be used to get detailed information about the IP address.": "https://www.findip-address.com/",
    "Aperi'Solve -> it can help to find messages embedded in the image.(Steganography)": "https://www.aperisolve.com/",
    "Jimpl -> can give details about a picture 'place, device and date, etc.'": "https://jimpl.com/",
    "Pic2Map -> can give details about a picture 'place, device and date, etc.'": "https://www.pic2map.com/",
    "Wigle -> with SSID etc. information, you can scan WIFI devices around the world and check their locations.": "https://www.wigle.net/",
    "Screenshot-Machine -> to take a screenshot of a website without entering it. It can be used for security.": "https://www.screenshotmachine.com/",
    "Grabify -> it recreates the URL address of any website and when clicked, many information such as IP information can be obtained.": "https://grabify.link/",
    "Browserling -> it allows creating a virtual browser and browsing the website for a few minutes.": "https://www.browserling.com/",
    "Hybrid-Analysis -> can be used to analyze suspicious files": "https://hybrid-analysis.com/",
    "Phishtank -> websites where we can check the URL addresses of phishers.": "https://phishtank.org/",
    "Checkphish -> websites where we can check the URL addresses of phishers.": "https://checkphish.ai/",
    "Any-Run -> a website that allows you to run malware samples in a virtual environment and observe their behavior.": "https://app.any.run/",
    "Hashcat -> a site that can be used to find the hash type.": "https://hashcat.net/wiki/doku.php?id=example_hashes",
    "Crack-Station -> site that can be used to decode hash types.": "https://crackstation.net/",
    "Network-Chuck -> a browser that provides disposable internet access. cloud based. it doesn't allow access to most places.": "https://browser.networkchuck.com/",
    "DNS-Dumpster -> detailed records related to dns are available for viewing": "https://dnsdumpster.com/",
    "Receive-SMSS -> can be used where telephone approval is required.": "https://receive-smss.com/",
    "Anonym-SMS -> can be used where telephone approval is required.": "https://anonymsms.com/",
    "Receive-SMS -> can be used where telephone approval is required.": "https://www.receivesms.co/",
    "Generator-Email -> clones the existing mail without the need to create a mail and all mails to be sent there are automatically sent to the original address.": "https://generator.email/blog/gmail-generator",
    "Epieos -> the e-mail OSINT tool can be used to get information about e-mail.": "https://epieos.com/",
    "Bing-Mobile-Friendliness -> shows the site while testing mobile compatibility, any website can be browsed anonymously.": "https://www.bing.com/webmaster/tools/mobile-friendliness",
    "Asharbinkhalil OSINT tools -> for other OSINT tools": "https://github.com/asharbinkhalil/intellitoolz",
    "Letsenhance -> can be used to clarify a picture.": "https://letsenhance.io/boost",
    "Check-Short-URL -> a site where we can find the long version of a shortened URL.": "https://checkshorturl.com/",
    "OnWorks Kali Linux Online -> online kali linux machine (also offers many extra machines like windows).": "https://www.onworks.net/tr/os-distributions/debian-based/free-kali-linux-online",
    "Academo Spectrum Analyzer -> a site that does specturm analysis analyzes the audio file.": "https://academo.org/demos/spectrum-analyzer/",
    "Futureboy Steganographic Analysis -> stenagoraphic analysis, revealing the text hidden in the picture.": "https://futureboy.us/stegano/decinput.html",
    "URL-Scan -> a URL scannerthat provides URL control": "https://urlscan.io/",
    "Proxy-Check -> a service that allows you to determine whether an IP address is malicious and/or being used for any activity such as proxy, VPN, tor service, etc.": "https://proxycheck.io/",
    "Web-Check -> an OSINT vehicle with 20 vehicles in it works fast.": "https://web-check.as93.net/",
    "Link-Shield -> a site where you can scan for risky links.": "https://linkshieldapi.com/",
    "Whatfontis -> to find a font from a picture. It can be used in CTFs.": "https://www.whatfontis.com/",
    "Imei-Info -> IMEI can be queried and information can be obtained. It can be used in CTFs.": "https://www.imei.info/",
    "Dream-Coder -> can be used in URL decode. It can be used in CTFs.": "https://dreamdecoder.me/chat",
    "SOC-Radar -> can be used to learn about anything.": "https://socradar.io/labs/",
    "Intelx -> search for ip-mail etc. in leaked information.": "https://intelx.io/",
    "YopMail -> fast, secure email service.(ideal for single use.)": "https://yopmail.com/"
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
        url = websites[selected_website]
        webbrowser.open(url)
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
        for i, (name, url) in enumerate(websites.items(), 1):
            name_parts = name.split(" -> ")
            if len(name_parts) > 1:
                colored_name = f"{name_parts[0]} -> \033[33m{' -> '.join(name_parts[1:])}\033[0m"
            else:
                colored_name = name
            slow_print(f"{i} - {colored_name} -> \033[94m{url}\033[0m", delay=0.0000001)
        
        try:
            choice = int(input("\nEnter the number of the option you want to choose: "))
            open_website(choice)
            input("Press Enter to continue...")
        except ValueError:
            slow_print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()