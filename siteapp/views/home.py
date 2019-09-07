from flask import Blueprint, render_template

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/home')
def show():
	return render_template('home.html')