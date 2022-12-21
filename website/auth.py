from flask import Blueprint, render_template, request, flash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html", text='hello there',boolean='f', user=current_user)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('firstName must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('password must be greater than 6 characters.', category='error')            
        else:
            # add user to the database
            flash('Account created', category='success')
            
    return render_template("sign_up.html", user=current_user)


