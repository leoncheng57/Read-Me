from flask import Flask, render_template, request, redirect, url_for
import getpage

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        imageURL = request.form['imageURL']
        return redirect(url_for("results"))

@app.route("/results")
def results():
    keyword = ""
    #test.py recieves imageURL + returns keyword
    #getpage.py receives keyword + returns book information
    info = returnBooksInfo("title",keyword)
    return render_template("results.html",url=url,info=info)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
