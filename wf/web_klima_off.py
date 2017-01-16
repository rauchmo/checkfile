import os

if (os.path.isfile("/home/pi/smarthome/cf/klima.txt") == True):
    os.remove('/home/pi/smarthome/cf/klima.txt')
else:
    exit()