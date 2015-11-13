from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi() # assumes environment variables are set.

def get_data(url):
    """
    Returns the entire dictionary provided by the API about the image
    Params: String url
    """
    result = clarifai_api.tag_image_urls(url)
    return result

def get_keywords(url):
    """
    Returns a list of the keywords that are identified with the image 
    Params: String url
    """
    return clarifai_api.tag_image_urls(url)["results"][0]["result"]["tag"]["classes"]

def get_probs(url):
    """
    Returns a list of the probabilities of correctness of each keyword
    Params: String url
    """
    return clarifai_api.tag_image_urls(url)["results"][0]["result"]["tag"]["probs"]


#######################################
############### TESTING ###############
#######################################

#url1 = "http://www.clarifai.com/img/metro-north.jpg"
#url1 = "https://static1.squarespace.com/static/5436dcd5e4b05ef245bb78c5/5436e746e4b05fd6079dfcf3/54d9cd14e4b079af934ddbf9/1430947393199/?format=1500w"
#url1 = "http://images.fastcompany.com/upload/happiness_bulldogdrummond.jpg"

# print url1
# print
# print get_data(url1)
# print
# print get_keywords(url1)
# print
# print get_probs(url1)

