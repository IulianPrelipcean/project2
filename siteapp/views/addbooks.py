from flask import Blueprint, render_template, request, redirect, session
from siteapp.config.db_connect import mydb


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/addbooks', methods=['POST', 'GET'])

def show():
	errors = {"fail": ''}
	if request.method == 'POST':
		if request.form.get('add'):
			book_name = request.form.get('book_name')
			author = request.form.get('author')
			nr_page = request.form.get('nr_page')
			review = request.form.get('review')
			id_user = int(session['id_user'])

			mycursor = mydb.cursor()
			sql = "INSERT INTO personal_books(id_user,book_name, author, nr_page, review) VALUES (%s,%s, %s, %s, %s) "
			val = (id_user,book_name, author, nr_page, review)
			mycursor.execute(sql,val)
			mydb.commit()

			return redirect('books')


	return render_template('addbooks.html', errors=errors)