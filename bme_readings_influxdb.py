# import all of our modules that we need
import smbus2
import bme280
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
from influxdb import InfluxDBClient

#### CONSTANTS ####
# define port number
port = 1
# define device address as a hexidecimal number
address = 0x76
# define time to sleep between iterations of the loop
delta_time_s = 300

#### INITIALIZE SENSOR
# initialize the bus to for the sensor to communicate with the RPi over
bus = smbus2.SMBus(port)
# calibrate the sensor. Important to do this everytime
calibration_params = bme280.load_calibration_params(bus, address)

# Connect to Influx DB server
client = InfluxDBClient(host='localhost', port=8086, database='weatherDB1')

# create a file object such that we will write data into the file
while True:
    # the sample method will take a single reading and return the data
    data = bme280.sample(bus, address, calibration_params)

    # collect the data from the sensor
    timestamp = data.timestamp
    pressure = data.pressure
    humidity = data.humidity
    temp_F = data.temperature*(9.0/5.0) + 32

    # create the Influx DB data
    influx_data = [
        {
            "measurement": "weather",
            "fields": {
                "temperature": temp_F,
                "pressure": pressure,
                "humidity": humidity
            }
        }
    ]

    # write the data to the DB
    client.write_points(influx_data)

    # sleep for sleep_time seconds
    time.sleep(delta_time_s)


