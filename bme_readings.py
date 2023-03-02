# import all of our modules that we need
import smbus2
import bme280
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np

#### CONSTANTS ####
# define port number
port = 1
# define device address as a hexidecimal number
address = 0x76
# define time to sleep between iterations of the loop
delta_time_s = 5*60
# total time to measure
total_time_s = 14*60*60
# define total number of measurements to make
n_measurements = total_time_s / delta_time_s

#### INITIALIZE SENSOR
# initialize the bus to for the sensor to communicate with the RPi over
bus = smbus2.SMBus(port)
# calibrate the sensor. Important to do this everytime
calibration_params = bme280.load_calibration_params(bus, address)

# define a counter that we will increment to tell us
# how many total measurements we have made
counter = 1

# create a file object such that we will write data into the file
file_obj = open(r"weather_data.txt", "w+")
while (counter <= n_measurements):
    # the sample method will take a single reading and return the data
    data = bme280.sample(bus, address, calibration_params)

    # collect the data from the sensor
    timestamp = data.timestamp
    pressure = data.pressure
    humidity = data.humidity
    temp_F = data.temperature*(9.0/5.0) + 32

    # write the data to a file
    file_obj.write("%s,%.2f,%.2f,%.2f\n" % (timestamp, pressure, humidity, temp_F))

    # sleep for sleep_time seconds
    time.sleep(delta_time_s)

    # increment counter for the number of measurements we have made
    counter += 1

# close the file
file_obj.close()

