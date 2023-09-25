from flask import Flask, render_template, flash, request
import os
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.app_context().push()


MAIL_ADDRESS = os.environ.get("EMAIL_KEY")
MAIL_APP_PW = os.environ.get("PASSWORD_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        print(data["name"], data["email"], data["message"])
        send_email(data["name"], data["email"], data["message"])
        flash("Message sent, will get back to you as soon as possible!")
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def send_email(name, email, message):
    email_message = f"Subject:Portfolio Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MAIL_ADDRESS, MAIL_APP_PW)
        connection.sendmail(MAIL_ADDRESS,  MAIL_ADDRESS, email_message)


if __name__ == "__main__":
    app.run(debug=False)