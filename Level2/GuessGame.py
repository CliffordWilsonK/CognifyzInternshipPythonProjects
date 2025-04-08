import random

num = random.randint(1, 100)

print('Welcome to the Guessing Game')
while True:
    guess = int(input('Enter your guess(1-100): '))
    if guess == num:
        print(f"{guess} is the number, you've guessed correctly")
        break
    elif guess < num:
        print('Too low')
    elif guess > num:
        print('Too high')