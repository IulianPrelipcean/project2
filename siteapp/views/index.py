from flask import Blueprint, render_template, session, redirect, request
from siteapp.config.db_connect import mydb

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/', methods=['POST', 'GET'])
def show():
	if request.method == 'POST':
		if request.form.get('submit'):
			email = request.form.get('email')
			message = request.form.get('message')
			date = request.form.get('date')

			#put the data into the table
			mycursor = mydb.cursor()
			sql = "INSERT INTO contact(email, message, date) VALUES (%s, %s, %s) "
			val = (email, message, date,)
			mycursor.execute(sql,val)
			mydb.commit()

			return redirect('/')

	return render_template('index.html')