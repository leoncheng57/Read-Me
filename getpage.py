import urllib2
import json

def returnTitles(searchterm):
    """
    Returns titles of books related to search term given
    Params: String searchterm
    """

    url = "https://www.googleapis.com/books/v1/volumes?q=" + searchterm
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)

    for i in r['items']:
        print i['volumeInfo']['title']
    
#Testing
returnTitles("Happiness")
