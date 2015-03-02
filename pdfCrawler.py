from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from Queue import Queue
import mechanize

def down(id) :
	br.addheaders = [('Referer', 'http://it-ebooks.info/book/' + str(id) + '/')]
	url = ("http://it-ebooks.info/book/" + str(id) + "/")

	soup = bs(urlopen(url).read())
	title = str(soup.html.head.title)[7:-36]
	if title != title.replace('/', '-') :
		title = title.replace('/', '-')
		print "!! replaced to " + title

	As = soup.find_all('a')
	for a in As :
		strLink = str(a.get('href'))
		downLink_index = strLink.find("filepi")
		if downLink_index != -1 :
			print str(id) + " # " + str(title) + " ... "
			br.retrieve(strLink, title + '.pdf')[0]
			print str(id) + " # Done."

br = mechanize.Browser()
br.set_handle_robots(False)

start = 0
end = 5000

for i in xrange(start, end) :
	down(i)