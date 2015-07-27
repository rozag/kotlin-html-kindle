import urllib
import os

urls = []
with open(os.getcwd() + '/sites', 'r') as sites:
	for url in sites:
		urls.append(url)
		
os.chdir(os.getcwd() + '/html-for-book/')
testfile = urllib.URLopener()
for url in urls:
    elts = url.split('/')
    filename = str(urls.index(url)) + '-' + elts[len(elts) - 1].replace('\n', '')
    testfile.retrieve(url, filename)
