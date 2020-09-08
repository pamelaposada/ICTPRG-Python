print ("Hey there! Let's play a little guessing game. \n"
"Guess the number between 0 and 25")

guesses= 0
guess_log_first = []
#Starting loop
while int(guesses) <= 6: #(7 guesses. Task 1.1)
    guesses = guesses + 1
    
    number = (int(input ("Enter a guess :")))

    #first part guess log list
    for x in range (guesses):
        guess_log_first.append(number)
      
    # conditions
    if (number) > 10:
        print("Nope. It is less than that") 
        #Show the user if their guess is less than the number (Task 1.2) 
    elif (number) < 10 :
        print ("Nope. The number is greater than that") 
        #Show the user if their guess is greater than the number (Task 1.2)
    elif (number) == 10 :
        print ("YOU WIN! The number was indeed 10 \n" 
        "You guessed in" , guesses, "guesses") 
        # show the user the number of guesses when he win (Task 2.1)
        break #Stop loop

if guesses >= 7: #(If the user try 7 times without succed)
        print ("YOU LOSE!\n"
        "You are a fool.The number was 10") 
        #If the user could not guess the number, 
        # call them a fool and show them the number (Task 2.2)

# guess log list second part
guess_log_second = [] 
for i in guess_log_first: 
    if i not in guess_log_second: 
        guess_log_second.append(i) 
   
print ("Your guess log: \n" 
+ str(guess_log_second)) #(Task 3)