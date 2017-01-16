import os
import os.path
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(4, GPIO.OUT) #Deckenlicht Flur EG
GPIO.setup(15, GPIO.OUT) #Deckenlicht Buero EG
GPIO.setup(18, GPIO.OUT) #Deckenlicht Kueche EG
GPIO.setup(14, GPIO.OUT) #Deckenlicht Wohnzimmer EG



GPIO.setup(16, GPIO.OUT) #Deckenlicht Badezimmer ST1
GPIO.setup(20, GPIO.OUT) #Deckenlicht Schlafzimmer ST1
GPIO.setup(12, GPIO.OUT) #Deckenlicht Flur ST1
GPIO.setup(21, GPIO.OUT) #Deckenlicht Schlafzimmer2 ST1
GPIO.setup(17, GPIO.OUT) #Deckenlicht Bibliutek ST1


GPIO.setup(13, GPIO.OUT) #Klimaanlage ganzen Haus
GPIO.setup(27, GPIO.OUT) #Fernseher Wohnzimmer EG
GPIO.setup(6, GPIO.OUT) #Kaffee fertig


GPIO.setup(5, GPIO.IN) #10rer Schalter Pin einschalten


while True:
    if(os.path.isfile("/home/pi/smarthome/cf/dlfeg.txt") == True): #Pruefung Deckenlicht Flur EG
        GPIO.output(4,GPIO.HIGH)
    else:
        GPIO.output(4,GPIO.LOW)
    if(os.path.isfile("/home/pi/smarthome/cf/dlkeg.txt") == True): #Pruefung Deckenlicht Kueche EG
        GPIO.output(18,GPIO.HIGH)
    else:
        GPIO.output(18,GPIO.LOW)
    if(os.path.isfile("/home/pi/smarthome/cf/dlweg.txt") == True): #Pruefung Deckenlicht Wohnzimmer EG
        GPIO.output(14,GPIO.HIGH)
    else:
        GPIO.output(14,GPIO.LOW)
    if (os.path.isfile("/home/pi/smarthome/cf/dlbeg.txt") == True):  # Pruefung Deckenlicht Buero EG
        GPIO.output(15, GPIO.HIGH)
    else:
        GPIO.output(15, GPIO.LOW)






    if(os.path.isfile("/home/pi/smarthome/cf/dlbst1.txt") == True): #Pruefung Deckenlicht Badezimmer ST1
        GPIO.output(16,GPIO.HIGH)
    else:
        GPIO.output(16,GPIO.LOW)
    if(os.path.isfile("/home/pi/smarthome/cf/dlsst1.txt") == True): #Pruefung Deckenlicht Schlafzimmer ST1
        GPIO.output(20,GPIO.HIGH)
    else:
        GPIO.output(20,GPIO.LOW)
    if (os.path.isfile("/home/pi/smarthome/cf/dls2st1.txt") == True):  # Pruefung Deckenlicht Schlafzimmer2 ST1
        GPIO.output(21, GPIO.HIGH)
    else:
        GPIO.output(21, GPIO.LOW)
    if (os.path.isfile("/home/pi/smarthome/cf/dlfst1.txt") == True):  # Pruefung Deckenlicht flur ST1
        GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(12, GPIO.LOW)
    if (os.path.isfile("/home/pi/smarthome/cf/dlbist1.txt") == True):  # Pruefung Deckenlicht Bibli ST1
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)



    if (os.path.isfile("/home/pi/smarthome/cf/tv.txt") == True):  # Pruefung Fernseher Wohnzimmer EG
        GPIO.output(27, GPIO.HIGH)
    else:
        GPIO.output(27, GPIO.LOW)

    if(os.path.isfile("/home/pi/smarthome/cf/klima.txt") == True): #Pruefung Klimaanlage
        GPIO.output(13,GPIO.HIGH)
    else:
        GPIO.output(13,GPIO.LOW)

    if(os.path.isfile("/home/pi/smarthome/cf/coffee_timer.txt") == True): #Pruefung Kaffee
        fobj = open("/home/pi/smarthome/cf/coffee_timer.txt")
        for line in fobj:
            a = (line.rstrip())
            b = int(a)
            fobj_out = open("/home/pi/smarthome/cf/coffee_timer.txt", "w")
            fobj_out.write(str(b))
            fobj_out.close()
            if (b == 0):
                GPIO.output(6, GPIO.HIGH)
            else:
                GPIO.output(6, GPIO.LOW)
        fobj.close()
    else:
        GPIO.output(6, GPIO.LOW)