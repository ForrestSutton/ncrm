# http://ajax.googleapis.com/ajax/services/search/web?vv=1.0&q=

import urllib
import json

exampleSearch = 'geographic sentimetn analysis!@#$'
encoded = urllib.quote(exampleSearch)

#print encoded

rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?vv=1.0&q='+ encoded).read()

jsonData = json.loads(rawData)
searchResults = jsonData=['responseData']['results']

for er in searchResults:
    title = er['title']
    link  = er['url']
    print title
    print link
    print '''

    '''


        
