#CTI-110
#P2HW2 - Score Avg
#Justin Baldwin
#03/03/2022
#
Score1 = input('Enter first score:')
Score2 = input('Enter second score:')
Score3 = input('Enter third score:')
Score4 = input('Enter fourth score:')
Score5 = input('Enter fifth score:')
Score6 = input('Enter sixth score:')
Score7 = input('Enter seventh score:')

Scores_List = [Score1, Score2, Score3, Score4, Score5, Score6, Score7]

print('--------------Results-----------')
print('Lowest Score :', min(Scores_List))
Scores_List.remove(min(Scores_List))
print('Updated Score List :', Scores_List)
Score_List = [int(item) for item in Scores_List]
average = sum(Score_List) / len(Score_List)
print('Average of Scores:', average)
print('----------------------------------')




