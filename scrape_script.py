links =[]
fullinks = ''
import re
from bs4 import BeautifulSoup
import requests
print'------//// Welcome to\ \ \ \ ---------'
print'------oma Cartoon downloader---------- '
print' ----- Download Lnks ------ : \n'
link = raw_input("please enter the link: ")
with requests.get(link) as page:
	soup = BeautifulSoup(page.content, 'html.parser')

menu = soup.find_all(id = 'eyoon-anime-player-episodes')[0]
episodes =  [tag['href'][2:] for tag in menu.find_all('a')]
for i in xrange(len(episodes)):
	with requests.get('https://'+episodes[i]) as page:
		sou = BeautifulSoup(page.content, 'html.parser')
	x = sou.find_all(id = 'eyoon-anime-player-downloads')[0]
	out =  x.find_all('li')[0].find_all('a')[0]['href']
	text = re.search('\/\/(.*)',out).group(0)
	view = re.search('(id\=)(.*)',text).group(2)
	print 'Download : '+str(i)+ " https:"+text
	print 'View     : '+str(i)+ " https://drive.google.com/file/d/"+view +'\n'


'''
x = soup.find_all(id = 'eyoon-anime-player-downloads')[0]
print x.find_all('li')[0].find_all('a')[0]['href']
'''

#eyoon-anime-player-downloads
#eyoon-anime-player-episodes
