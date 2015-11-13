from flask import Flask, render_template, request, session, redirect, url_for
import getpage, image

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        session["img_url"] = request.form['img_url']
        return redirect(url_for("results"))

@app.route("/results")
def results():
    #keywords = []
    print session["img_url"]
    keywords = image.get_keywords(session["img_url"])
    print keywords
    #image.py recieves imageURL + returns keyword
    #getpage.py receives keyword + returns book information
    info=""
    #info = getpage.returnBooksInfo("title",keyword)
    return render_template("results.html",keywords=keywords,info=info)
    

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Read-Me"
    app.run(host='0.0.0.0',port=8000)
