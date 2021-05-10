import random
real_guess = random.randint(1, 20)

# Store player name
print("Hi, What is your name?")
name = input()
print(f"Hi {name}, Welcome to the Guess Game")

print("You have 7 guesses")
num = 0
for num in range(1, 7):
    print("Take a guess ")
    guess = input()
    if int(guess) > real_guess:
        print("Your guess is high.")
    elif int(guess) < real_guess:
        print("Your guess is low.")
    else:
        print("Congrats, You guessed the number !!")
        break

print(f'{name} !! You guessed the number in {num} guesses')
