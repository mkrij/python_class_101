divisor: int = int(input('Please provide a positive integer.'))
print('The factors of ' + str(divisor) + " are: ")
for x in range(1, divisor+1):
    if divisor % x == 0:
        print(x)
