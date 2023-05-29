from flask import Flask, render_template, request
import requests
import smtplib


MY_EMAIL = "**************"
MY_PASSWORD = "*************"
app = Flask(__name__)


def get_blog():
    blogs = requests.get("https://api.npoint.io/451fde2f9c37eecbf1c9")
    all_blogs = blogs.json()
    return all_blogs


@app.route("/")
def home():
    return render_template("index.html", posts=get_blog())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/post/<blog_id>')
def post_blog(blog_id):
    post = get_blog()[int(blog_id) - 1]
    title = post["title"]
    subtitle = post["subtitle"]
    author = post["author"]
    date = post["date"]
    content = post["body"]
    image = post["image"]
    return render_template("post.html", title=title, subtitle=subtitle, author=author,
                           date=date, content=content, image=image)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Blog message! \n\nName: {name} \n Email: {email} \n Phone: {phone} \n Message: {message}".encode("UTF-8"))


if __name__ == "__main__":
    app.run(debug=True)
