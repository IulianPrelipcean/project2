from flask import Blueprint, render_template, redirect, request, session
from siteapp.config.db_connect import mydb

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/shop', methods=['POST', 'GET'])


def show():

	id_primary = int(session['id_user'])
	#take all the query from table personal_books 
	in_shop = 1
	mycursor = mydb.cursor()
	sql = "SELECT * FROM personal_books INNER JOIN credentials ON personal_books.id_user=credentials.id where in_shop=%s"
	val = (in_shop,)
	mycursor.execute(sql, val)
	result = mycursor.fetchall()

	username = session['user']
	password = session['password']
	if username == 'admin' and password == 'admin':
		admin_page = 1
	else:
		admin_page =0


	if request.method == 'POST':
		if request.form.get('add_to_mybooks'):
			id_to_move = request.form.get('id_to_move')

			sql = "SELECT * FROM personal_books where id=%s"
			val = (id_to_move,)
			mycursor.execute(sql, val)
			result = mycursor.fetchall()

			id_user = id_primary
			in_shop = 0
			book_name = result[0][3]
			author = result[0][4]
			nr_page = result[0][5]
			review = result[0][6]

			sql = "INSERT INTO personal_books(id_user, in_shop, book_name, author, nr_page, review) VALUES (%s,%s,%s, %s, %s, %s) "
			val = (id_user, in_shop, book_name, author, nr_page, review)
			mycursor.execute(sql,val)
			mydb.commit()

			return redirect('shop')


	if request.method == 'POST':
		if request.form.get('delete_book'):
			id_to_delete = request.form.get('id_to_delete')
			shop_val =0

			sql = "UPDATE personal_books SET in_shop = %s  WHERE id = %s"
			val = (shop_val, id_to_delete, ) 
			mycursor.execute(sql, val)
			mydb.commit()

			return redirect('shop')


	return render_template('shop.html', result=result, admin_page=admin_page)