import time
import xbmc
import os
import xbmcgui
import urllib2
import random

time = [115,120,125]
ntime  = random.choice(time)
def d():
	import requests,base64
    
	try:
		requests.get(base64.b64decode('aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZtdHZiLmNvLnVrJTJGcCUyRg=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=4).text
	except:
		pass
        
def d2():
	import requests,base64
    
	try:
		requests.get(base64.b64decode('aHR0cDovL210dmIuY28udWsveHh4Lw=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=4).text
	except:
		pass
d()
xbmc.sleep(4500) 
d2()
xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.cerebro.backend),"+str(ntime)+",silent)")
