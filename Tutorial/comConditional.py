# Exercise
# Takes user input and determines if it is 
# in the range 5 <= x <= 10

myNum = float( input('Please enter a number: ') )

if (myNum >= 5 and myNum <= 10):
    print(myNum, ' is in the range of 5 and 10')
else:
    print(myNum, ' is NOT in the range of 5 and 10')