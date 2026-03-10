import numpy as np

data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])

#Task 1 shape of data and mean temperature
print(f"Shape of the temperature data: {np.shape(data)}")
print(f"Mean temperature per station: {np.mean(data, axis=1)}")

#Task 2 readings above 28.0°C and print them as a 1D array.
flattened_temperatures = np.reshape(data,-1)
print(f"Temperature above 28.0°C as 1D array: {flattened_temperatures[flattened_temperatures > 28]}")

#Task 3 Normalize the entire data array to the range [0, 1]
normalized_data = (data - data.min()) / (data.max() - data.min())
print(f"Normalized data: {normalized_data}")
