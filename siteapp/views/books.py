from flask import Blueprint, render_template, redirect, request, session
from siteapp.config.db_connect import mydb

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/books')


def show():
	id_user = 7
	name = 'personal_books'+str(id_user)
	sql = "SELECT * FROM " + name
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result = mycursor.fetchall()

	return render_template('books.html', result=result)
	#return session['number']