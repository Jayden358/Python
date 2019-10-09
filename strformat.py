#Jayden Williams
#9/19
#format examples
#sentence examples
value0 = "Jayden Williams"
value1 = "17"
msg = str.format("{0:10.10} my name is {1:10.10} and I am {2} years old","Hello",value0,value1)
print(msg)

#equation examples
print(str.format("Example 'd': {0:15d}", 1500000))
print(str.format("Example ',': {0:15,}",1500000))
print(str.format("Example 'e': {0:15e}",3.14159))
print(str.format("Example 'f': {0:15.2f}",3.14159))
print(str.format("Example 'g': {0:15g}",3.14159))
#percent
print(str.format("Example '%': {0:15.0%}",0.75))
