import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome to my flashcards application!'


@app.route('/date')
def get_date():  # put application's code here
    return f'Welcome to my flashcards application - current date is {datetime.date.today()}'
