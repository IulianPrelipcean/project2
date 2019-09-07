from flask import Blueprint, render_template, request, redirect
from siteapp.config.db_connect import mydb

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/register', methods=['POST', 'GET'] )
def show():
	errors = {"fail": ''}
	if request.method == 'POST':
		if request.form.get('register'):
			username = request.form.get('username')
			password = request.form.get('password')

			# put data in the table <credentials>
			mycursor = mydb.cursor()
			sql = "INSERT INTO credentials (username, password) VALUES(%s, %s)"
			val = (username, password)
			mycursor.execute(sql,val)
			mydb.commit()

			# take the user id
			sql = "SELECT * FROM credentials WHERE username=%s AND password=%s"
			val = (username, password)
			mycursor.execute(sql,val)
			result = mycursor.fetchall()
			id_user = result[0][0]

			# make the table for the users
			name = 'personal_books'+str(id_user)
			sql = "CREATE TABLE " + name + """(id INT AUTO_INCREMENT PRIMARY KEY, book_name varchar(255), author varchar(255), nr_page INT , review varchar(255))"""
			mycursor.execute(sql)


			return redirect('/logpage')


	return render_template('register.html')