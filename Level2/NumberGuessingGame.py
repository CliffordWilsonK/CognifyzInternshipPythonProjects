import random

print('Welcome to the Number Guessing Game!')
minimum = int(input('Enter the Min element of your range: \n'))
maximum = int(input('Enter the Max element of your range: \n'))

num = random.randint(minimum, maximum)

while True:
    guess = int(input('Enter your guess: '))
    if guess == num:
        print(f"{guess} is the number, you've guessed correctly")
        break
    elif guess < num:
        print('Too low')
    elif guess > num:
        print('Too high')