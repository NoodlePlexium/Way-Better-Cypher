from math import e
import art
import os
import random

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

alphabet = ['/','?',"~",'`',':',';','|','=','+','_','-',')','(','*','&','^','%','$','#','@','!',',',' ', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def cypher(message, shift, seed, direction):
    # encode
    if direction == "e":
        random.seed(seed)
        random.shuffle(alphabet)
        encrypted_list = []
        for i in range(len(message)):
            letter = message[i]
            old_pos = alphabet.index(letter)
            new_pos = (old_pos + shift) % len(alphabet)
            letter = alphabet[new_pos]

            encrypted_list.append(letter)
        print(f"\nEncrypted to: {''.join(encrypted_list)}") 
        
    # decode    
    elif direction == "d":
        decrypted_list = []
        for i in range(len(message)):
            letter = message[i]
            old_pos = alphabet.index(letter)
            new_pos = (old_pos - shift) % len(alphabet)
            letter = alphabet[new_pos]

            decrypted_list.append(letter)
        print(f"\nDecrypted to: {''.join(decrypted_list)}")  
    else:
        print(f"Why can't you follow simple instructions? I said type 'e' to encrypt or type 'd' to decrypt. You decided to write '{direction}'!")     

should_continue = True
while should_continue:
    clearConsole()
    print(art.logo)

    direction = input("Type 'e' to encrypt, type 'd' to decrypt ")
    text = input("\nType your message:\n").lower()
    seed = int(input("Type the code number:\n")) 
    shift = int(str(seed)[0]) + 1 
    cypher(text, shift, seed, direction) 

    cont = input("\nPress 'Enter' to run again, type 'no' to terminate.\n").lower()

    if cont == "no":
        should_continue = False
        print("\nterminating...")
