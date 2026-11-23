# IoT Sensor Data Analysis using NumPy
import numpy as np

sensor_data = np.array([22.2, 23.8, 25.0, 26.5, 29.4,
                        31.2, 28.6, 24.9, 27.3, 30.8])

print("Sensor Data:", sensor_data)
print("Mean      :", round(np.mean(sensor_data), 2))
print("Median    :", round(np.median(sensor_data), 2))
print("Minimum   :", np.min(sensor_data))
print("Maximum   :", np.max(sensor_data))
print("Std. Dev. :", round(np.std(sensor_data), 2))

threshold = 28.5
high_values = sensor_data[sensor_data > threshold]
print("Values above", threshold, ":", high_values)
