import random

num = random.randint(1, 100)
guess = int(input('What number do you guess? (1 - 100)'))
score = 10

while guess != num:
    if guess > num:
        print('Your guess is too high!')
        score -= 1
        guess = int(input('What number do you guess? '))
    if guess < num:
        print('Your guess is too low!')
        score -= 1
        guess = int(input('What number do you guess? '))
print('You have successfully guessed the number! Your score is:', score)