from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import*

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
@app.route('/admin')
def admin():

	return render_template("cart.html")

@app.route('/log')
def log():
	return render_template("log.html")
##### Code here ######



#####################


if __name__ == '__main__':
	app.run(debug=True)