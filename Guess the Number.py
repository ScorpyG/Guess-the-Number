#Justin Hoang, Sep 1st, 2020

#Import files from Python library
from random import randint 
import time

print ("WElCOME TO GUESS THE NUMBER!") #Welcome message 
print ("")

name = input ("Your name: ") # Requesting input from the player

#Set a lowest number and a highest number that the player want to guess
a = input ("Ok! " + name + " Please enter the lowest number you want to start off with: ")
b = input ("\nNext enter the highest number you want to guess with: ")

#Convert both input into integer
lowestNum = int(a)
highestNum = int(b)

#Randomize the solution inside the given range
answer = randint (lowestNum,highestNum) 

print (name,"\nPlease guess from " + a + "-" + b) #Intruction for the player

while True:
    g = input ("Guess the number: ") #Requesting an integer input from the user

    try:
        guess = int(g) #covert input to a number
        time.sleep(0.5) #delay time

        if guess == answer: #A condition if the player's guess matches the solution
            print ("You Win '_' " + name + "\n!Good job!") #Message to the player
            break #Stop the loop

        elif guess > answer: #A condition if the player's guess bigger than the solution
            print ("Too High \nKeep Trying") #Message to the player

        elif guess < answer: #A condition if the player's guess smaller than the solution
            print ("Too Low \nKeep Trying") #Message to the player
          
        print("") #Space

    except:
        print ("Please be sure that your input is an integer") #Message to remind user that the input must be an integer
    
print ("\nGame Over") #final script
