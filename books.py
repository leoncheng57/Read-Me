import urllib2
import json

key = "AIzaSyAbcq5DqVguTNomXJhuQhLp2ZX_0q4pOXY"
def get_info(searchterm):
    """
    Returns specified information for books related to search term given
    Params: String searchterm
    """
    info = ""
    url = "https://www.googleapis.com/books/v1/volumes?q=" + searchterm + "&key=" + key
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)

    overallDict={}
    infoRequested=["authors","description","imageLinks","pageCount"]

    for book in r['items']:
        individualBookInfo={}
        dictKey=""
        if "subtitle" in book['volumeInfo']:
            dictKey = book['volumeInfo']['title']+": "+book['volumeInfo']['subtitle']
        else:
            dictKey = book['volumeInfo']['title']

        for item in infoRequested:
            value = ""
            if item == "authors":
                for author in book['volumeInfo']['authors']:
                    value += author+", "
            elif item == "imageLinks":
                value = book['volumeInfo']['imageLinks']['smallThumbnail']
            elif item in book['volumeInfo']:
                value = book['volumeInfo'][item]
            individualBookInfo[item]=value
                
        overallDict[dictKey]=individualBookInfo

    return overallDict

#Testing
#Example: https://www.googleapis.com/books/v1/volumes?q=%22Happiness%22
print get_info("Happiness")
#print get_info("authors","Happiness")

