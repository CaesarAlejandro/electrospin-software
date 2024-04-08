from machine import Pin as Pn
import esp
import gc
import network 

try: 
    import usocket as uskt
except:
    import socket

esp.osdebug(None)
gc.collect()

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('lab laser 2', '160,Lab.Laser!')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()

pin33 = Pin(33, Pin.OUT)
pin25 = Pin(25, Pin.OUT)
pin34 = Pin(34, Pin.OUT)
pin35 = Pin(35, Pin.OUT)
pin32 = Pin(32, Pin.OUT)
pin14 = Pin(14, Pin.OUT)


