import requests
import os
import shutil  # Pour récupérer la taille du terminal

# Vérifie si colorama est installé, sinon l'installe
try:
    from colorama import Fore, Style, init
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, Style, init

# Initialisation de colorama (utile pour Windows)
init(autoreset=True)

# Fonction pour nettoyer l'écran
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows -> cls | Linux/Termux -> clear

# Fonction pour centrer le texte dans le terminal
def center_text(text):
    columns = shutil.get_terminal_size().columns  # Récupère la largeur du terminal
    return text.center(columns)

# Bannière avec "IP-ANALYSER" centré en haut du terminal
def banner():
    clear_screen()  # Nettoie l'écran avant d'afficher la bannière
    print("\n" * 2)  # Ajoute des lignes vides pour placer le texte en haut
    print(Fore.CYAN + center_text("=" * 30))
    print(Fore.YELLOW + center_text("IP-ANALYSER"))
    print(Fore.CYAN + center_text("=" * 30))
    print(Fore.GREEN + center_text("[+] IP-ANALYSER 1.0 -  Permet de voir les infos d'une adresse IP"))
    print(Fore.GREEN + center_text("[+] Créé par : ~𓆩꧁𝕊𝔼ℂ𝕂𒆜𝐋𝐈𝐆𝐇𝐓 𝐘𝐀𝐆𝐀𝐌𝐈꧂𓆪 - THE WORLD OF HACKING"))
    print(Fore.GREEN + center_text("[+] Whatsapp | Telegram  : +224664873993|SECKLIGHTYAGAMI"))
    print(Fore.GREEN + center_text("[+] Chaîne Telegram : " + Fore.BLUE + "https://t.me/theworldofhackingbySkillSensei"))
    print(Fore.GREEN + center_text("[+] GitHub : https://github.com/theworldofhacking/"))
    print(Fore.GREEN + center_text("[+] Dernière mise à jour : Mars 2025"))
    print(Fore.RED + center_text("[!] Utilisation à des fins éducatives uniquement."))
    print(Fore.CYAN + center_text("=" * 50) + "\n")

# Fonction pour récupérer les infos d'une IP
def get_ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'fail':
            print(Fore.RED + f"Erreur : {data['message']}")
            return

        latitude = data['lat']
        longitude = data['lon']
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

        print(Fore.CYAN + "\n[ Informations sur l'adresse IP ]")
        print(Fore.CYAN + "=" * 50)
        print(Fore.YELLOW + f"IP            : {data['query']}")
        print(Fore.YELLOW + f"Pays          : {data['country']} ({data['countryCode']})")
        print(Fore.YELLOW + f"Région        : {data['regionName']}")
        print(Fore.YELLOW + f"Ville         : {data['city']}")
        print(Fore.YELLOW + f"Code postal   : {data['zip']}")
        print(Fore.YELLOW + f"Latitude      : {latitude}")
        print(Fore.YELLOW + f"Longitude     : {longitude}")
        print(Fore.YELLOW + f"FAI           : {data['isp']}")
        print(Fore.YELLOW + f"Organisation  : {data['org']}")
        print(Fore.YELLOW + f"AS            : {data['as']}")
        print(Fore.CYAN + "=" * 50)
        print(Fore.GREEN + "[+] Mettez ce lien dans votre navigateur pour voir la position exacte :")
        print(Fore.BLUE + google_maps_link)
        print(Fore.CYAN + "=" * 50)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Erreur de connexion : {e}")
    except Exception as e:
        print(Fore.RED + f"Une erreur inattendue est survenue : {e}")

# Exécution du script
if __name__ == "__main__":
    banner()
    ip = input(Fore.CYAN + "Entrez l'adresse IP à analyser : " + Fore.YELLOW)
    get_ip_info(ip)
