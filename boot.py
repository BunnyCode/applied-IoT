import network
import project_secrets
import utime
import machine

Pin = machine.Pin
led = Pin("LED", Pin.OUT)

def blink_sequence():
    utime.sleep(0.3)
    led.value(1)
    utime.sleep(0.3)
    led.value(0)
    utime.sleep(0.5)

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        utime.sleep(1)
        sta_if.connect(project_secrets.SSID, project_secrets.PASSWORD)
        while not sta_if.isconnected():
            print("Attempting to connect.... status is: ", sta_if.isconnected())
            blink_sequence()
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")
do_connect()