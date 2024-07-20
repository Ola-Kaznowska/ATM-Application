from time import sleep
import maskpass

print("Welcom to your account")
sleep(1)
print()   


user = input("Select login/L or register/R: ")

sleep(2)

if user == "L":
    sleep(1)
    name = input("Enter name: ")
    sleep(1)
    print()
    
    pwd = maskpass.askpass(prompt="Enter Password: ", mask="*")
    print("processing...")
    sleep(3)
    print()  
    print(f"Welcome {name} to My Account24.us")
    
elif user == "R":
    print("We starting create a account :D! ")
    sleep(2)
    print()
    Name = input("Enter name: ")
    sleep(2)
    print()
    
    password = maskpass.askpass(prompt="Enter Password: ", mask="*")
    print("Processing...")
    sleep(3)
    print()
    print(f"Welcome back {Name} to My Account24.us")
    
    
else:
    print("Something we wrong :(")
    