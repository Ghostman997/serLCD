import web
#from commands import *
import urllib
import os
from os import listdir
from os import walk
import glob
import serial

def clrScr():
    ser = serial.Serial('/dev/ttyUSB0')
    ser.write('\xFE')
    ser.write('\x01')
    ser.close

def printText(text):
    ser = serial.Serial('/dev/ttyUSB0')
    ser.write(text)
    ser.close

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

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
       song = ' '
       f = glob.glob('./mp3s/*.mp3')
       for fname in f:
            #song += fname
            song += "<p><a href = '/?name=%s'>'%s'</a></p>" % (fname, fname)
            song = song.replace("./mp3s/","")
            song += '\n'
           #referer = web.ctx.env.get('HTTP_REFERER', 'http://10.0.0.113:8080')
            referer = web.ctx.env.get('QUERY_STRING', 'http://10.0.0.113:8080')
           #referer = referer.replace('http://10.0.0.113:8080/?name=', '')
            referer = referer.replace('name=', "")
            referer = urllib.unquote(referer)
            print "referer = %s" % referer
            fname = fname.replace("./mp3s/", "")
            print "fname = %s" % fname
            if fname == referer:
                    #fname = fname.replace("$", "\$")
                    clrScr()
                    #cursorMov(0, 1)
                    printText(fname)
                    os.system('mpg123 "./mp3s/%s"' % fname.replace("$", "\$"))
       return song
      # greeting = "Hello World"
      # return greeting

if __name__ == "__main__":
    app.run()
