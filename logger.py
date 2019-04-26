import sys
import Adafruit_DHT
import config
import urllib2

DEBUG = 1
DHT_pin = 4
DHT_sensor = Adafruit_DHT.DHT22

Logging_Delay = 600 # number of seconds between posts

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % THINGSPEAK_API_KEY
print(baseURL)

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_sensor, DHT_pin)
        temperature = (9/5) * temperature + 32
        f = urllib2.urlopen(baseURL +
                            "&field1=%s&field2=%s" % (temperature, humidity))
        print f.read()
        f.close()

        sleep(int(Logging_Delay))
    except:
        print 'Exiting'
        break
    
