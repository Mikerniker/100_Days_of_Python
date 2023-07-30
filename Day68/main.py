from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#CONFIGURE FLASK LOGIN
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = User(name=name,
                        email=email,
                        password=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return render_template("secrets.html", user_name=name)
    else:
        return render_template("register.html")


@login_manager.user_loader
def load_user(id):
    user_id = db.session.execute(db.select(User).where(User.id == id)).scalar()
    return user_id.id



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        user_id = user.id
        login_user(user)
        load_user(user_id)
        
        return render_template("secrets.html", current_user=user)

    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass

@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf", as_attachment=True)
