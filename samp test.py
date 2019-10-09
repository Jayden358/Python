#Bales, Greyson
#Ian Christensen
#Jayden Williams
#Max Virkus
#9/11/19
#Math Program

#Perimeter of a square is done at the bottom of the page.


#1 The Perimeter Of A square


#Bales, Greyson
#perimiter of square

#measure of square analysis
sqr_perm_measure = input(print("What is your measurment? ie feet, meter"))

#length of side length

length_sqr = input("What is the side length of your square")

#equation to put answer into a variable


ans_length_sqr = float(length_sqr) + float(length_sqr) + float(length_sqr) + float(length_sqr)

#the answer and its formated

sqr_perm = str.format(" :{0:15.2f}" , ans_length_sqr)
#the number inside of the ascii art
var_sqr_perm = str.format(" :{0:.3g}" , float(length_sqr))



# print statment taken out...print("The perimeter of the square is" , sqr_perm , m1)


#showing the ascii art of a square with numbers in it


Square =str.format("""
 ___{}____________
|                    |
|                    |
|                    |
|                    |
|                    |
{}         {}
|                    |
|___{}___________|""", var_sqr_perm , var_sqr_perm , var_sqr_perm , var_sqr_perm)


#prints shape and answer
print(Square , sqr_perm , sqr_perm_measure , "is your perimeter")

input()
#2 The Area Of The square In square feet



#area of a square


#side measurement analysis
msr_sqr_side = input(print("What's your measurement? ie feet, meter "))

#side length
sqr_side_length = input(print("What's your side length? "))


#equation and variable for that answer

area_sqr = float(sqr_side_length) * float(sqr_side_length)

#giving answer back formated to 2 decimals

form_area_sqr = str.format(" :{0:15.2f}", area_sqr)

print(form_area_sqr , msr_sqr_side , "squared")




#ascii art of a square for a representative


print("""
 _________
|         |
|         |
|    d    a
|         |
|_________|""")

input()



#3 The Circumference Of An Circle
#Ask For Values of Diameter and Pi
print("Pi value")
num1= input()
print("Diameter value")
num2= input()

print("""
			*  *
   *    r/  *
  * ____/____*
  *     D    *
   *        *
      *  *""")

#4 The Area Of A Triangle
# Ask for values of height and base

print("Base value",)
num1= input()

print("Height value")
num2= input()


print("""
 ./`                                                             
                                   :-//-`                                                           
                                  /. +  --`                                                         
                                `/`  +    -+-                                                       
                               ./`   +      .-.                                                     
                              -:     +        `--`                                                  
                             :-      +          `+:`                                                
                           `/.       +             .-`                                              
                          .+         +               ./-                                            
                         ./          +                 -:-                                          
                        :-           +                   `--                                        
                       /.            +                     `/+`                                     
                     `/`             -                        --`                                   
                     A            `:`                           .C.                                 
                 .+:o              :-- `                           -/o.                             
                 +:++             -`hb   /-                          +:-`                             
                `.                ` ` `::                              :+`                          
               ./                    :                                  `:-`                        
              -:                     +                                     .-.                      
             /-                      +                                       .+:                    
            /..`                     +                                         `--                  
          `/`   .-                   +                                           `-:.               
         ./       -`                 +                                              /:`             
        :-         -`                +                                                .-.           
       /.  `/ /`   `.                +                                                  ./:         
     `/`    .Y      /                +---:-                                               .:-       
    ./      .      `-                +   .:                                                  --`    
   -+--------------::----------------+---:/----------------------------------------------------o+.  
    `````````````````````````````````````````B`::```````````````````````````````````````````````` 

""")


print('''             /|\\
                     / | \\
                    /  |  \\
                   /   |   \\
                  /    |    \\
                 /     |     \\
                /      |      \\
               /       |       \\
              -------------------


''')
             



#equation
eq1= (float(num1) * float(num2))/2

#input num1 and 2

result= eq1
print("Answer")
print(eq1)




#5 Volume Of An cube
cube_volume=(a**3)


print("""
   .+------+
 .' |    .'|
+---+--+'  |
|   |  |   |
|  ,+--+---+
|.'    | a'
+------+'""")


print("""

                                      
                                          
                                                              












""")



#perimiter of square

#measure of analysis

m1 = input(print("What is your measurment? ie feet, meter"))

#length of side length

length_sqr = input(print("What is the side length of your square"))

#answer

ans_length_sqr = float(length_sqr) + float(length_sqr) + float(length_sqr) + float(length_sqr)

#displaying the answer

sqr_perm = str.format(" :{0:15.2f}" , ans_length_sqr)

print("The perimeter of the square is" , sqr_perm , m1)

input()





#area of a square


#side measurement analysis
msr_sqr_side = input(print("What's your measurement? ie feet, meter "))

#side length
sqr_side_length = input(print("What's your side length? "))


#equation

area_sqr = float(sqr_side_length) * float(sqr_side_length)

#giving answer back

form_area_sqr = str.format(" :{0:15.2f}", area_sqr)

print(form_area_sqr , msr_sqr_side , "squared")




input()









input()
