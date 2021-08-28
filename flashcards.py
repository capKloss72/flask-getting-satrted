import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome to my flashcards application!'


@app.route('/page_views')
def get_page_views():  # put application's code here
    global page_views
    page_views = page_views + 1
    return f'This page has been visited: {page_views}'


page_views = 0


@app.route('/date')
def get_date():  # put application's code here
    return f"Welcome to my flashcards application - current date is {datetime.date.today()}"
