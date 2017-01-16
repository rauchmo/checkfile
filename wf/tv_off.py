import os
import os.path

if (os.path.isfile("/home/pi/smarthome/cf/tv.txt") == True):
    os.remove('/home/pi/smarthome/cf/tv.txt')