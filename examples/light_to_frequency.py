from machine import Pin, PWM, ADC
import time

# Use GPIO16 for the buzzer
buzzer = PWM(Pin(16))

adc = ADC(28)        # create an ADC object acting on a pin
adc_values = []
num_readings = 10

print("Calibrating ADC values...")
for i in range(num_readings):
    val = adc.read_u16()  # Read a raw analog value in the range 0-65535
    adc_values.append(val)
    print(f"Reading {i+1}: {val}")
    time.sleep(0.01)
    
average_val = sum(adc_values) / num_readings
print(f"\nAverage calibrated ADC value: {average_val:.2f}")

# Function to play a tone
def play_tone(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(20000)  # Volume
    time.sleep(duration)
    buzzer.duty_u16(0)

while (1):
    val1 = adc.read_u16() - average_val # read a raw analog value in the range 0-65535
    print(val1)
    if val1 < -30000:
        play_tone(139, 1)
    elif val1 > -30000 and val1 < 0:
        play_tone(247, 1)
    elif val1 > 0 and val1 < 30000:
        play_tone(659, 1)
    else:
        play_tone(740, 1)
        
