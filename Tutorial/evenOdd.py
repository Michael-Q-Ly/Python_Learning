# Exercise
# Takes user input and determines if it is odd or even

myNum = float( input('Please enter a number: ') )

oddNum = float( myNum % 2 )

if (oddNum):
    print(myNum, ' is odd!')
else:
    print(myNum, ' is even!')