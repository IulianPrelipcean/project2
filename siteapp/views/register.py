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


			return redirect('/logpage')


	return render_template('register.html')