from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
import bluetooth
from periferal import BLESimplePeripheral


ble = bluetooth.BLE()
sp = BLESimplePeripheral(ble)


led = Pin("LED", Pin.OUT)
freq=1000


@asm_pio(set_init=PIO.OUT_LOW)
def square():
    wrap_target()
    set(pins, 1)
    set(pins, 0)
    wrap()



def on_rx(data):
    data=data.decode()
    freq=int(data)
    print(data)
    sm = rp2.StateMachine(0, square,
                            freq=int(2*freq), set_base=Pin(3))
    sm.active(1)




while True:
    if sp.is_connected():  
        sp.on_write(on_rx)
        led.value(1)
    else:
        led.value(0)



    

