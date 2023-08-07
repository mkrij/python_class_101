list_total: int = int(input('How many numbers would you like to enter?'))
min: int = 1000000
max: int = -1000000
for x in range (0, list_total):
    value: int = int(input('Please provide a number'))
    if value < min:
        min = value
    if value > max:
        max = value
print('Your maximum value is: ' + str(max))
print('Your minimum value is: ' + str(min))