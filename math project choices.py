#Bales, Greyson
#Ian Christensen
#Jayden Williams
#Max Virkus
#9/11/19
#Math Program



def perimeter_of_a_square():
    #The 2 variables that you need to perform the maths
    #and to show where the variables are.
    sqr_perm_measure = input("What is your measurent? ie feet, meter")
    length_of_square = input("What is the side length of your square?")
    #making sure things are what they are meant to be.
    if sqr_perm_measure.isalpha():
        try:#changing into a float
            sqr_len_perm = float(length_of_square)
        except:
            print("Invalid imput")
            permimeter_of_a_square()
            #Doing equation on the float
        sqr_perm_ans = sqr_len_perm + sqr_len_perm + sqr_len_perm + sqr_len_perm  
    
            #The ASCII art for the square.
        square_ascii_perm = str.format("""
         _______
        |       |
        |       |
        |      {:0.3g}
        |       |
        |_______|""", sqr_len_perm)
                #printing answer with ASCII art
        print(square_ascii_perm , "The perimeter of the square is", sqr_perm_ans, sqr_perm_measure)
    else:
        print("Invalid input")
        perimeter_of_a_square()
    




def area_of_a_square():
    #area of a square
    area_sqr_side_msr = input("What is your measurement?ie feet, meter     ")
    area_sqr_side_len = input("What is your side length?     ") 
    #checking if number and word
    if area_sqr_side_msr.isalpha():
        try:
            area_sqr_len = float(area_sqr_side_len)
        except:
            print("Invalid input")
            area_of_a_square()
        #all of the math and printing the fun stuff.
        area_sqr_len = area_sqr_len* area_sqr_len
        sqr_side_len = float(area_sqr_side_len)
        # ASCII art
        area_square = str.format("""
___{0:^5.3g}___
|            |
|            |
|    {0:^8.3g}|
|            |
|____________|
""",sqr_side_len)
        print(area_square, "The area of your square is ", area_sqr_len , area_sqr_side_msr , "squared")
    else:
        print("""""")
        print("Sorry invalid input, please try again")
        area_of_a_square()



def circumference_of_circle():
    #Ask For Values of Diameter and Pi
    diameter=input()
    pi =float(3.14)
    Pivalue = diameter*float(3.14)
    input("what is the diameter")
    print("Pivalue")
    print("Diameter value")
    print("""
    			*  *
       *    {:^2.10g}/  *
      * ____/____*
      *     {:^4.10g}    *
       *        *
          *  *""")

def triangle_area():
    print("Base value",)
    num1= input()
    print("Height value")
    num2= input()
    #equation
    eq1= (float(num1) * float(num2))/2
    #input num1 and 2
    result= eq1
    print("Answer")
    print(eq1)
    tri= str.format('''                      /|\\
                         / | \\
                        /  |  \\
                       /   |   \\
                      /    |    \\
                     /     |     \\
                    /      |{}     \\
                   /       |       \\
                  -------------------
                           {}

    ''',num1,num2)
    print(tri)
    input()
















def menu():
    while True:
        
        choice = input("pick an option 1 perimeter of square,2 area of square,3,4,5 or 6 to quit")
        if choice=="1":
            perimeter_of_a_square()
        elif choice == "2":
            area_of_a_square()
        elif choice == "3":
            circumference_of_circle()
        elif choice == "4":
            triangle_area()
        elif choice == "5":
            option5()
        elif choice == "6":
            varify = quit_varify()
            if varify:
                break
        else:
            print("thats not an option")
menu()
input("press enter to exit")
