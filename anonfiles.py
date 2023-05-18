import os
import sys

from colorama import Fore
from anonfile import AnonFile
from pathlib import Path


def banner():
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



def upload(path):
    upload = anon.upload(path, progressbar=True)
    print(upload.url.geturl())

def download():
    link = input("Enter the link to the file: ")
    try:
        filename = anon.download(link, path=target_dir)
        print("Your file was downloaded to: " + str(Path.home().joinpath('Downloads')) + "/" + str(filename))
        sys.exit(0)
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    anon = AnonFile()
    banner()

    user = input(Fore.RED + "I want to:\n\t[1]Upload To Anonfiles\n\t[2]Download from Anonfiles\n\t[3]Quit Program\n" + "[" + os.getlogin() + "]" + "$ ")
    
    user_succ = False
    while user_succ == False:

        if user == '1':
            path = input(Fore.RED + "Enter the Absolute Path to the file: ")

            if os.path.isfile(path):
                up = input(Fore.RED + "Do you want to upload it now? [Y/n]: ")
                up = up.lower()
                if 'y' in up:
                    upload(path)
                    user_succ = True
                    Fore.RESET
                    sys.exit(0)
                elif 'n' in up:
                    print(Fore.BLUE+"Process Terminated by User...")
                    user_succ = True
                    Fore.RESET
                    sys.exit(0)

                else:
                    print(Fore.RED + "Invalid Input, try again...")

            else:
                print("File does not exists, try again....")

                 
        elif user == "2":
            #try:
            target_dir = Path.home().joinpath('Downloads')
            if os.path.exists(target_dir):
                download()
                
            else:
                try:
                    os.mkdir(Path.home().joinpath('Downloads'))
                    download()
                    
                except PermissionError as e:
                    print("I do not have permission to create a directory at " + str(Path.home().joinpath('Downloads')) + " try again...")
                    Fore.RESET
                    sys.exit(1)
                
        elif user == "3":
            user_succ = True 
            sys.exit(0)
        else:
            print("Invalid choice, try again...")

