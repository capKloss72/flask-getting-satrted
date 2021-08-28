from app import app
from flask import Flask, render_template, abort, jsonify, Blueprint
from model import db

# app = Flask(__name__)
flashcard_views = Blueprint('flashcard_views', __name__)


@app.route('/')
def welcome():  # put application's code here
    return render_template("welcome.html", cards=db)


@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(card))
    except IndexError:
        abort(404)


@app.route('/api/card')
def api_card_list():  # put application's code here
    return jsonify(db)


@app.route('/api/card/<int:index>')
def api_card_details(index):
    try:
        card = db[index]
        return {"card": card}
    except IndexError:
        abort(404)
