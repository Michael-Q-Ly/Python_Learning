# Exercise:
# Gets the user to input the amount of grades they have,
# then asks the user to input each grade. The program
# then averages the grades, shows the average,
# and then displays all grades.
# Make the code moduler (i.e., make inputGrades,
# printGrades, avgGrades, and highLow functions)

def inputGrades(numGrades):                                                         # This function allows the user to input
    grades = []                                                                     # their grades

    for gradeNum in range(1,numGrades+1,1):
        print('Enter grade ', gradeNum, ':') 
        score = float( input() )
        grades.append(score)
    print()
    return grades

def printGrades(numGrades, grades):                                                 # Prints the user grades
    for j in range(0,numGrades,1):
        print(grades[j])

def avgGrades(numGrades, grades):                                                   # Averages user grades
    sum = 0
    for j in range(0,numGrades,1):
        sum += grades[j]
    average =  sum / numGrades
    return average


def highLow(numGrades, grades):                                                     # Sorts the user grades and determines highest
    low = grades[0]                                                                 # and lowest grades
    high = grades[0]
    for j in range(0,numGrades,1):
        temp = grades[j]
        if (low > temp):
            low = temp
        else:
            low = low

        if (high < temp):
            high = temp
        else:
            high = high

    for j in range(0, numGrades-1, 1):                                              # Sorting algorithm
        for k in range(j, numGrades-1, 1):
            temp = grades[j]
            if (grades[j] < grades[k+1]):
                grades[j] = grades[k+1]
                grades[k+1] = temp

    return high, low, grades


# MAIN FUNCTION
numGrades = int( input('Please enter how many grades you have: ') )                 # Prompt user input

grades = inputGrades(numGrades)                                                     # Get user to input grades

print('Here are your grades:')
printGrades(numGrades, grades)

avgGrade = avgGrades(numGrades, grades)                                             # Average user's grades and display them
print('Your grade average is ', avgGrade, '\n')

high, low, sortedGrades = highLow(numGrades, grades)                                # Sort the grades from high to low and display
print('Here are your grades sorted from highest to lowest:')                        # the sorted grades
printGrades(numGrades, sortedGrades)

print('Your highest grade is ', high)                                               # Display highest and lowest grades
print('Your lowest grade is  ', low)