print("Hello World")
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.tennislive.net/atp/match/emil-ruusuvuori-VS-damir-dzumhur/bratislava-challenger-2019-1/'

# query the website and return the html to the variable page
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable soup
soup = BeautifulSoup(page,'html.parser')
# name_box = soup.find('div',attrs={'class':'price'})
# name = name_box.text.strip()
id = soup.find("div", {"id": "ff_p"})
table_list = id.findAll('table', {'class': 'table_stats_match'})
myTable = table_list[1]
rows = myTable.findChildren('tr')
i = 1
for row in rows:
    if i%2 == 0:
        cells = row.findChildren('td')
        for cell in cells:
            # value = cell.string
            print(cell.get_text())
            print(i)

    i += 1