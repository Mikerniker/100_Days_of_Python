from flask import Flask, render_template
import requests

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

@app.route("/contact")
def contact():
    return render_template("contact.html")

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

if __name__ == "__main__":
    app.run(debug=True)
