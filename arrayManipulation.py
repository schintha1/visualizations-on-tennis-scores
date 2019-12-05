# Handle character values in score
def modifyCharScore(score):
    if((score.find('A')) != -1):
        score = '50'
    elif((score.find('[BP]')) != -1):
        score = score[:-4]
    elif((score.isdigit()) and (len(score)<4)):
        score = score
    return score

# Change format of the scores
def getIndividualScore(arr):
    player1 = []
    player2 = []
    # Get scores of player1 and player2
    for i in arr:
        score1 = []
        score2 = []
        k = i.split(",")
        for j in k:
            l = j.split("-") 
            score1.append(modifyCharScore(l[0]))
            score2.append(modifyCharScore(l[1]))
        player1.append(score1)
        player2.append(score2)

    # Add winning point to the player score
    if(len(player1) == len(player2)):
        totPoints = len(player1)
    else:
        totPoints = min(len(player1),len(player2))

    for i in range(totPoints):
        if(len(player1[i]) == len(player2[i])):
            totServes = len(player1[i])-1
        else:
            totServes = min(len(player1[i]),len(player2[i]))-1

        if((int(player1[i][totServes]) > int(player2[i][totServes])) and (int(player1[i][totServes]) >= 40)):
            winnerScore = int(player1[i][totServes]) + 10
            player1[i].append(str(winnerScore))
            loserScore = player2[i][totServes]
            player2[i].append(loserScore)

        elif((int(player1[i][totServes]) < int(player2[i][totServes])) and (int(player2[i][totServes]) >= 40)):
            winnerScore = int(player2[i][totServes]) + 10
            player2[i].append(str(winnerScore))
            loserScore = player1[i][totServes]
            player1[i].append(loserScore)

        else:
            pass

    return [player1,player2]



arr = [u'0-0, 15-0, 30-0, 40-0, 40-15', 
       u'0-0, 15-0, 15-15, 30-15, 30-30, 30-40', 
       u'0-0, 0-15, 15-15, 30-15, 40-15', 
       u'0-0, 15-0, 15-15, 30-15, 30-30, 30-40, 40-40, 40-A',
       u'0-0, 15-0, 30-0, 30-15, 40-15', 
       u'0-0, 0-15, 0-30, 0-40', 
       u'0-0, 0-15, 0-30, 15-30, 30-30, 30-40[BP], 40-40, A-40', 
       u'0-0, 0-15, 0-30, 0-40', 
       u'0-0, 15-0, 30-0, 30-15, 40-15', 
       u'0-0, 0-15, 0-30, 0-40', 
       u'0-0, 15-0, 30-0, 30-15, 40-15', 
       u'0-0, 0-15, 0-30, 0-40',
       u'0-0, 0-1, 1-1, 1-2, 2-2, 3-2, 3-3, 3-4, 3-5, 3-6']


output = getIndividualScore(arr)

print((output[0]))
print("          ")
print((output[1]))

