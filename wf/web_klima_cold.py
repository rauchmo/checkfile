import os

if (os.path.isfile("/home/pi/smarthome/cf/klima.txt") == True):
    os.remove('/home/pi/smarthome/cf/klima.txt')
    fobj_out = open("/home/pi/smarthome/cf/klima.txt","w")
    klimatemp = 20
    fobj_out.write(str(klimatemp))
    fobj_out.close()
else:
    fobj_out = open("/home/pi/smarthome/cf/klima.txt", "w")
    klimatemp = 20
    fobj_out.write(str(klimatemp))
    fobj_out.close()