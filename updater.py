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

update()
apt_install()
