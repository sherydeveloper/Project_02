import random

n = random.randint(1, 100)
a = -1
guess = 0
while(a != n):
    a = int(input("Guess the Number :"))
    if(a < n):
        print("Higher Number Please")
    elif(a > n):
        print("Lower Number Please")
    guess += 1

print(f"You have guessed the number {n} in {guess} guesses")
