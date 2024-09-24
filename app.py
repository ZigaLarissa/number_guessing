import random

# generate a random number between 1 and 100
rand_numb = random.randint(1, 100)

# loop
while True:
    # guess prompt
    guess = input("Guess the number between 1 and 100: ")
    
    # check if the response is valid
    if guess.isalpha() == False:
        guess = int(guess)

        # check if it is not out of bound
        if 1 <= guess <= 100:

            # if the response is big than the generated number
            if guess > rand_numb:
                # print too high
                print('Too High')

            # if the answer is not too high
            elif guess < rand_numb:
                # print too low
                print("Too Low")

            # else
            elif guess == rand_numb:
                #print congratulations
                print("Conglatulations! You guessed the number.")
                print(f"Been {rand_numb} all along!")
                break

        else:
            print("Number out of bound!")


    else:
        # print invalid input
        print("Please enter a valid number")