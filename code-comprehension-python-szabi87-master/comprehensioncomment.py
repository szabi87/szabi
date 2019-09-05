import random #import random module

guesses_taken = 0 #assign 0 to guesses_taken variable

print('Hello! What is your name?')# print Hello! What is your name? to console
myName = input()#take an input from user(name)

number = random.randint(1, 20)# make random number between 1 and 19 and save in number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #print the explanation

while guesses_taken < 6: #while loop looping until guesses_taken < 6
    print('Take a guess.') # print the introduction
    guess = input() # user input
    guess = int(guess) #convert the input to integer


    guesses_taken += 1 #guess opportunity reduce

    if guess < number:#if guess less than number print Your guess is too low.
        print('Your guess is too low.')

    if guess > number:#if guess bigger than number print Your guess is too low.
        print('Your guess is too high.')

    if guess == number:#if guess equal to number break
        break

if guess == number:#if guess  equal to number, user guessed the number and print the underline
    guesses_taken = str(guesses_taken)
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')

if guess != number:#if guess not equal to number user try till guess_take is 6 and print under
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
