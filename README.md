# Read-Me

Were you ever inspired by an image? Did it spark wondrous ideas in your mind?

Now, with "Read-Me", you can select an image and it will help you find books that are related to the image! 

## Team
- Tiffany (Xiuzhen) Lei  
- Sean Chu               
- Leon Cheng            

## APIs Used
- Google Books: https://developers.google.com/books/?hl=en
- Clarifai: https://developer.clarifai.com/docs/

## Instructions to Set Up Clarifai API Python Client
- https://github.com/Clarifai/clarifai-python
<pre>
pip install git+git://github.com/Clarifai/clarifai-python.git
export CLARIFAI_APP_ID="an_application_id_from_your_account"
export CLARIFAI_APP_SECRET="an_application_secret_from_your_account"
</pre>


- Can try these in your terminal to activate authorization:
<br />
export CLARIFAI_APP_ID=e_vr9J23aqXJ343NG5qnpFDjYNz5oWd-Rj69WB8m
<br />
export CLARIFAI_APP_SECRET=mVMHfpOizXEDVaE1kCEshI5gkKEYv7VGhdIXhp5c



## Documentation
- Located in html folder

## Sample Image URLs
- Train: https://upload.wikimedia.org/wikipedia/commons/a/a7/Transperth_Sets.JPG
- Ocean: https://upload.wikimedia.org/wikipedia/commons/e/e0/Clouds_over_the_Atlantic_Ocean.jpg


## TODO
- make everything pretty
- add error handling (ex: bad url input)
