from flask import Blueprint, render_template, request, redirect, session
from siteapp.config.db_connect import mydb


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/logpage', methods=['POST', 'GET'])



def show():
	errors = {"fail": ''}
	if request.method == 'POST':
		if request.form.get('login'):
			username = request.form.get('username')
			password = request.form.get('password')
			session['user'] = username
			session['password'] = password
			if username == 'admin' and password == 'admin':
				return redirect('adminpage')
			else:
				# select the id for the user in order to use it in the session
				mycursor = mydb.cursor()
				sql = "SELECT * FROM credentials WHERE username=%s AND password=%s"
				val = (username, password)
				mycursor.execute(sql, val)
				myresult = mycursor.fetchall()
				if len(myresult) > 0:
					id_user = myresult[0][0]
					session['id_user'] = str(id_user)
					return redirect('books')
				else:
					errors['fail'] = 'Name or password incorect !'



	return render_template('logpage.html', errors=errors)