# Exercise:
# Gets the user to input the amount of grades they have,
# then asks the user to input each grade. The program
# then averages the grades, shows the average,
# and then displays all grades.


numGrades = int( input('Please enter how many grades you have: ') )             # Prompt user input
grades = []                                                                     # Declare empty array to be filled

for gradeNum in range(1,numGrades+1,1):                                         # Prompt user to fill array with grades
    print('Enter grade ', gradeNum, ':') 
    score = float( input() )
    grades.append(score)
print()


print('Here are your grades:')                                                  # Display grades
for j in range(0,numGrades,1):
    print(grades[j])


sum = 0                                                                         # Initialize sum accumulator
for j in range(0,numGrades,1):                                                  # Sum all the grades, average them, and display them
    sum += grades[j]
average =  sum / numGrades
print('Your grade average is ', average, '\n')


low = grades[0]                                                                 # Initialize high and low grades
high = grades[0]
for j in range(0,numGrades,1):                                                  # Swap low and high grades by stepping through a loop
    temp = grades[j]
    if (low > temp):                                                            # Lowest grade swaps
        low = temp
    else:
        low = low

    if (high < temp):                                                           # Highest grade swaps
        high = temp
    else:
        high = high

print('Your highest grade is ', high)                                           # Display highest and lowest grades
print('Your lowest grade is ', low)


# for j in range(0, numGrades, 1):                                                # Sort the grades from highest to lowest (Solution 1)
#     index = j
#     temp = grades[j]
#     high = grades[j]
#     for k in range(j, numGrades, 1):
#         if (high < grades[k]):
#             high = grades[k]
#             index = k
#     grades[j] = grades[index]
#     grades[index] = temp

for j in range(0, numGrades-1, 1):                                              # Solution 2
    for k in range(j, numGrades-1, 1):
        temp = grades[j]
        if (grades[j] < grades[k+1]):
            grades[j] = grades[k+1]
            grades[k+1] = temp
        

print('Here are your grades sorted from highest to lowest:')                     # Display grades
for j in range(0,numGrades,1):
    print(grades[j])