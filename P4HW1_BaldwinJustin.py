#CTI-110-0901
#P4HW1 - Score List
#Justin Baldwin
#04/04/2022
#

count = int(input('How many scores do you want to enter? '))

i,mylist=1,[ ]
while(True):
    if(len(mylist)==count):
        break
    print('Enter score #'+str(i)+': ',end=' ')
    score = int(input())
    if(score < 0 or score > 100):
        print('INVALID score entered!!!')
        print('Score should be between 0 and 100')
        print('Please enter score again.')
    else:
        mylist.append(float(score))
        i += 1
mylist.sort()
Lowest_score = mylist[0]
mylist.remove(Lowest_score)
Score_avg = sum(mylist) /len(mylist)
if(Score_avg > 90):
    grade = 'A'
elif(Score_avg >= 80 and Score_avg < 90):
    grade = 'B'
elif(Score_avg >= 70 and Score_avg < 80):
    grade = 'C'
elif(Score_avg >= 60 and Score_avg < 70):
    grade = 'D'
else:
    grade = 'F'

print('---------------Results---------------')
print('Lowest Score: ', Lowest_score)
print('Modified List: ', mylist)
print('Scores Average: ', Score_avg)
print('Grade: ', grade)
print('---------------------------------------')



#pseudocode:

#Initialize the variables

       #asking the user count for scores input()

#infinite while loop running till list initialized is filled while(True):

        #repeated user input input() for scores

        #appending to the list mylist mylist.append()

 #sorting the list using sort function mylist.sort()

#getting lowest score mylist[0]

#removing the lowest score using .remove function  mylist.remove(lowest_score)

#calculating average = sum(mylist)/len(mylist)

#check the grade using if-else-if bloc

#printing the message

#printing the lowest_score,modified_list,average and grade
