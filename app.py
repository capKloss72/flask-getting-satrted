from flask import Flask

app = Flask(__name__)
from views.flashcards import flashcard_views

app.register_blueprint(flashcard_views)
