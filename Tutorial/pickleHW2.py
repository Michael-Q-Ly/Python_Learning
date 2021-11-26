import pickle

with open('pickleHWData.pkl', 'rb') as fileRead:
    numStudents = pickle.load(fileRead)
    names       = pickle.load(fileRead)
    grades      = pickle.load(fileRead)
    info        = pickle.load(fileRead)

print('Here is the student roster: ')                                                                   # Display roster to user
for j in names:
    print(j)

exitPrompt = int(0)
while (exitPrompt == 0):
    inputName = str( input('Which student would you like to view? ') )                                  # Ask user for which student to view

    for j in range(0, numStudents, 1):                                                                  # Display student credentials
        if (inputName == names[j]):
            print('Student Name:  ', names[j])
            print('Student Grade: ', grades[j])
    terminate = str( input('Press \'E\' to exit or any other key to continue.\n') )                     # Allow user to stop looking at grades
    if (terminate == 'e' or terminate == 'E'):
        exitPrompt = 1

prompt = 'If you would like to view all records, press \'Y\', else press any other key.\n'              # Ask if the user wants to see all student records


roster = str( input(prompt) )                                                                           # Determine whether to view records or terminate program
if (roster == 'y' or roster == 'Y'):
    for j in info:
            print(j)
else:
    print('Terminating program...')
