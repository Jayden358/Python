#var = "true"
#var = var.title()
#print(type(bool(var))
result = 30 != 25
print(result)

# >
# <
# <=
# >=
# ==
# !=

#if <logical expression>:
#this code executes if the logical expression is true

#get user input and convert it to an integer
#answer = int(input("What is the secret number?"))
#if answer > 5:
#    print(answer,"is greater than 5")

#score = 60
#if(score < 70):
#    print("Try harder!")
    
#elif (score >= 70):
  #  print("That's better!")
    
#elif(score >= 90);
  #  print("You rock!")

#else:
  #  print("I'm always here")    




user_name ="Jayden, bob, tim, steve, trump"
password = "P455w0rd! apple 8834 pancakes 1111"

user = input("Enter your username")
user_pass = input("enter your password")

if user == user_name:
    if user_pass in password:
        print("You're in "+user)
    else:
            print("wrong password")
elif user != user_name:
    print("not a good username")
else:
    print("I don't know how you got here")
