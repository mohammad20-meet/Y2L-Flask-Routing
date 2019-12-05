from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/store')
def store():
	if request.method == 'POST':
		added_to_cart = Add_to_Cart()
		return render_template("store.html")
	else:
		return render_template("store.html")
@app.route('/cart')
def cart():
	n = query_all()
	return render_template("cart.html", products=n)
	
@app.route('/portal')
def portal():
	query_all()
	add_product()
	edit_product()
	delete_product()


	return render_template("portal.html")

@app.route('/log', methods=['GET', 'POST'])
def log():
	if request.method == 'GET':
		return render_template('log.html')
	else:
		N = request.form['uname']
		o = request.form['psw']
		if N == "Mohammad" or o == "ok":

			return render_template('portal.html',
			uname = N,
			psw = o)
		else:
			return render_template('log.html')


##### Code here ######



#####################


if __name__ == '__main__':
	app.run(debug=True)