from urllib.request import Request, urlopen
from bs4 import BeautifulSoup 

url = "https://harvard.bluera.com/harvard/rpv-eng.aspx?lang=eng&amp;redi=1&amp;SelectedIDforPrint=6d494a89410e2736137a302cd473587976a3579fd86c0e59d51f6fbbd5d4d7e1369ce97b850b9f0e5d449221228e54f8&amp;ReportType=2&amp;regl=en-US"
# We can disguise our request
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# gcontext = ssl.SSLContext()
html = urlopen(req).read()


# Create a Beautiful Soup object (lxml is the html parser, don't worry too much about it for now)
soup = BeautifulSoup(html, 'html.parser')
type(soup)


# Get the title of the webpage
title = soup.title
print(title)


result = soup.find("div", {"class":"CommentBlockRow TableContainer"})
print(result.text)


all_links = soup.find_all("a")
for link in all_links:
    print(link)