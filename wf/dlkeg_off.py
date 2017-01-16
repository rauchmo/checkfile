import os
import os.path

if (os.path.isfile("/home/pi/smarthome/cf/dlkeg.txt") == True):
    os.remove('/home/pi/smarthome/cf/dlkeg.txt')