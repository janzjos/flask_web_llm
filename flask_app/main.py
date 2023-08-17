from flask import Flask

# app = Flask(
#    __name__, template_folder="/opt/app/templates", static_folder="/opt/app/static"
# )

from flask import Flask, render_template, request, jsonify

# from ice_breaker import ice_break_with

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/")
# def home():
#    return "Web App with Python Flask!!"


@app.route("/about")
def about():
    return "About Python Flask!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=False)
