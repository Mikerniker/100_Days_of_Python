from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/188d478a1aceaa6a6e0f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

# @app.route('/post/<blog_num>')
# def post(blog_num):
#     blog_url = "https://api.npoint.io/188d478a1aceaa6a6e0f"
#     response = requests.get(blog_url)
#     all_posts = response.json()
#     return render_template("post.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
