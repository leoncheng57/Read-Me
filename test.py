from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi() # assumes environment variables are set.

img_url = "http://www.clarifai.com/img/metro-north.jpg"

result = clarifai_api.tag_image_urls(img_url)["results"][0]["result"]["tag"]["classes"]


print result
