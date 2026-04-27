import random
import string

def generate_password(length, use_symbols, use_numbers):
    characters = string.ascii_letters 
    
    
    if use_symbols == "y":
        characters = characters + string.punctuation
        
  
    if use_numbers == "y":
        characters = characters + string.digits


    password = ""
    for i in range(length):
        password = password + random.choice(characters)
    
    return password

print("--- 🔐 Smart Password Generator ---")


length_input = input("How many characters long should the password be? ")
length = int(length_input) # Convert text input to a number

symbols_choice = input("Include symbols? (y/n): ").lower()
numbers_choice = input("Include numbers? (y/n): ").lower()

# password generation
new_password = generate_password(length, symbols_choice, numbers_choice)


print("\nYour Generated Password is:")
print("----------------------------")
print(new_password)
print("----------------------------")