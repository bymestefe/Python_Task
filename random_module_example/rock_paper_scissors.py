import random

# rock-paper-scissors (taş-kağıt-makas)
# whoever reaches 3 is winner  (3'e ulaşan kazanır)



def control_of_winner(u,p):
    if u == 0 and p == 1:
        print("winner of this stage is pc")
        return 0
    elif u == 0 and p == 2:
        print("winner of this stage is user")
        return 1
    elif u == 1 and p == 0:
        print("winner of this stage is user")
        return 1
    elif u == 1 and p == 2:
        print("winner of this stage is pc")
        return 0
    elif u == 2 and p == 0:
        print("winner of this stage is pc")
        return 0
    elif u == 2 and p == 1:
        print("winner of this stage is user")
        return 1
    else:
        print("draw")
        return -1


    
score_of_user = 0
score_of_pc = 0      


while True:
    
    choice_of_user = int(input("0 for rock, 1 for paper, 2 for scissors = "))
    
    choice_of_pc = random.randint(0, 2)
    
    winner = control_of_winner(choice_of_user, choice_of_pc)
    
    if winner == 1:
        score_of_user += 1
    elif winner == 0:
        score_of_pc += 1
    else:
        score_of_user += 0
        score_of_pc += 0
    
    
    print("-"*15)
    print(f"Score of pc = {score_of_pc}")
    print(f"Score of user = {score_of_user}")
    
    if score_of_user == 3:
        print("")
        print("USER WON THE GAME")
        break            # if the score reaches 3 the loop will stop
    if score_of_pc == 3:
        print("")
        print("PC WON THE GAME")
        break            # skor 3'e ulaşırsa döngü duracak






