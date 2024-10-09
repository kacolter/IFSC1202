from random import randint
x = randint(1,20)
start = 1
end = 20
name = input("Hello! What is your name? " "")
print("Well," + " " + str(name) + "," + " " +  "I am thinking of a number betweeen" + " " + str(start) + " " + "and" + " " + str(end) + ".")
print("You have 5 guesses." )
for i in range (5):
    number=int(input("Take a guess: "))
    if number > x:
        print("Your guess is too high.")
        continue
    elif number < x:
        print("Your guess is too low.")
        continue
    if number == x:
        print("Good job" + " " + str(name) + "!" + " " + "You guessed my number in" + " " + str(i + 1) + " " + "guesses!")
        break
else:
        print("Nope. The number I was thinking of was" + " " + str(x) + ".")
       
