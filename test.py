from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi() # assumes environment variables are set.

def imageInfo(url):
    result = clarifai_api.tag_image_urls(url)
    return result

def imageTags(url):
    return clarifai_api.tag_image_urls(url)["results"][0]["result"]["tag"]["classes"]

def imageProbs(url):
    return clarifai_api.tag_image_urls(url)["results"][0]["result"]["tag"]["probs"]



#---------------------TESTING--------------------------

#url1 = "http://www.clarifai.com/img/metro-north.jpg"
url1 = "https://static1.squarespace.com/static/5436dcd5e4b05ef245bb78c5/5436e746e4b05fd6079dfcf3/54d9cd14e4b079af934ddbf9/1430947393199/?format=1500w"
#url1 = "http://images.fastcompany.com/upload/happiness_bulldogdrummond.jpg"

print url1
print
print imageInfo(url1)
print
print imageTags(url1)
print
print imageProbs(url1)

