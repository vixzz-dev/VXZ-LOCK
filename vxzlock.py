import requests, bs4, colorama  
from colorama import Fore, Style  

colorama.init()  

print(Fore.RED + """
██╗   ██╗██╗  ██╗███████╗
██║   ██║╚██╗██╔╝╚══███╔╝
██║   ██║ ╚███╔╝   ███╔╝ 
╚██╗ ██╔╝ ██╔██╗  ███╔╝  
 ╚████╔╝ ██╔╝ ██╗███████╗
  ╚═══╝  ╚═╝  ╚═╝╚══════╝
""" + Style.RESET_ALL)  

print(Fore.GREEN + "🔍 VXZ LOCK - Social Media OSINT Tool" + Style.RESET_ALL)  
print(Fore.YELLOW + "📌 Dev: @Ambavixzz | Termux Version" + Style.RESET_ALL)  
print(Fore.RED + "⚠️ Hanya untuk edukasi! Jangan disalahgunakan!" + Style.RESET_ALL)  

username = input(Fore.CYAN + "\n[?] Masukkan Username: " + Style.RESET_ALL)  

# Simulasi hasil  
print(Fore.GREEN + f"\n[+] Akun ditemukan: {username}" + Style.RESET_ALL)  
print(Fore.YELLOW + f"[+] Dibuat pada: 15 Januari 2022" + Style.RESET_ALL)  
print(Fore.BLUE + f"[+] Konten yang disukai: 120+ foto/video" + Style.RESET_ALL)  