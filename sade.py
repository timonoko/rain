import machine
import neopixel
import time,random

LED_PIN_NUMBER = 13 
LEDS = 16*16  # Change this to the number of LEDs in your strip/ring

pin = machine.Pin(LED_PIN_NUMBER, machine.Pin.OUT)

np = neopixel.NeoPixel(pin, LEDS)

def pix(y,x,c,b=8):
    d=[0,0,0]
    for z in range(3):
        d[z]=int(c[z]*b/255)
    if y%2==1: x=15-x
    if x<16 and y<16 and x>-1 and y>-1:
        np[y*16+x]=d

def getpix(y,x):
    if y%2==1: x=15-x
    if x<16 and y<16 and x>-1 and y>-1:
#        return eval(str(np[y*16+x]))
        return np[y*16+x]
    else:
        return [0,0,0]
    


def kuva(k):
    for x in range(16):
        for y in range(16):
            pix(x,y,k[x][y],6)
    np.write()

def ranc(x):
    return random.randint(0,x)

pix(0,0,[255,0,0])
pix(15,0,[0,255,0])
pix(15,15,[0,0,255])


def doit(n):
  np.fill((0,0,0))
  for m in range(n):
    if ranc(16)>14: pix(ranc(16),0,[ranc(100),ranc(100),ranc(100)],b=ranc(100))
    x = ranc(16)
    for z in range(16):
        y=15-z
        iik=getpix(x,y)
        pix(x,y+1,iik,b=255)
        pix(x,y,[iik[0],iik[1],iik[2]],b=150)
    np.write()


