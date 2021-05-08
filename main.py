from machine import Pin, Timer, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import framebuf

led = Pin(25, Pin.OUT)
tim = Timer()

WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq=400000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

def tick(timer):
    global led
    led.toggle()

def mi_tick():
    
    global led
    led(1)
    print('1')
    sleep(1)
    led(0)
    print('0')
    sleep(1)

def display_message(msg=":-)"):
    global i2c, oled
    print("scan: " +  str(i2c.scan()))    
    oled.fill(0)
    #oled.text(msg,0,0)
    buffer3 = bytearray(b"\x00\x00\x00\x00\x7F\x80\x01\x98\x7F\x80\x03\xFC\x60\x60\x03\x6C\x60\x60\x03\xFC\x60\x18\x03\xFC\x60\x18\x01\x98\x60\x60\x00\xF0\x60\x60\x00\x60\x7F\x80\x00\x00\x7F\x80\x00\x00\x60\x00\x00\x00\x66\x3C\x0F\x00\x66\x7F\x3F\xC0\x60\x63\x30\xC0\x66\x60\x20\x40\x66\x60\x20\x40\x66\x60\x20\x40\x66\x63\x30\xC0\x66\x7F\x3F\xC0\x06\x3C\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\xFF\xFF\xF8\x00\x00\x00\x00\x3F\xFF\xFF\xF8\x00\x00\x00\x00\x15\x55\x55\x50\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    fb = framebuf.FrameBuffer(buffer3, 32, 32, framebuf.MONO_HLSB)
    oled.blit(fb, 0, 0)
    oled.text(msg,20,30)
    oled.show()


        
print('run')
mi_tick()
display_message("yep")
#
#tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
