from flask import Flask, render_template, request, session, redirect, url_for
import books, image

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        session["img_url"] = request.form['img_url']
        return redirect(url_for("img_results"))

@app.route("/img_results")
def img_results():
    """
    Displays a page with a list of the keywords that match the image
    """
    keywords = image.get_keywords(session["img_url"])
    session["keywords"] = keywords
    return render_template("img_results.html",keywords=keywords)

@app.route("/match")
def match():
    """
    Displays books that match the top 3 keywords
    Note: keywords are already sorted by highest probability
    """    
    keywords = session["keywords"]
    keywords = [keywords[0],keywords[1],keywords[2]]
    info ={}
    for x in keywords:
        info[x] = books.get_info(x)
    return render_template("match.html", info=info)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Read-Me"
    app.run(host='0.0.0.0',port=8000)
