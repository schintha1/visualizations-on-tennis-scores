import urllib2
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from bs4 import BeautifulSoup

#Test URl
# http://www.tennislive.net/atp/match/emil-ruusuvuori-VS-damir-dzumhur/bratislava-challenger-2019-1/
# http://www.tennislive.net/atp/match/alex-de-minaur-VS-denis-shapovalov/davis-cup-finals-qf-aus-can-2019/
# specify the url
quote_page = 'http://www.tennislive.net/atp/match/rafael-nadal-VS-daniil-medvedev/nitto-atp-finals-london-2019/'

# query the website and return the html to the variable page
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable soup
soup = BeautifulSoup(page,'html.parser')

# find the table in html page with score values
id = soup.find("div", {"id": "ff_p"})
table_list = id.findAll('table', {'class': 'table_stats_match'})

#Change format of the points

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

#Initialize plotly graph with rows and columns
fig = go.Figure()
fig = make_subplots(rows=len(table_list), cols=15)
r = 1

#Point graph for Player1
#Point graph for Player2

xPoints = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Score graph for Player1
def p1add_trace(i,r,c):
    fig.update_layout(title='Tennis Live Scores',
    xaxis_title='Serve',yaxis_title='Score')
    fig.add_trace(go.Line(x=xPoints,y=i,line_color = "crimson"),row=r,col=c)
    return fig

#Score graph for Player2
def p2add_trace(i,r,c):
    fig.add_trace(go.Line(x=xPoints,y=i,line_color = "grey"),row=r,col=c)
    fig.update_layout(title='Tennis Live Scores',
    xaxis_title='Serve',yaxis_title='Score')
    return fig


#Iterate through each set played
for j in range(len(table_list)):
    setNumber = j+1
    myTable = table_list[j]
    rows = myTable.findChildren('tr')
    score = []
    point = []
    i=1
    
    #Iterate table to get game scores and Points
    for row in rows:
        if (i==1):
            i = i+1
            continue
        elif i%2 != 0:
            cells = row.findChildren('td')
            for cell in cells:
                score.append(cell.get_text())

        elif i%2 == 0:
            cells = row.findChildren('td')
            for cell in cells:
                point.append(cell.get_text())
        i += 1

    #Get each player scores of a single set
    scoreData  = getIndividualScore(score)
    player1Score = scoreData[0]
    player2Score = scoreData[1]

    c = 1
    # change P- Sometimes inaccurate
    for p in range(len(player1Score)):
        p1add_trace(player1Score[p],r,c)
        p2add_trace(player2Score[p],r,c)
        
        #Increment column for fig    
        c = c+1
    
    #Increment row for fig    
    r = r+1


fig.update_layout(height=800, width=3000, title_text="Tennis Scores")

fig.show()
