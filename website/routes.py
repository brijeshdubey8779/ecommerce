from flask import Flask, render_template, request, redirect, url_for, session, flash
from website import app, db, login_manager
from website.models import Products, User
from website.forms import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from website.functions import is_valid_password
from flask_login import current_user, UserMixin, login_required, login_user, logout_user, LoginManager

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/products")
def products():    
    products = Products.query.all()
    return render_template("products.html", products=products)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        full_name = request.form['name'].strip()
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password1 = request.form['password'].strip()
        password2 = request.form['confirm-password'].strip()    
        
        if password1 != password2:
            flash('Password did not match.', 'error')
            return redirect(url_for('register'))
        elif is_valid_password(password1):
            # encrypting password before storing
            hash_password = generate_password_hash(password1, method='scrypt')

            # Checking if user is alredy registered
            user_exists = User.query.filter_by(email=email).first()
            if user_exists:
                error = "Email already exists."
                return render_template('login.html', error=error)
            
            new_user = User(full_name=full_name, username=username, email=email, password=hash_password)
            
            with app.app_context():
                db.session.add(new_user)
                db.session.commit()
            flash("Registration Succesful", "success")
            return redirect(url_for('login'))
        else:
            flash('''PLease Enter a vailid password which conatins \n
                  1. Minimum 8 charaters.\n
                  2. Atleast ahve 1 number and 1 special charter''', "danger")
            return redirect('register')
            
                
            
        return redirect(url_for('login'))

    
    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        
        user = User.query.filter_by(email=email).first()
        # password_hash = generate_password_hash(password, method='scrypt')
        if user and check_password_hash(user.password, password):
            login_user(user)
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('profile'))
        else:
            flash('Login failed. Check your email or password.', 'danger')
    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
                          
@app.route("/profile")
@login_required
def profile():
    user = current_user
    return render_template('profile.html', user=user)

@app.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():   
    user = current_user     
    if request.method == "POST":
        # Get the updated user details from the form
        
        if user.email != request.form['email']:
            email= request.form['email']
            if User.query.filter_by(email=email).first():
                flash("Email id is alredy registered Try a differet email ", "danger")
                return redirect(url_for('update_profile'), user=user)
        if user.username != request.form['username']:
            username = request.form['username']
            if user.query.filter_by(username=username).first():
                flash("This username is alredy taken.", "danger")
                return redirect(url_for('update_profile'), user=user)
        
        user.full_name = request.form['full_name']
        user.username = request.form['username']
        user.email = request.form['email']

        # Commit the changes to the database

        db.session.commit()
        flash("Profile updated successfully", "success")
        return redirect(url_for('profile'))

    return render_template("update_profile.html", user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user from session
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))