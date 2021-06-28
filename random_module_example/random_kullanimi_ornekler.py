import random

gelen_sayi = random.randint(0, 1) # provides a value of 1 or 0
print(gelen_sayi)
if gelen_sayi == 1:
    print("Heads") 
else:
    print("Tails")