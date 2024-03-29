from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = "static"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
