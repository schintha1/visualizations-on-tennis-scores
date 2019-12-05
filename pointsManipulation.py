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
