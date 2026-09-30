from random import choice
from main import speak
user_score = 0
computer_score = 0

choice_list = ["rock","paper","scissor"]
user_2 = ""
turn = 0
while True:
    user_1 = input(f"{speak("ROCK PAPER SCISSOR")}:")
    if user_1 != user_2 and turn >= 1:
        choice_list = ["rock","paper","scissor"]
    else:
        None
    computer = choice(choice_list)
    print("computer:"+computer)
    
    if user_1 == "rock" :
        choice_list.append("paper")
        if computer == "scissor":
            user_score += 1
        elif computer == "paper":
            computer_score += 1   
        else:
            None

    elif user_1 == "paper":
        choice_list.append("scissor")
        if computer == "rock":           
            user_score += 1
        elif computer == "scissor":
            computer_score += 1 
        else:
            None
    elif user_1 == "scissor":
        choice_list.append("rock")
        if computer == "paper":            
            user_score += 1
        elif computer == "rock":           
            computer_score += 1
        else:           
            None  
    user_2 = user_1
    
    print(str(user_score)+"|"+str(computer_score))
    
    turn += 1
    if user_score == 5:
        speak("YOU WIN")
        break
    if computer_score == 5:
        speak("YOU LOSE")
        break