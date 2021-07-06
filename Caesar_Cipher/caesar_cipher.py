# -*- coding: utf-8 -*-

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]



def caesar(text, shift_number, choice):
    
    output = ""
    
    if choice == "decode":
        shift_number *= -1
    
    for char in text:
        if char in alphabet:
            index_of_letter = alphabet.index(char)
            new_index_of_letter = index_of_letter + shift_number
            new_letter = alphabet[new_index_of_letter]
            output += new_letter
        else:
            output += char
    print("-" * 26)
    print(f"The {choice}d text is {output}")
            




x = "yes"

while(x == "yes"):
    choice = input("please enter 'encode' or 'decode' = ")
    message = input("enter your message = ").lower()
    shift = int(input("enter the shift number = "))
    shift = shift % 26
    caesar(message, shift, choice)
    
    x = input("'yes' for the again = ")
    
    if x != "yes":
        print("GoodBye")
        break;





















