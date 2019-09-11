from flask import Blueprint, render_template, redirect, request, session
from siteapp.config.db_connect import mydb

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/books')


def show():
	id_primary = int(session['id_user'])
	mycursor = mydb.cursor()
	sql = "SELECT * FROM personal_books where id_user=%s"
	val = (id_primary,)
	mycursor.execute(sql, val)
	result = mycursor.fetchall()

	return render_template('books.html', result=result)
	#return session['id_user']