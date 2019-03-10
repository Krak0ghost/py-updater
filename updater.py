import os

su = "sudo apt "
sui = "sudo apt install "

def update():
    os.system(su + 'update')
    os.system(su + 'upgrade -y')
    os.system(su + 'dist-upgrade -y')


update()
