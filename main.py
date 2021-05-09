from machine import Pin, Timer, I2C, PWM
from ssd1306 import SSD1306_I2C
from time import sleep
import framebuf
import utime

led = Pin(25, Pin.OUT)
bot = Pin(3, Pin.PULL_DOWN)
tim = Timer()

WIDTH = 128
HEIGHT = 64
max_x=49
max_y=38
i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq=400000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
button_black = Pin(2, Pin.IN, Pin.PULL_UP)


def tick(timer):
    global led
    led.toggle()

def display_message(msg=":-)",x=14,y=46):
    global i2c, oled
    print("scan: " +  str(i2c.scan()))    
    oled.fill(0)
    # buffer3 = bytearray(b"\x00\x00\x00\x00\x7F\x80\x01\x98\x7F\x80\x03\xFC\x60\x60\x03\x6C\x60\x60\x03\xFC\x60\x18\x03\xFC\x60\x18\x01\x98\x60\x60\x00\xF0\x60\x60\x00\x60\x7F\x80\x00\x00\x7F\x80\x00\x00\x60\x00\x00\x00\x66\x3C\x0F\x00\x66\x7F\x3F\xC0\x60\x63\x30\xC0\x66\x60\x20\x40\x66\x60\x20\x40\x66\x60\x20\x40\x66\x63\x30\xC0\x66\x7F\x3F\xC0\x06\x3C\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\xFF\xFF\xF8\x00\x00\x00\x00\x3F\xFF\xFF\xF8\x00\x00\x00\x00\x15\x55\x55\x50\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    # fb = framebuf.FrameBuffer(buffer3, 32, 32, framebuf.MONO_HLSB)
    # oled.blit(fb, 0, 0)
    l = len(msg)
    banner = '+--' + str(l * '-') + '--+'
    msg = '|  ' + msg + '  |'
    oled.text(banner,x,y)
    oled.text(msg,x,y+10)
    oled.text(banner,x,y+20)
    #oled.text(banner,50,30)
    oled.show()
    (len(banner),20)

def t_now():
  return {
    'day': str(utime.localtime()[2]),
    'month': str(utime.localtime()[1]),
    'year': str(utime.localtime()[0]),
    'hour': str(utime.localtime()[3]),
    'minute': str(utime.localtime()[4]),
    'second': str(utime.localtime()[5])
  }

def start():
  print('run')
  x = 0
  y = 0
  while True:
      print(str(button_black.value()))
      if (button_black.value() == 0):
          time_now = t_now()        
          d1 = time_now['day'] + "/" + time_now['month'] + "/" + time_now['year']
          d2 = time_now['hour'] + ":" + time_now['minute'] + ":" + time_now['second']
          # print(d)
          for _ in range(3):
            display_message(d1,x,y)
            sleep(0.5)
            display_message(d2,x,y)
            sleep(0.5)

      elif (button_black.value() == 1):
          display_message("click me!",x,y)
      print("x: ",str(x))
      print("y: ",str(y))
      sleep(0.1)
      x += 1
      y += 1
      if ( abs(x) == max_x ):
          x *= -1
      if ( abs(y) == max_y ):
          y *= -1
