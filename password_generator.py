import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation


while True:
    length = int(input("enter length of password:"))
    print("\n1. Just Lower case")
    print("2. lower case and Upper case characters")
    print("3. characters with special character")
    print("4.password with including numbers,characters,special characters")
    
    choice = input("Enter choice: ")

    if choice == "1":
        chars = lower
        

    elif choice == "2":
        chars = upper
        

    elif choice == "3":
        chars = digits

        
    elif choice == "4":
        chars = symbols


    else:
        print("Invalid choice")
password = "".join(random.choice(chars) for _ in range(length))
print(password)