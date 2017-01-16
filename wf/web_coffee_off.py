import os
import os.path
import time


if (os.path.isfile("/home/pi/smarthome/cf/coffee_timer.txt") == True):
    os.remove('/home/pi/smarthome/cf/coffee_timer.txt')
if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_black.txt") == True):
    os.remove('/home/pi/smarthome/cf/coffee_mode_black.txt')
if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_latte.txt") == True):
    os.remove('/home/pi/smarthome/cf/coffee_mode_latte.txt')
if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_cappuccino.txt") == True):
    os.remove('/home/pi/smarthome/cf/coffee_mode_cappuccino.txt')
if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_tee.txt") == True):
    os.remove('/home/pi/smarthome/cf/coffee_mode_tee')
if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_kakao.txt") == True):
    os.remove('/home/pi/smarthome/cf/coffee_mode_kakao.txt')