from flask import Flask, request, render_template, redirect
from flask_login import LoginManager, UserMixin

login_manager = LoginManager()

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/services')
def services():
  return render_template('services.html')


@app.route('/products')
def products():
  return render_template('products.html')


@app.route('/bestproduct')
def bestproduct():
  return render_template('bestproduct.html')


@app.route('/signup')
def signup():
  return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # Handle user login
    username = request.form['username']
    password = request.form['password']
    # Check if username and password are correct
    if username == 'example' and password == 'password':
      return redirect('/')
    else:
      return render_template('login.html', error=True)
  else:
    # Show login form
    return render_template('login.html', error=False)


@app.route('/contact')
def contact():
  return render_template('contact.html')


class User(UserMixin):

  def __init__(self, id):
    self.id = id


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
