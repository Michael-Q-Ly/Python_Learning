# fruits = [ 'Apple', 'Orange', 'Banana', 'Mango', 'Kiwi']
# print(fruits[0:4])

# fruit = fruits[2]
# print(fruit)

# for fruit in fruits:
#     print(fruit)
#     for letter in fruit:
#         print(letter)
# print('That\'s all, Folks')


# for myNumber in range(10,-1,-1):
#     print(myNumber)
# print('That\'s all, Folks!')


numGrades = int( input('Please enter how many grades you have: ') )             # Prompt user input
grades = []                                                                     # Declare empty array to be filled
sum = 0

for gradeNum in range(1,numGrades+1,1):                                         # Prompt user to fill array with grades
    print('Enter grade ', gradeNum, ':') 
    score = float( input() )
    grades.append(score)

# print('Here are your grades: ', grades)                                          # Display grades

print('Here are your grades:')
for j in range(0,numGrades,1):
    print(grades[j])
