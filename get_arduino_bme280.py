import serial
import time
import json
import pymysql

"""
Как добавить в крон
1. sudo crontab -e
2. Добавить строку: 
*/10 * * * * sudo /usr/bin/python3 /home/artem/arduino/get_arduino_bme280.py
"""

# device = '/dev/ttyACM0' адрес оригинальной Arduino
device = '/dev/ttyUSB0'

try:
    print("Trying...", device)
    arduino = serial.Serial(device, 115200)
except:
    print("failed to connect on", device)

packet = ""
working = True
while working:
    time.sleep(0.1)
    data = arduino.readline()
    data = data.decode('utf-8')
    packet = packet + data
    print(data)
    if data == "}":
        working = False

print(packet)
arduino_data = json.loads(packet)
print(arduino_data['t'])
print(arduino_data['p'])
print(arduino_data['h'])

con = pymysql.connect(host = 'localhost', user = 'site', password = 'Sql_760165', db = 'meteo_site', autocommit = True)

with con:
    cur = con.cursor()
    sql = "insert INTO sensors_data (type, val) values (1, "+ arduino_data['t']+")"
    cur.execute(sql)
    sql = "insert INTO sensors_data (type, val) values (2, "+ arduino_data['p']+")"
    cur.execute(sql)
    sql = "insert INTO sensors_data (type, val) values (3, "+ arduino_data['h']+")"
    cur.execute(sql)