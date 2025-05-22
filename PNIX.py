# PNIX - Phone Number Info Xtracter 
# OSINT Tool by Pratham Singhal

import phonenumbers as phn
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from phonenumbers.phonenumberutil import NumberParseException
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code
from phonenumbers.phonenumberutil import PhoneNumberType
from phonenumbers.phonenumberutil import NumberParseException
from colorama import init, Fore, Style
import requests
import numlookupapi

init(autoreset=True)


def banner():
    print(Fore.GREEN + r"""
██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██║╚██╗██╔╝
██████╔╝██╔██╗ ██║██║ ╚███╔╝ 
██╔═══╝ ██║╚██╗██║██║ ██╔██╗ 
██║     ██║ ╚████║██║██╔╝ ██╗
╚═╝     ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
""" + Fore.YELLOW + Style.BRIGHT + """
    📱 P.N.I.X - Phone Number Info Xtracter
    🧪 First-time Development – Model 1.0
""" + Style.DIM + Fore.WHITE + "╔" + "═" * 55 + "╗" + Style.RESET_ALL)
    
    print(
        Fore.CYAN + "║  👨‍💻 Developed By : " + Fore.LIGHTWHITE_EX + "Pratham Singhal".ljust(33) + Fore.CYAN + "║\n" +
        Fore.CYAN + "║  💻 Language     : " + Fore.LIGHTWHITE_EX + "Python".ljust(35) + Fore.CYAN + "║\n" +
        Fore.CYAN + "║  ⚙️  Functions    : " + Fore.LIGHTWHITE_EX + "Track | Trace | Lookup | Extract".ljust(35) + Fore.CYAN + "║\n" +
        Fore.CYAN + "║  🌐 GitHub       : " + Fore.LIGHTWHITE_EX + "github.com/PrathamSinghal001".ljust(35) + Fore.CYAN + "║\n" +
        Fore.CYAN + "║  🔗 LinkedIn     : " + Fore.LIGHTWHITE_EX + "linkedin.com/in/pratham-singhal001/".ljust(35) + Fore.CYAN + "║\n" +
        Fore.CYAN + "║  🧠 License      : " + Fore.LIGHTWHITE_EX + "Open Source (Community Driven)".ljust(35) + Fore.CYAN + "║"
    )

    print(Style.DIM + Fore.WHITE + "╚" + "═" * 55 + "╝")
    print(Fore.YELLOW + "        { ⚡ Powered by the Community ⚡ }\n")

banner()



def PNIX(number):
            
    parsed = phn.parse(number)
    national_no = parsed.national_number
    country_code = parsed.country_code
    region = geocoder.description_for_number(parsed, "en")
    region_code = phn.region_code_for_number(parsed)
    carrier_name = carrier.name_for_number(parsed, "en")
    carrier_vaild = carrier.name_for_valid_number(parsed, "en")
    time_zone = timezone.time_zones_for_number(parsed)
    is_vaild = phn.is_valid_number(parsed)
    is_possible = phn.is_possible_number(parsed)
    format_no = phn.format_number(parsed, phn.PhoneNumberFormat.INTERNATIONAL)
    number_type = phn.number_type(parsed)
     
    type_names = {
        PhoneNumberType.MOBILE: "MOBILE",
        PhoneNumberType.FIXED_LINE: "FIXED_LINE",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "FIXED_LINE_OR_MOBILE",
        PhoneNumberType.TOLL_FREE: "TOLL_FREE",
        PhoneNumberType.PREMIUM_RATE: "PREMIUM_RATE",
        PhoneNumberType.SHARED_COST: "SHARED_COST",
        PhoneNumberType.VOIP: "VOIP",
        PhoneNumberType.PERSONAL_NUMBER: "PERSONAL_NUMBER",
        PhoneNumberType.PAGER: "PAGER",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.VOICEMAIL: "VOICEMAIL",
        PhoneNumberType.UNKNOWN: "UNKNOWN"
    }

    number_type_name = type_names.get(number_type, "UNKNOWN")
    
    
    API = "https://api.numlookupapi.com/v1/validate/number?apikey=num_live_OoqxL0v9iiUF4rk2Y0H2GaoqgyeyFV7bT8oQQxWK"
    response = requests.get(API)
    data = response.json()
    
    client = numlookupapi.Client('num_live_OoqxL0v9iiUF4rk2Y0H2GaoqgyeyFV7bT8oQQxWK')
    location = client.validate('+919993931245')['location']
    
    
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Country Code : " + Fore.LIGHTGREEN_EX + f"+{country_code}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "National Number : " + Fore.LIGHTGREEN_EX + f"{national_no}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Region : " + Fore.LIGHTGREEN_EX + f"{region}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Region Code : " + Fore.LIGHTGREEN_EX + f"{region_code}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Location : " + Fore.LIGHTGREEN_EX + f"{location}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Carrier Name : " + Fore.LIGHTGREEN_EX + f"{carrier_name}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Carrier Vaild : " + Fore.LIGHTGREEN_EX + f"{carrier_vaild}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Time Zone : " + Fore.LIGHTGREEN_EX + f"{time_zone}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Is Vaild : " + Fore.LIGHTGREEN_EX + f"{is_vaild}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Is Possible : " + Fore.LIGHTGREEN_EX + f"{is_possible}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Format Number : " + Fore.LIGHTGREEN_EX + f"{format_no}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Format Number : " + Fore.LIGHTGREEN_EX + f"{format_no}" + Style.RESET_ALL)
    
    
        

    file_name = input("Enter the File name to save Xtract details in txt file : ")
    
    with open (f"{file_name}.txt", "w") as file:
        file.write(f"Phone Number : {number}\n")
        file.write(f"Country Code : {country_code}\n")
        file.write(f"National No.  : {national_no}\n")
        file.write(f"Region Name : {region}\n")
        file.write(f"Region Code : {region_code}\n")
        file.write(f"Carrier Name : {carrier_name}\n")
        file.write(f"Carrier Vaild : {carrier_vaild}\n")
        file.write(f"Time Zone : {time_zone}\n")
        file.write(f"Is Vaild No. : {is_vaild}\n")
        file.write(f"Is Possible No. : {is_possible}\n")
        file.write(f"Format No. : {format_no}\n")
        file.write(f"Number Type No. : {number_type_name}\n")
        file.write(f"Location : {location}\n")



while True:
    number = input("Enter Phone Number (With Country Code (+91)) : ")
    PNIX(number)
    
    cont = input("Do you want to extract details for another number? (Y/N): ")
    if cont.lower() != "y":
        break

