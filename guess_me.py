import random

num =  random.randint(1,100)

print("WELCOME TO GUESS ME !")
print("I am thinking of a number between 1 and 100")
print("If you're guess is within 10 of the number, I'll tell you you're WARM!")
print("If you're guess is further than 10 away from the number, I'll tell you you're COLD! ")
print("If you're guess is closer to the number than the previous guess, I'll tell you you're WARMER!")
print("If you're guess is farther from the number than the previous guess, I'll tell you you're COLDER! ")
print("LET'S PLAY!")

guesses = [0]

while True:
    guess = int(input("I am thinking of a number between 1 and 100 \n What is your guess?"))

    if guess < 0 or guess > 100 :
        print("OUT OF BOUNDS! Try again:")

        continue 

    # comparing the player's guess to the number

    if guess == num:

        print(f"CONGRATULATIONS, you guessed it after only {len(guesses)} attempts")

        break

    # Adding an incorrect guess to the guesses list

    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:

        if abs(num - guess) < abs(num - guesses[-2]):

             print("WARMER")
       
        else:

            print("COLDER")

    else:

        if abs(num - guess) <= 10:
            print("WARM") 

        else:
            print("COLD")


    