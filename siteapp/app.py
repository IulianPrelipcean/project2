from flask import Flask, session
from siteapp.views.index import bp as index_bp
from siteapp.views.logpage import bp as logpage_bp
from siteapp.views.books import bp as books_bp
from siteapp.views.register import bp as register_bp
from siteapp.views.addbooks import bp as addbooks_bp
from siteapp.views.adminpage import bp as adminpage_bp
from siteapp.views.shop import bp as shop_bp
from siteapp.views.users import bp as users_bp

app = Flask(__name__)

app.secret_key = 'acsd'

app.register_blueprint(index_bp)
app.register_blueprint(logpage_bp)
app.register_blueprint(books_bp)
app.register_blueprint(register_bp)
app.register_blueprint(addbooks_bp)
app.register_blueprint(adminpage_bp)
app.register_blueprint(shop_bp)
app.register_blueprint(users_bp)