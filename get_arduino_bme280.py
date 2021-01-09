import serial
import time

# device = '/dev/ttyACM0' адрес оригинальной Arduino
device = '/dev/ttyUSB0'

try:
    print("Trying...", device)
    arduino = serial.Serial(device, 115200)
except:
    print("failed to connect on", device)

while True:
    time.sleep(0.1)
    data = arduino.readline()
    print(data.decode('utf-8'))
