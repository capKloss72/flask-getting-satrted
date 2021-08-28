from flask import Flask, render_template
from model import db

app = Flask(__name__)


@app.route('/')
def welcome():  # put application's code here
    return render_template("welcome.html", message="Here is a message from the template")


@app.route('/card')
def card_view():
    card = db[1]
    return render_template("card.html", card=card)
