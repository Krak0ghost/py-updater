#!/usr/bin/python3

import os

su = "sudo apt "
sui = "sudo apt install -y "

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


update()
apt_install()
docker_install()
