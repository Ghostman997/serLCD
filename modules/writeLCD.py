import serial
#ser = serial.Serial('/dev/ttyUSB0')
def clrScr():
    ser = serial.Serial('/dev/ttyUSB0')
    ser.write('\xFE')
    ser.write('\x01')
    ser.close
#def cursorMovx(x):
#    ser = serial.Serial('/dev/ttyUSB0')
#    y = chr(128 + x)
#    ser.write('\xFE')
#    ser.write(y)
#    ser.close
def printText(text):
    ser = serial.Serial('/dev/ttyUSB0')
    ser.write(text)
    ser.close
#def cursorMovy(y):
#    ser = serial.Serial('/dev/ttyUSB0')
#    x = chr(20 * y)
#    ser.write('\xFE')
#    ser.write(x)
#    ser.close

def cursorMov(x,y):
    ser = serial.Serial('/dev/ttyUSB0')
    if y == 0:
        pass
    elif y == 1:
        y = 40
    elif y == 2:
        y = 20
    elif y == 3:
        y = 60
    z = chr((128 + x) +  y)
    ser.write('\xFE')
    ser.write(z)
    ser.close

clrScr()
#cursorMovx(8)
#cursorMovy(2)
cursorMov(0, 1)
printText('lol')

