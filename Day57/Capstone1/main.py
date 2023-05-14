from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/188d478a1aceaa6a6e0f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<blog_id>')
def blog_post(blog_id):
    blog_url = "https://api.npoint.io/188d478a1aceaa6a6e0f"
    response = requests.get(blog_url)
    all_posts = response.json()
    post = all_posts[int(blog_id) - 1]
    title = post["title"]
    subtitle = post["subtitle"]
    body = post["body"]
    return render_template("post.html", title=title, subtitle=subtitle, body=body)

if __name__ == "__main__":
    app.run(debug=True)
