# -*- coding: utf-8 -*-

# guess the random number generated between 0-100 and print the number of attempts of the user
# sayıyı tahmin edelim. kullanıcın kaçıncı denemede bulduğunu da yazalım


import random
    
def check_number(x,y):
    if x > y:
        print("HIGH")
        return False
    elif x < y:
        print("LOW")
        return False
    elif x == y:
        print("OK")
        return True
    else:
        return False

user_attemps = 0
target = random.randint(0, 100)

while True:
    entered_number = int(input("please guess the number between 0-100 = "))
    user_attemps += 1
    if check_number(entered_number, target) == True:
        break
    
print("Attemps =",user_attemps)


 