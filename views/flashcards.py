from flask import Flask, render_template, abort, jsonify, Blueprint
from model import db


def welcome():  # put application's code here
    return render_template("welcome.html", cards=db)


def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(card))
    except IndexError:
        abort(404)


def api_card_list():  # put application's code here
    return jsonify(db)


def api_card_details(index):
    try:
        card = db[index]
        return card
    except IndexError:
        abort(404)
