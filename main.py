from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/harrypotter/")
def harrypotter():
    return render_template("harrypotter.html")

@app.route("/thewalkingdead/")
def thewalkingdead():
    return render_template("thewalkingdead.html")

@app.route("/onepunchman/")
def onepunchman():
    return render_template("onepunchman.html")

if __name__ == "__main__":
    app.run(debug=True)