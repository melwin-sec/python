import random

secret_number = random.randint(1, 100)

guess_number = int(input("Enter a number: "))

while guess_number != secret_number:
    if guess_number < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess_number = int(input("Enter a number: "))

if secret_number == guess_number:
    print("You guessed the number correctly!")
else:
    print("Sorry, the secret number was:", secret_number)
