from random import choice as densor
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset=True)




print(Fore.RED+""""
██╗░░░██╗██╗░██████╗░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░░██║██║██╔════╝██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
╚██╗░██╔╝██║╚█████╗░███████║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░╚████╔╝░██║░╚═══██╗██╔══██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░░██║██████╔╝██║░░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                        This Tool For Visa Checker
                     [!] Coded By Mr Densor @6gr8 [!]
""")

ch = input("""
1 - Make Combo [ Visa ]
2 - Check Visa
""")


if ch == "1":
    numofvisa = int('16')
    filesave = 'Densor'+'.txt' # Instead of the name < Densor > you can add the name of your file
    nums = '123456789'
    while True:
        visa =(''.join((densor(nums) for x in range(numofvisa))))
        visacr = '123456789'
        visas = int("1")
        viscr = (''.join((densor(visacr) for i in range(visas))))
        visacr = '2'
        visas = int("2")
        vissadata = ('02'.join((densor(visacr) for s in range(visas))))
        visacvcn = '123456789'
        visacvch = int('3')
        visacvc = (''.join((densor(visacvcn) for d in range(visacvch))))
        print(visa+"|"+viscr+"/"+vissadata+"|"+visacvc)
        with open(f'{filesave}', 'a') as c:
            c.write(visa +"|"+ viscr +"/"+vissadata+"|"+visacvc+'\n')
if ch == "2":
    from HamodyTools import *
    filevisa = input("[+] Enter List Visa :")
    vises = [line.strip() for line in open(f"{filevisa}")]
    for visa2 in vises:
        visa = visa2
        check = Hamody.Visa(visa)
        if check == False:
            print(Fore.RED+"[!] Dead Visa")
        else:
            print(Fore.GREEN+check)
            with open('visa_true.txt', 'a') as c:
                c.write(check+ '\n')