
from colorama import Fore
# from anonfile import AnonFile
from anonfile import AnonFile
from pathlib import Path
anon = AnonFile()
import sys
print(Fore.GREEN +"""
░█████╗░███╗░░██╗░█████╗░███╗░░██╗███████╗██╗██╗░░░░░███████╗░██████╗
██╔══██╗████╗░██║██╔══██╗████╗░██║██╔════╝██║██║░░░░░██╔════╝██╔════╝
███████║██╔██╗██║██║░░██║██╔██╗██║█████╗░░██║██║░░░░░█████╗░░╚█████╗░
██╔══██║██║╚████║██║░░██║██║╚████║██╔══╝░░██║██║░░░░░██╔══╝░░░╚═══██╗
██║░░██║██║░╚███║╚█████╔╝██║░╚███║██║░░░░░██║███████╗███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═════╝░

██╗░░░██╗██████╗░██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
██║░░░██║██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░░██║██████╔╝██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
██║░░░██║██╔═══╝░██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝██║░░░░░███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
░╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
                                                 -Terminal1337""")

print(Fore.MAGENTA+'''                            What Do you want to do? \n
                           [1]Upload To Anonfiles \n
                           [2]Download from Anonfiles\n''')


user = input(Fore.RED + "I want to [1/2]: ")

if user == '1':
    pass
    path = input(Fore.RED + "Enter the Path to the file: ")
    up = input(Fore.RED + "Do you want to upload it now? [Y/n]")
    if 'Y' in up:
        pass
    elif 'n'in up:
        print(Fore.BLUE+"Process Terminated by User")
        sys.exit()
    else:
        print(Fore.RED + "Invalid Input,Terminating Program")
        sys.exit()
    upload = anon.upload(path, progressbar=True)
    print(upload.url.geturl())
elif user == "2":
    pass
    target_dir = Path.home().joinpath('Downloads')
    link = input("Enter the link to the file: ")
    filename = anon.download(link, path=target_dir)
    print(filename)
else:
    sys.exit()

