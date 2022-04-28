#Justin Baldwin
#CTI-110-0901 P5HW1 - Score List
#04/26/2022
#Collecting a set number of scores and then dropping the lowest score to get an average letter grade
#

def displaymenu():
    print('---------------MENU--------------------')
    print('1) Create Score List')
    print('2) Display Results')
    print('3) Exit')
    print('--------------------------------------------')

def MenuChoiceFromUser():
    valdChoice = False
    while valdChoice == False:
        userChoice = input('Enter your choice:  ')
        if userChoice in ['1', '2', '3']:
            valdChoice = True
        else:
            print('Invalid choice entered. Please enter a valid choice')
            displaymenu()
            validChoice = False
    return userChoice

def ValidNumber(number):
    try:
        number = int(number)
        return True
    except ValueError:
        print('Enter a numeric value')
        return False

def ScoreList():
    ScoreList = []
    ValidScoreCount = False
    while ValidScoreCount == False:
        ScoreCount = input('Enter Score Number:  ')
        if ValidNumber(ScoreCount):
            ScoreCount = int(ScoreCount)
            if ScoreCount > 0:
                ValidScoreCount = True
            else:
                print('Invalid Entry. Enter a positive number greater than zero')
                ValidScoreCount = False
        else:
            ValidScoreCount = False
    ValidScore = False
    for i in range(ScoreCount):
        ValidScore = False
        while ValidScore == False:
            Score = input('Enter the #{} score: '.format(i+1))
            if ValidNumber(Score):
                Score = float(Score)
                if (Score >= 0 and Score <=100):
                    ValidScore = True
                    ScoreList.append(Score)
                else:
                    print('Invalid Score Entered. Valid Score is a number between 0 and 100')
                    ValidScore = False
            else:
                ValidScore = False
    return ScoreList

def EvalScoreList(ScoreList):
    LowestScore = float('Inf')
    for Score in ScoreList:
        if Score <= LowestScore:
            LowestScore = Score
    ScoreList.remove(LowestScore)
    AverageScore = sum(ScoreList) / len(ScoreList)
    AverageScore = round(AverageScore, 2)
    GradeLetter = ''
    if AverageScore >= 0 and AverageScore <= 60:
        GradeLetter = 'F'
    elif AverageScore > 60 and AverageScore <= 70:
        GradeLetter = 'D'
    elif AverageScore > 70 and AverageScore <= 80:
        GradeLetter = 'C'
    elif AverageScore > 80 and AverageScore <= 90:
        GradeLetter = 'B'
    elif AverageScore > 90:
        GradeLetter = 'A'    
    return ScoreList, LowestScore, AverageScore, GradeLetter

UserScoreList = []
ExitProgram = False
while (ExitProgram == False):
    displaymenu()
    Choice = MenuChoiceFromUser()
    if Choice == '1':
        UserScoreList = ScoreList()
    elif Choice == '2':
        if len(UserScoreList) > 0:
            ModScoreList, LowScore, AvgScore, GradeLtr = EvalScoreList(UserScoreList)
            print('The score list after removing the lowest score is {} '.format(UserScoreList))
            print('The lowest score entered is:  ', LowScore)
            print('The average of scores entered is:  ', AvgScore)
            print('The grade letter is:  ', GradeLtr)
        else:
            print('No Score Entered. Enter a score to see results.')
    elif Choice == '3':
        print('Goodbye Have A Nice Day!')
        ExitProgram = True



#Function to display initial menu
#Get menu choice from user until a valid choice is entered, which are either 1, 2, or 3
#Loops until valid choice is entered
#Function to check if user entered a number
#ScoreList is created and returned
#Valid number is entered between 0 and 100 which are also included
#Loops until valid score is entered
#Get Scores from user
#Check is score entered is valid number between 0 and 100
#Call ValidNumber() to check if score is valid
#Return ScoreList
#Function to evaluate Score List
#Loop list to get lowest score
#Removes lowest score from list
#Gets average of scores entered
#Rounds Score to 2 decimal places
#Gets letter grade for score
#Return ScoreList, LowestScore, AverageScore and GradeLetter
#Choice from user to either loop program back with different scores or exit program
