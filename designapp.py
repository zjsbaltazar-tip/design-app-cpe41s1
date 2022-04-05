# Import dependencies
from flask import Flask
from flask import request
from flask import render_template

"""
NAME: ZEUS JAMES S. BALTAZAR
COURSE: DEVELOPING APPLICATION AND AUTOMATION
DATE PERFORMED: APRIL 04, 2022
"""

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5050)