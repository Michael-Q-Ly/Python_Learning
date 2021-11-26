# Exercise:
# Ask for how many students the user has.
# Have the user enter the student's name and their grade average.
# Store the data into a file.
# Ask the user which student they want to view.
# Display the student's name and info.

import pickle


numStudents     = int( input('How many students do you have? ') )                       # Get number of students fileReadom user

studentName     = []                                                                    # Declare empty arrays to store
studentGrade    = []                                                                    # names and grades

for j in range(0, numStudents, 1):                                                      # Get students' names and grades one-by-one
    name    = str( input('Please enter the student\'s name: ') )
    prompt  = 'Please enter ' + name + '\'s grade: '
    grade   = float( input(prompt) )

    studentName.append( str(name) )                                                     # Store the data into the arrays
    studentGrade.append( float(grade) )
studentInfo = (studentName, studentGrade)


with open('pickleHWData.pkl', 'wb') as fileWrite:                                       # Write credentials into a file
    pickle.dump(numStudents,    fileWrite)
    pickle.dump(studentName,    fileWrite)
    pickle.dump(studentGrade,   fileWrite)
    pickle.dump(studentInfo,    fileWrite)


with open('pickleHWData.pkl', 'rb') as fileRead:                                        # Read fileReadom credentials file
    numStud     = pickle.load(fileRead)
    names       = pickle.load(fileRead)
    grades      = pickle.load(fileRead)
    info        = pickle.load(fileRead)