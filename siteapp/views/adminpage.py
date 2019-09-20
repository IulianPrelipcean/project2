from flask import Blueprint, render_template, request, redirect, session
from siteapp.config.db_connect import mydb


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/adminpage', methods=['POST', 'GET'])

def show():
	#take the stored data
	mycursor = mydb.cursor()
	sql = "SELECT * FROM credentials"
	mycursor.execute(sql)
	result = mycursor.fetchall()

	#checking the form for deleting an user
	if request.method == 'POST':
		if request.form.get('delete'):
			username = request.form.get('username')
			password = request.form.get('password')
			id_to_delete = request.form.get('id_to_delete')

			#delete the query
			sql = "DELETE FROM credentials WHERE id=%s"
			val = (id_to_delete,) 
			mycursor.execute(sql, val)
			mydb.commit()

			#delete the books that corespond to the user
			sql = "DELETE FROM personal_books WHERE id_user=%s"
			val = (id_to_delete,)
			mycursor.execute(sql, val)
			mydb.commit()

			return redirect('adminpage')

	return render_template('adminpage.html', result=result)