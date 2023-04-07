from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/services')
def services():
  return render_template('services.html')


@app.route('/products')
def products():
  return render_template('products.html')


@app.route('/best_product')
def best_product():
  return render_template('best_product.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    # process user sign up data
    return redirect(url_for('login'))
  return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # process user login data
    return redirect(url_for('home'))
  return render_template('login.html')


@app.route('/image')
def image():
  return render_template('image.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
