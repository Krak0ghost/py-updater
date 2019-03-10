import os

su = "sudo apt "

def update():
    os.system(su + 'update')

update()
