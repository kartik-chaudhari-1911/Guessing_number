import random

random_number=random.randint(0,100)
attempts=0

while True:
    attempts+=1
    guess=int(input('Enter the guess:\t'))
    if guess==random_number:
        break
    elif guess < random_number:
        print('To low')
    else:
        print('Too high')

print(f'Good Job! You guessed the number in {attempts} attempts')