# -*- coding: utf-8 -*-

import random

word_list = ["speaker","monitor","screen","printer","keyboard","scanner","tablet"]

x = random.randint(0, 6)
word = (word_list[x])
print(word)

len_of_word = len(word)
list_1 = []

for i in range(len_of_word):
    list_1 += "_"
print(list_1)

life = 5
while life != 0:
    guess = input("guess a letter : ").lower()
    
    if guess not in word:
        life -= 1
        print("this letter does not exist in the word")
        
    if guess in list_1:
        life -= 1
        print("you've found this letter before")
        
    for pos in range(len_of_word):
        letter = word[pos]
        if letter == guess:
            list_1[pos] = letter
    
    if "_" not in list_1:
        print("\nGAME OVER, YOU WON")
        print(f"the word was {word.upper()}")
        break
    
    print("your life =",life)
    print()
    
    if life != 0:
        print(" ".join(list_1))
    
if life == 0:
    print("GAME OVER, YOU LOST")
    print(f"the word you had to find was {word.upper()}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    