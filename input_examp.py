#Jayden Williams
#9/19
#input

#ask name
print("What is your name?")
user_name = input()
print("Welcome " + user_name)

#ask age
user_age = input("How old are you? ")
print("You are",user_age,"years old")
try:
    print("you will be",int(user_age)+5,"in 5 years")
except:
    print("that wasn't a number")

    
input()
