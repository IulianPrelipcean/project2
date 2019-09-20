from flask import Blueprint, render_template, redirect, request, session
from siteapp.config.db_connect import mydb

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/books', methods=['POST', 'GET'])


def show():
	#take all the query from table personal_books 
	id_primary = int(session['id_user'])
	mycursor = mydb.cursor()
	sql = "SELECT * FROM personal_books where id_user=%s"
	val = (id_primary,)
	mycursor.execute(sql, val)
	result = mycursor.fetchall()

	#delete a book
	if request.method == 'POST':
		if request.form.get('delete_book'):

			id_to_delete = request.form.get('id_to_delete')

			#delete a query(book)
			sql = "DELETE FROM personal_books WHERE id=%s"
			val = (id_to_delete,) 
			mycursor.execute(sql, val)
			mydb.commit()

			return redirect('books')

	#add a book to the shop
	if request.method == 'POST':
		if request.form.get('add_to_shop'):
			
			id_to_move = request.form.get('id_to_move')
			shop_val = 1

			sql = "UPDATE personal_books SET in_shop = %s  WHERE id = %s"
			val = (shop_val, id_to_move, ) 
			mycursor.execute(sql, val)
			mydb.commit()

			return redirect('books')



	return render_template('books.html', result=result)
	#return session['id_user']