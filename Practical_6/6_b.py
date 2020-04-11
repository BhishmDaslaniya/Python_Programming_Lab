'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
import urllib.request
import lxml
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = urllib.request.urlopen(base_url)
soup = BeautifulSoup(r,'lxml')
 
for heading in soup.find_all('h2'):
    print(heading.get_text())
