import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("index.html", notes=notes)
# index.html file should be under templates folder
#form submit
'''
@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "please submit your the form"
    else:
        name = request.form.get("name")
        return render_template("index.html", name=name)

'''
@app.route("/newyear")
def newyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day ==1
    new_year = True
    return render_template ("index.html", new_year=new_year)

@app.route("/about-us")
def about():
    return render_template("more.html")


@app.route("/more")
def more():
    return render_template ("more.html")

@app.route("/loop")
def loop():
    names = ["mary", "lucky", "mehady", "mahmud", "ranu"]
    return render_template ("loop.html", names=names)

@app.route("/<string:name>")
def hi(name):
    name = name.capitalize()
    return f"Hello, {name}"
