import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)

inputPins = ['26', '19', '16', '20', '21']

sensorLocations = {
    '26': 'at the front door',
    '19': 'in the kitchen',
    '16': 'by the heater',
    '20': 'by the bedroom door',
    '21': 'overhead'    
}

for pin in inputPins:
    GPIO.setup(int(pin), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
def getTime():
    timeArr = str(datetime.datetime.now()).split(' ')[1].split('.')[0].split(':')
    if int(timeArr[0]) > 12:
        timeArr[0] = str(int(timeArr[0]) - 12)
        amOrPm = 'P.M.'
    else:
        amOrPm = 'A.M.'
    
    currentTime = '{0}:{1}:{2} {3}'.format(timeArr[0], timeArr[1], timeArr[2], amOrPm)
    return currentTime

while True:
    for pin in inputPins:
        if GPIO.input(int(pin)):
            print('{0} - {1}'.format(getTime(), sensorLocations[pin]))
            time.sleep(1)


    
##    if GPIO.input(21):
##        print('Sensor 1: ' + datetime)
##        time.sleep(5)
##    elif GPIO.input(20):
##        print('Sensor 2: ' + datetime)
##        time.sleep(5)
##
##GPIO.cleanup()