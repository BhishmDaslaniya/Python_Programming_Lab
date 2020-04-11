'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
import requests

from bs4 import BeautifulSoup

source = requests.get("https://www.nytimes.com").text

def get_title(text):
	n=input(text)
	return str(n)

soup = BeautifulSoup(source, 'lxml')
with open(get_title('What do you want to name the file?'), 'w') as open_file:
	for article in soup.find_all('h2'):
		open_file.write(str(article.text))
		open_file.write('\n')