import web
#from modules import *
import urllib
import os
from os import listdir
from os import walk
import glob

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
            referer = web.ctx.env.get('HTTP_REFERER', 'http://10.0.0.113:8080')
            referer = referer.replace('http://10.0.0.113:8080/?name=', '')
            referer = urllib.unquote(referer)
            print "referer = %s" % referer
            fname = fname.replace("./mp3s/", "")
            print "fname = %s" % fname
            if fname == referer:
                    os.system('mpg123 "%s"' % fname)
                    break
       return song
      # greeting = "Hello World"
      # return greeting

if __name__ == "__main__":
    app.run()
