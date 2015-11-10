import urllib2
import json
key = "AIzaSyAbcq5DqVguTNomXJhuQhLp2ZX_0q4pOXY"
def returnTitles(searchterm):
    """
    Returns titles of books related to search term given
    Params: String searchterm
    """

    url = "https://www.googleapis.com/books/v1/volumes?q=" + searchterm + "&key=" + key
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)

    for i in r['items']:
        print i['volumeInfo']['title']
    
#Testing
returnTitles("Happiness")
