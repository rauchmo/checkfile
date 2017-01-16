import os
import os.path
import time

fobj_out = open("/home/pi/smarthome/cf/coffee_timer.txt", "w")
tim2 = 1
fobj_out.write(str(tim2))
fobj_out.close()
os.remove('/home/pi/smarthome/cf/coffee_timer.txt')
fobj_out = open("/home/pi/smarthome/cf/coffee_timer.txt", "w")
tim = 0
fobj_out.write(str(tim))
fobj_out.close()