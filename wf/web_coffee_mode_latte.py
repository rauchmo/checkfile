import os
import os.path
import time

if (os.path.isfile("/home/pi/smarthome/cf/coffee_timer.txt") == True):
    exit()
else:
    fobj_out = open("/home/pi/smarthome/cf/coffee_timer.txt", "w")
    tim2 = 1
    fobj_out.write(str(tim2))
    fobj_out.close()
    if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_black.txt") == True):
        exit()
    if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_latte.txt") == True):
        exit()
    if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_cappuccino.txt") == True):
        exit()
    if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_tee.txt") == True):
        exit()
    if (os.path.isfile("/home/pi/smarthome/cf/coffee_mode_kakao.txt") == True):
        exit()
    fobj_out = open("/home/pi/smarthome/cf/coffee_mode_latte.txt", "w")
    fobj_out.close()
    time.sleep(20)
    os.remove('/home/pi/smarthome/cf/coffee_timer.txt')
    fobj_out = open("/home/pi/smarthome/cf/coffee_timer.txt", "w")
    tim = 0
    fobj_out.write(str(tim))
    fobj_out.close()