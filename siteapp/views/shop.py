from flask import Blueprint, render_template, redirect, request, session
from siteapp.config.db_connect import mydb

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/shop', methods=['POST', 'GET'])


def show():


	#take all the query from table personal_books 
	in_shop = 1
	mycursor = mydb.cursor()
	sql = "SELECT * FROM personal_books where in_shop=%s"
	val = (in_shop,)
	mycursor.execute(sql, val)
	result = mycursor.fetchall()

	return render_template('shop.html', result=result)