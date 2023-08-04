original_temp: float = float(input('What is the temperature you want converted?'))
temp_system: str = str(input('C or F'))
if temp_system == 'C' or temp_system == 'c':
    print('The temperature in Fahrenheit is: ' + str(original_temp * 1.8 + 32.0))
elif temp_system == 'F' or temp_system == 'f':
    print('The temperature in Celsius is: ' + str((original_temp - 32.0)/1.8))
else:
    print('Invalid temperature scale.')