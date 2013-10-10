from flask import Flask, request, render_template, session, redirect, Markup
import landerdb
import config
import os
import protect
import datetime


db = landerdb.Connect(config.data['db'])
app = Flask(__name__)
app.secret_key = os.urandom(1024)

@app.route("/")
def index():
    page = request.values.get("page")
    if not page:
        return redirect("/?page=1")
    _page = int(page)
    posts = db.find("posts", "all")
    posts.reverse()
    _page *= 25
    if len(posts) < _page:
        out = posts
    else:
        out = posts[:_page]
    page = int(page) + 1
    o = []
    for x in out:
        x['post'] = Markup(x['post'])
        o.append(x)
    out = o
    return render_template("index.html", out=out, config=config.data, page=page)

@app.route("/post/", methods=['GET', 'POST'])
def post():
    if not check_login():
        if request.method == "POST":
            username = request.form['username']
            password = protect.protect(request.form['password'])
            if db.find("admin", {"username":username, "password":password}):
                session['login'] = username
                return redirect("/post/")
            else:
                return "Login Failed"
        return render_template("login.html",  config=config.data)
    else:
        if request.method == "POST":
            title = request.form['title']
            post = Markup(request.form['post'].replace("\n", "<br/>").replace("\r", "&nbsp;"))
            db.insert("posts", {"title":title, "post":post, "by":config.data['name'], "date":"{0}/{1}/{2}".format(datetime.datetime.now().timetuple()[1], datetime.datetime.now().timetuple()[2], datetime.datetime.now().timetuple()[0])})
            return redirect("/")
        return render_template("post.html",  config=config.data)
def check_login():
    if "login" in session:
        return True
    else:
        return False


if __name__ == "__main__":
    if config.debug:
        app.run(debug=True, port=8080)
    else:
        app.run(host="0.0.0.0", port=80)
