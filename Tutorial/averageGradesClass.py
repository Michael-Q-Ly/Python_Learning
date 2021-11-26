"""
Exercise:
    This program should implement classes and methods for  the
    averageGrades.py program.
    Gets the user to input the amount of grades they have,
    then asks the user to input each grade. The program
    then averages the grades, shows the average,
    and then displays all grades.
    Make the code moduler (i.e., make inputGrades,
    printGrades, avgGrades, and highLow functions)
"""

def getNames():                                                     # Get the user's full name
    fName = str( input('Enter the student\'s first name: ') )
    lName = str( input('Enter the student\'s last name: ') )
    return fName, lName


class Students:                                                     # Class for students with grade methods
    def __init__(self,f,l,ng):                                      # Initialize
        self.fName          = f
        self.lName          = l
        self.numGrades      = ng
    def getScores(self):                                            # Allow user to input grades
        self.scores = []
        for j in range(0,self.numGrades,1):
            scores = float( input('What is the score? ') )
            self.scores.append(scores)
        return self.scores
    def avgScores(self):                                            # Average the user's grades
        sum = float(0)
        for j in range(0,self.numGrades,1):
            sum += self.scores[j]
        self.average = float( sum/self.numGrades )
        return self.average
    def highLow(self):                                              # Determine the user's highest
        high    = self.scores[0]                                    # and lowest grades
        low     = self.scores[0]
        for j in range(1,self.numGrades,1):
            if (high < self.scores[j]):
                high = self.scores[j]
            if (low > self.scores[j]):
                low = self.scores[j]
        return high, low
    def sortScores(self):                                           # Sort user's grades from
        for j in range(0,self.numGrades-1,1):                       # highest to lowest
            for k in range(0,self.numGrades-1,1):
                if (self.scores[k] < self.scores[k+1]):
                    tempH = self.scores[k]
                    self.scores[k] = self.scores[k+1]
                    self.scores[k+1] = tempH
        return self.scores
    def printScores(self):                                          # Print the user's grades
        for j in range(0,self.numGrades,1):
            print(self.scores[j])
        

cont = 1                                                            # Flag to continue program


""" Main Program """
while (cont):                                                       # Always run until flag goes low
    fName, lName    = getNames()                                    # Get user's name
    prompt          = 'How many grades does '+ fName + ' ' + lName + ' have? '
    numGrades       = int( input(prompt) )
    myStudent       = Students(fName,lName,numGrades)

    scores      = myStudent.getScores()                             # Get users scores one-by-one
    print(fName + ' ' + lName + '\'s scores:')                      # and store into an array
    myStudent.printScores()

    average     = myStudent.avgScores()                             # Average the user's grades
    print('Average: ', average)

    high,low    = myStudent.highLow()                               # Get the user's highest and lowest grades
    print('Highest grade: ', high)
    print('Lowest grade:  ', low)

    scores = myStudent.sortScores()                                 # Sort the user's scores high to low
    print('Sorted grades:')
    myStudent.printScores()

    cont = int( input('Enter \'0\' to exit...\n') )                 # Ask user if they want to enter another
                                                                    # student by setting a flag

print('Goodbye!\n')                                                 # Exit prompt