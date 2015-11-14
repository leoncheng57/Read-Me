import urllib2
import json

key = "AIzaSyAbcq5DqVguTNomXJhuQhLp2ZX_0q4pOXY"
def get_info(infoItem,searchterm):
    """
    Returns specified information for books related to search term given
    Params: String infoItem (ex.: "title"), String searchterm
    """
    info = ""
    url = "https://www.googleapis.com/books/v1/volumes?q=" + searchterm + "&key=" + key
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    for i in r['items']:
        if infoItem == "authors":
            for j in i['volumeInfo'][infoItem]:
                info += "\n" + j
        else:
            info += "\n" + i['volumeInfo'][infoItem]

    return info
    
#Testing
#Example: https://www.googleapis.com/books/v1/volumes?q=%22Happiness%22
#print get_info("title","Happiness")
#print get_info("authors","Happiness")

