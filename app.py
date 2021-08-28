from flask import Flask
from views.lazy import LazyView

app = Flask(__name__)


def url(import_name, url_rules=[], **options):
    view = LazyView('views.' + import_name)
    for url_rule in url_rules:
        app.add_url_rule(url_rule, view_func=view, **options)


url('flashcards.welcome', ['/'])
url('flashcards.card_view', ['/card/<int:index>'])
url('flashcards.api_card_list', ['/api/card'])
url('flashcards.api_card_details', ['/api/card/<int:index>'])
