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
        email = request.form['email']
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            flash('This email is already registered, try logging in instead.')
            return redirect(url_for('register'))

        new_user = User(name=request.form['name'],
                        email=request.form['email'],
                        password=generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html")


@login_manager.user_loader
def load_user(id):
    user_id = db.session.execute(db.select(User).where(User.id == id)).scalar()
    return user_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not user:
            flash('This email does not exist. Please try again.')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect,please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    # print(current_user.name)  
    return render_template("secrets.html")
    

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")
    # return send_from_directory('static', path="files/cheat_sheet.pdf", as_attachment=True) alternative


if __name__ == "__main__":
    app.run(debug=True)
