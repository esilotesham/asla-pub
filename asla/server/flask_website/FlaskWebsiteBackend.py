from __future__ import print_function
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from user_admin_service import UserAdminService
import os
import sys

app = Flask(__name__)
app.secret_key = "1234"
admin_service = UserAdminService()

def create_app():
    """
    Returns the app's name to bootstrap
    :return: the name of the app
    """
    bootstrap_app = Flask(__name__)
    Bootstrap(bootstrap_app)
    return bootstrap_app


@app.route('/')
def welcome_to_asla():
    """
    Landing page
    :return:
    """
    return render_template('index.html'), 200


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Allows for signup
    :return:
    """
    if request.method == "GET":
        return render_template('signup.html'), 200
    elif request.method == "POST":
        #print(request.form['email'], file=sys.stderr)
        if not admin_service.make_new_user(request.form):
            flash('It appears you are already with us, try logging in instead!', category='error')
            return render_template('signup.html'), 200
        else:
            flash("Thank you for registering!", category='success')
            return render_template('signup.html'), 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Allows for login
    :return:
    """
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        return render_template('login.html')


@app.route('/login_expert', methods=['GET'])
def login_expert():
    """
    Allows for login
    :return:
    """
    return render_template('login_expert.html')


@app.route('/update', methods=['POST'])
def update():
    """
    updates a user
    :return:
    """
    return "Update"


@app.route('/authenticate', methods=['POST'])
def authenticate():
    """
    Authenticates a user's credentials'
    """    
    if admin_service.authenticate_user(request.form['email'], request.form['pwd']):
        return "Valid User", 200
    else:
        return "Invalid credentials", 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
