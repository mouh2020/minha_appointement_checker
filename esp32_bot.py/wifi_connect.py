import network
from config import wifi_name,wifi_password

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifi_name,wifi_password)
        while not sta_if.isconnected():
            pass
    print('Conencted successfully.\nNetwork config:', sta_if.ifconfig())
