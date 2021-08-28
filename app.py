from flask import Flask
from views import flashcards
app = Flask(__name__)
# from views.flashcards import flashcard_views

# app.register_blueprint(flashcard_views)
app.add_url_rule('/', view_func=flashcards.welcome)
app.add_url_rule('/card/<int:index>', view_func=flashcards.card_view)
app.add_url_rule('/api/card', view_func=flashcards.api_card_list)
app.add_url_rule('/api/card/<int:index>', view_func=flashcards.api_card_details)