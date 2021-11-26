# Exercise:
# Get the amount of grades the user has and then
# have the user input those grades. Display those
# grades back to the user.


numGrades = int( input('How many grades do you have? ') )                   # Ask user for number of grades

j = 0
grades = []
while (j < numGrades):                                                      # Get grades from user
    score = float( input('What is your grade? ') )
    grades.append(score)
    j += 1


print('Here are your grades:')
while (j > 0):
    print(grades[numGrades-j])
    j -= 1
