# Name: Mithun Lokanathan
# Roll Number: iitp_aimltn_2602016
# Assignment: Python Loops & Automation - Subjective Question

#common temperature list input
temperatures = list(map(int,input().split(','))) #sample_input = 28, 32, 35, 40, 31, 33, 30

#Task 1: Find Maximum and Minimum
max_temperature,min_temperature = temperatures[0], temperatures[0]
for temperature in temperatures[1:]:
    if temperature > max_temperature:
        max_temperature = temperature
    if temperature < min_temperature:
        min_temperature = temperature
print(f"Highest Temperature: {max_temperature}°C")
print(f"Lowest Temperature: {min_temperature}°C")

#Task 2: Count Hot Days
hot_days_count = 0
for temperature in temperatures:
    if temperature <= 30:
        continue
    else:
        hot_days_count += 1
print(f"Hot Days (>30°C): {hot_days_count}")

#Task 3: Alert System
hot_days_count = 0
for index,temperature in enumerate(temperatures):
    if temperature <= 30:
        continue
    elif temperature >= 40:
        print(f"Hot Days (>30°C): {hot_days_count}")
        print(f"Alert! Extreme temperature 40°C detected on Day {index+1}")
    else:
        hot_days_count += 1


        