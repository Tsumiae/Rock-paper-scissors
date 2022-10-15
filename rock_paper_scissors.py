import random

draw = 0
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options: 
        continue

    rn = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    cpu_pick = options[rn]
    print("Cpu chose", cpu_pick + ".")

    if user_input == "rock" and cpu_pick == "scissors":  
        print("You win!!!")
        user_wins += 1
        
     
    if user_input == "paper" and cpu_pick == "rock":   
        print("You win!!!")
        user_wins += 1
        
    
    elif user_input == "scissors" and cpu_pick == "paper":  
        print("You win!!!")
        user_wins += 1

    elif user_input == "rock" and cpu_pick == "rock":  
        print("You draw!!!")
        draw += 1
    
    elif user_input == "paper" and cpu_pick == "paper":  
        print("You draw!!!")
        draw += 1
    
    elif user_input == "scissors" and cpu_pick == "scissors":  
        print("You draw!!!")
        draw += 1
    
    else:
        print("you lost!")
        computer_wins += 1
        
print("you won", user_wins, "times.")
print("the computer won", computer_wins, "times.")
print("you drew", draw, "times.")
print("Goodbye!")
    
