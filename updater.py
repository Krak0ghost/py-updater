#!/usr/bin/python3

import os

su = "sudo apt "
sui = "sudo apt install -y "

docker_net = "sudo docker network create --subnet 192.168.0.0/16 --gateway 192.168.0.1 --ip-range=192.168.0.0/24 --driver=bridge bridge5"
docker_repo = 'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"'
docker_pull = "docker pull track2name/ubuntu && docker pull ubuntu"
docker_programs = "sudo apt-get -y install docker-ce docker-ce-cli containerd.io"

echo_meta = "sudo echo 'deb http://apt.metasploit.com/ lucid main' > /etc/apt/sources.list.d/metasploit-framework.list"
key_meta = "sudo wget -O - http://apt.metasploit.com/metasploit-framework.gpg.key | apt-key add -"

wine_repo = "sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ cosmic main' -y"

def update():
    os.system(su + 'update')
    os.system(su + 'upgrade -y')
    os.system(su + 'dist-upgrade -y')

def add_repository():

    os.system('sudo add-apt-repository ppa:webupd8team/y-ppa-manager')
    os.system(su + 'update')
    os.system(sui + 'y-ppa-manager')

def apt_install():
    os.system(sui + 'vim')
    os.system(sui + 'nmap')
    os.system(sui + 'leafpad')
    os.system(sui + 'net-tools')
    os.system(sui + 'ssh')
    os.system(sui + 'ifupdown')
    os.system(sui + 'gnome-tweak-tool')

def docker_install():

    os.system(sui + 'apt-transport-https')
    os.system(sui + 'ca-certificates')
    os.system(sui + 'curl')
    os.system(sui + 'gnupg2 ')
    os.system(sui + 'software-properties-common')

    os.system('curl -fsSL https://download.docker.com/linux/debian/gpg  | sudo apt-key add -')
    os.system('sudo apt-key fingerprint 0EBFCD88')

    os.system(docker_repo)

    os.system(su + 'update')
    os.system(su + 'docker-ce docker-ce-cli containerd.io')

    os.system(docker_net)
    os.system(docker_pull)

def snap_install():

    os.system('sudo snap install atom --classic')


def metasploit_install():

    os.system(echo_meta)
    os.system(key_meta)
    os.system(su + 'update')
    os.system(sui + 'metasploit-framework')


def wine_install():

    os.system(sui + 'wine-stable')

    os.system('sudo dpkg --add-architecture i386')
    os.system('wget -nc https://dl.winehq.org/wine-builds/winehq.key')
    os.system('sudo apt-key add winehq.key')

    os.system(wine_repo)
    os.system(su + 'update')
    os.system(sui + '--install-recommends winehq-stable')

def reboot():
    os.system('sudo reboot now')

update()
add_repository()
apt_install()
snap_install()
metasploit_install()
wine_install()
docker_install()
