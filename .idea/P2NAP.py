import random
guesses = 1


print("Let me guess your number! pick 1-10! If too high enter 2. If too low enter 1. If its correct enter 3!")
low =1
high = 100
last = 1

while(guesses > 0):



    num = random.randint(low,high)


    print("Lets see is it...{}? ".format(num) )
    guess = input()
    guess = int(guess)

    if guess == 2:
        print("Too high ok")
        last = num
        high = num


    if guess == 1:
        print("Ok too low.")
        low = num
        last = num

    if guess == 3:
        print("See, this is why we machines rule!\n\n")
        break

    if guess < 1 or guess > 3:
        print("That's not a valid input!")

    if guess == 1 and num == 100:
        print("Too low? I'm at 100, I suppose I win.")
        break
    if guess == 2 and num == 1:
        print("Too high? I'm at 1, I suppose I win.")
        break


