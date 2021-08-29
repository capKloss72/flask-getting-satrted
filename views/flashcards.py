from flask import abort, render_template, jsonify, request, redirect, url_for

from model import db, save_db


def welcome():  # put application's code here
    return render_template("welcome.html", cards=db)


def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(card))
    except IndexError:
        abort(404)


def add_card():
    if request.method == "POST":
        card = {"question": request.form['question'],
                "answer": request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for("card_view", index=len(db) - 1))
    else:
        return render_template("add_card.html")


def remove_card(index):
    try:
        if request.method == "GET":
            return render_template("remove_card.html", card=db[index])
        elif request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for("welcome"))
    except IndexError:
        abort(404)


def api_add_card():
    request_data = request.get_json()
    card = {"question": request_data["question"],
            "answer": request_data["answer"]}
    db.append(card)
    save_db()
    return request_data, 201


def api_remove_card():
    request_data = request.get_json()
    card = {"question": request_data["question"],
            "answer": request_data["answer"]}
    if card in db:
        db.remove(card)
        save_db()
    return request_data, 201


def api_card_list():  # put application's code here
    return jsonify(db)


def api_card_details(index):
    try:
        card = db[index]
        return card
    except IndexError:
        abort(404)
