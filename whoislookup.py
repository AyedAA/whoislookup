import whois
import sys
from colorama import Fore, Style, init
#TLD Limitations:
# Some domain types like `.edu`, `.gov`, and certain country-specific TLDs may not return WHOIS data due to restrictions or different WHOIS servers.
# This tool will show a helpful error message if such domains are unsupported or unavailable.


init(autoreset=True)
def safe_date(date_field):
    if isinstance(date_field, list):
        return date_field[0]
    return date_field

if len(sys.argv)<2:
    print(Fore.RED+"No domain provided ")
    print(Fore.BLUE+"use 'pythone whoispython Domain_Name' ")
    sys.exit()

user_input=sys.argv[1:]

for user_input in sys.argv[1:]:
        if(user_input==""):
            print(Fore.RED+"the domain name is empty,try again!")
        try:
           
            domain = whois.whois(user_input)

            name = domain.domain_name
            if isinstance(name, list):
                name = name[0]

            name = name or "N/A"
            registrar = domain.registrar or "N/A"
            created = safe_date(domain.creation_date) or "N/A"
            expired = safe_date(domain.expiration_date) or "N/A"

            print(Fore.MAGENTA + Style.BRIGHT + f"\n📡 WHOIS Information for: {Fore.GREEN}{user_input}")
            print(Fore.YELLOW + "Domain: ", Fore.CYAN + str(name).lower())
            print(Fore.YELLOW + "Registrar: ", Fore.CYAN + str(registrar))
            print(Fore.YELLOW + "Created on: ", Fore.CYAN + str(created))
            print(Fore.YELLOW + "Expired On: ", Fore.CYAN + str(expired))
            print()

        
        except Exception as e:
            if "No match for" in str(e) or "not found" in str(e).lower():
                print(Fore.RED + f"Domain {user_input} not found or unregistered.\n")
            else:
                print(Fore.RED + f"Failed to retrieve WHOIS info for {user_input}: {e}\n")

        




