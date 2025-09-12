from machine import ADC
import time

adc = ADC(28)        # create an ADC object acting on a pin
while (1):
    val = adc.read_u16()  # read a raw analog value in the range 0-65535
    print(val)
    time.sleep(0.01)
#val = adc.read_uv()   # read an analog value in microvolts