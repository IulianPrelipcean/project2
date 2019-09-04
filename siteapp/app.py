from flask import Flask
from siteapp.views.index import bp as index_bp
from siteapp.views.logpage import bp as logpage_bp
from siteapp.views.books import bp as books_bp
from siteapp.views.register import bp as register_bp


app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(logpage_bp)
app.register_blueprint(books_bp)
app.register_blueprint(register_bp)