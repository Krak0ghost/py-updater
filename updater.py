#!/usr/bin/python3

import os

su = "sudo apt "
sui = "sudo apt install -y "
docker_net = "sudo docker network create --subnet 192.168.0.0/16 --gateway 192.168.0.1 --ip-range=192.168.0.0/24 --driver=bridge bridge5"

def update():
    os.system(su + 'update')
    os.system(su + 'upgrade -y')
    os.system(su + 'dist-upgrade -y')

def apt_install():
    os.system(sui + 'vim')
    os.system(sui + 'nmap')
    os.system(sui + 'leafpad')
    os.system(sui + 'net-tools')
    os.system(sui + 'ssh')
    os.system(sui + 'keepass2')
    os.system(sui + 'lua5.3')
    os.system(sui + 'gitk')
    os.system(sui + 'gparted')
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

    os.system('sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"')

   os.system(su + 'update')
   os.system(su + 'docker-ce docker-ce-cli containerd.io')

   



update()
apt_install()
docker_install()
