from flask import *
from markupsafe import escape
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"


@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!p>"


@app.route("/user/<name>", methods=["GET"])
def hello(name):
    return jsonify({"name": f"{name}"})


@app.route("/regist_user", methods=["POST"])
def regist_user():
    json = request.get_json()
    return jsonify({"name":json["name"]})


#===============================================================================
# flaskprojectフォルダ
#   > flask --app api\hello run --port=50001
#   > python api\hello.py

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=50001)


