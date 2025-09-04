from counterfit_connection import CounterFitConnection
from counterfit_shims_grove import GroveLightSensor
import time

CounterFitConnection.init('127.0.0.1', 5000)

light_sensor = GroveLightSensor(67)

while True:
    light = light_sensor.light
    print('Light level^', light)
    time.sleep(1)