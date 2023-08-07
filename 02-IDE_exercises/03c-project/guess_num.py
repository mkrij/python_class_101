number_to_guess: int = int(input('Provide a number to be guessed.'))
guess: int = int(input('Guess a number'))
if guess == number_to_guess:
    print('You guessed it in 1 try!')
total_guesses: int = 1
while guess != number_to_guess:
    if guess > number_to_guess:
        total_guesses += 1
        guess: int = int(input('Too high - guess again!'))
    elif guess < number_to_guess:
        total_guesses += 1
        guess: int = int(input('Too low - guess again!'))
print('You guessed it in ' +str(total_guesses) + ' tries!')