import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

format_str = '%Y-%m-%d %H:%M:%S'

time_array = np.array([])
pressure_array = np.array([])
humidity_array = np.array([])
temp_array = np.array([])
with open("weather_data.txt") as w_data:
    for line in w_data:
        # read the line
        newline = line.rstrip("\n").split(",")
        
        # extract the data
        time = newline[0]
        pressure = np.float32(newline[1])
        humidity = np.float32(newline[2])
        temp = np.float32(newline[3])

        # strip off all the characters that won't 
        # become a valid datwtime object
        time, sep, trash = time.partition('.')

        # convert time to datetime obj
        time = datetime.strptime(time, format_str).timestamp()

        time_array = np.append(time_array, time)
        pressure_array = np.append(pressure_array, pressure)
        humidity_array = np.append(humidity_array, humidity)
        temp_array = np.append(temp_array, temp)


plot_type = 'pressure'

if (plot_type == 'temp'):
    quantity = temp_array
    ylabel = 'Temp (F)'
    title = 'Temperature vs. Time'
elif (plot_type == 'pressure'):
    quantity = pressure_array
    ylabel = 'Pressure (??)'
    title = 'Pressure vs. Time'
elif (plot_type == 'humidity'):
    quantity = humidity_array
    ylabel = 'Humidity (%)'
    title = 'Humidity vs. Time'


plt.plot((time_array-time_array[0])/3600, quantity)
plt.title(title)
plt.xlabel('Time (hr)')
plt.ylabel(ylabel)
#plt.ylim(60.0, 70.0)
plt.show()
