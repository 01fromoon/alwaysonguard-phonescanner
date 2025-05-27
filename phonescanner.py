import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import init, Style
import time
import os
import sys
import json
from datetime import datetime
from pathlib import Path

init(autoreset=True)

LOG_FILE = "searched_numbers.json"

def save_to_json(number, lang, valid, country, operator):
    log = {
        "number": number,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "lang": lang,
        "valid": valid,
        "country": country,
        "operator": operator
    }
    data = []
    if Path(LOG_FILE).exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception:
                data = []
    data.append(log)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Koyu yeşilden açık yeşile doğru ANSI renk kodları (256 renk desteği olan terminaller için)
GREEN_SHADES = [
    "\033[38;5;22m",  # Dark Green
    "\033[38;5;28m",
    "\033[38;5;34m",
    "\033[38;5;40m",
    "\033[38;5;46m",  # Light Green
]

BANNER_LINES = [
    "   _____  .__                              ________           ________                       .___",
    "  /  _  \\ |  |__  _  _______  ___.__. _____\\_____  \\   ____  /  _____/ __ _______ _______  __| _/",
    " /  /_\\  \\|  |\\ \\/ \\/ /\\__  \\<   |  |/  ___//   |   \\ /    \\/   \\  ___|  |  \\__  \\\\_  __ \\/ __ | ",
    "/    |    \\  |_\\     /  / __ \\\\___  |\\___ \\/    |    \\   |  \\    \\_\\  \\  |  // __ \\|  | \\/ /_/ | ",
    "\\____|__  /____/\\/\\_/  (____  / ____/____  >_______  /___|  /\\______  /____/(____  /__|  \\____ | ",
    "        \\/                  \\/\\/         \\/        \\/     \\/        \\/           \\/           \\/ ",
    "                                                        Phone Information tool / By 01fromoon"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_banner():
    clear()
    for i, line in enumerate(BANNER_LINES):
        shade_index = min(i, len(GREEN_SHADES)-1)
        print(GREEN_SHADES[shade_index] + Style.BRIGHT + line)
        time.sleep(0.07)
    print(Style.RESET_ALL)
    print("\033[1;32m" + "\n\t\t\t\tAlwaysOnGuard Phone Scanner\n")
    time.sleep(0.5)

def language_choice():
    print("\033[1;36m" + "Select language / Dil seçiniz:")
    print("\033[1;32m" + "[1] English")
    print("\033[1;32m" + "[2] Türkçe")
    while True:
        choice = input("\033[1;33m" + "Choice / Seçim: ").strip()
        if choice in ["1", "2"]:
            return "en" if choice == "1" else "tr"
        else:
            print("\033[1;31m" + "Invalid choice! / Geçersiz seçim!")

def get_phone_info(phone_number, lang):
    try:
        parsed = phonenumbers.parse(phone_number)
        valid = phonenumbers.is_valid_number(parsed)
        possible = phonenumbers.is_possible_number(parsed)
        country = geocoder.country_name_for_number(parsed, "tr" if lang == "tr" else "en")
        location = geocoder.description_for_number(parsed, "tr" if lang == "tr" else "en")
        operator = carrier.name_for_number(parsed, "tr" if lang == "tr" else "en")
        tz = timezone.time_zones_for_number(parsed)
        int_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nat_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        e164_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        info = {
            "valid": valid,
            "possible": possible,
            "country": country,
            "location": location,
            "operator": operator,
            "timezone": ', '.join(tz) if tz else "-",
            "international": int_format,
            "national": nat_format,
            "e164": e164_format
        }
        return info
    except Exception as e:
        return {"error": str(e)}

def print_info(info, lang):
    if "error" in info:
        print("\033[1;31m" + ("Hata: " if lang == "tr" else "Error: ") + info["error"])
        return
    green = "\033[1;32m"
    cyan = "\033[1;36m"
    magenta = "\033[1;35m"
    yellow = "\033[1;33m"
    reset = Style.RESET_ALL

    if lang == "tr":
        print(green + f"[✓] Geçerli Numara: {info['valid']}")
        print(cyan + f"[i] Mümkün Numara: {info['possible']}")
        print(magenta + f"[i] Ülke: {info['country']}")
        print(magenta + f"[i] Bölge: {info['location']}")
        print(cyan + f"[i] Operatör: {info['operator']}")
        print(yellow + f"[i] Zaman Dilimi: {info['timezone']}")
        print(green + f"[#] Uluslararası biçim: {info['international']}")
        print(green + f"[#] Ulusal biçim: {info['national']}")
        print(green + f"[#] E.164 biçim: {info['e164']}")
    else:
        print(green + f"[✓] Valid Number: {info['valid']}")
        print(cyan + f"[i] Possible Number: {info['possible']}")
        print(magenta + f"[i] Country: {info['country']}")
        print(magenta + f"[i] Region: {info['location']}")
        print(cyan + f"[i] Operator: {info['operator']}")
        print(yellow + f"[i] Timezone: {info['timezone']}")
        print(green + f"[#] International format: {info['international']}")
        print(green + f"[#] National format: {info['national']}")
        print(green + f"[#] E.164 format: {info['e164']}")

def generate_osint_links(phone_number):
    num = phone_number.replace(" ", "")
    num_wa = num.replace("+", "")
    google = f"https://www.google.com/search?q={num}"
    whatsapp = f"https://wa.me/{num_wa}"
    facebook = f"https://www.facebook.com/search/top/?q={num}"
    instagram = f"https://www.instagram.com/{num_wa}/"
    twitter = f"https://twitter.com/search?q={num}"
    truecaller = f"https://www.truecaller.com/search/global/{num_wa}"
    syncme = f"https://www.sync.me/search/?number={num_wa}"

    return {
        "Google": google,
        "WhatsApp": whatsapp,
        "Facebook": facebook,
        "Instagram": instagram,
        "Twitter": twitter,
        "Truecaller": truecaller,
        "Sync.me": syncme,
    }

def print_osint_links(links, lang):
    print("\033[1;36m" + ("\nOSINT Linkleri:" if lang == "tr" else "\nOSINT Links:"))
    for name, url in links.items():
        print(f"\033[1;33m- {name}: \033[0m{url}")

def main():
    user_lang = language_choice()
    animated_banner()
    if user_lang == "en":
        print("\033[1;32m" + "Welcome to AlwaysOnGuard Phone Scanner!")
        print("\033[1;36m" + "Enter a phone number with country code (e.g. +905xxxxxxxxx, +1xxxxxxxxxx)")
        print("\033[1;33m" + "Press Ctrl+C to exit.")
    else:
        print("\033[1;32m" + "AlwaysOnGuard Phone Scanner'a hoşgeldiniz!")
        print("\033[1;36m" + "Lütfen ülke kodu ile birlikte telefon numarasını girin (örn. +905xxxxxxxxx, +1xxxxxxxxxx)")
        print("\033[1;33m" + "Çıkmak için Ctrl+C'ye basın.")
    while True:
        try:
            phone_number = input("\033[1;34m" + ("> Telefon numarası: " if user_lang == "tr" else "> Phone number: ")).strip()
            if not phone_number:
                continue
            info = get_phone_info(phone_number, user_lang)
            print_info(info, user_lang)
            # OSINT Linklerini göster
            osint_links = generate_osint_links(phone_number)
            print_osint_links(osint_links, user_lang)
            # JSON'a kaydet
            if "error" not in info:
                save_to_json(
                    phone_number,
                    user_lang,
                    info.get("valid", False),
                    info.get("country", ""),
                    info.get("operator", "")
                )
            print()
        except KeyboardInterrupt:
            print("\n\033[1;31m" + ("Çıkılıyor..." if user_lang == "tr" else "Exiting..."))
            time.sleep(1)
            sys.exit()
        except Exception as e:
            print("\033[1;31m" + ("Hata: " if user_lang == "tr" else "Error: ") + str(e))

if __name__ == "__main__":
    main()
