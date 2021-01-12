import os 


def install():
    print("UBUNTU POST-INSTALL SCRIPT")
    print("Updating API")
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')
    print("Installing snapd")
    os.system('sudo apt install snapd')
    os.system('clear')
    print("Installing base packages")
    os.system('sudo apt-get install --yes git git-extras build-essential python3-pip htop glances')
    print('Installing vscode, microsoft teams and discord as snap packages')
    os.system('sudo snap install --classic code')
    os.system('sudo snap install teams-for-linux')
    os.system('sudo snap install discord')

install()