from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_blogs():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    return response.json()

def fetch_blog(number):
    posts = fetch_blogs()

    for post in posts:
        if post["id"] == int(number):
            return post
    
    return {"msg": "doesn't exist"}

@app.route('/')
def get_blogs():
    return render_template("blogs.html", posts = fetch_blogs())

@app.route('/<number>')
def get_blog(number):
    return render_template("blog.html", post = fetch_blog(number))

if __name__ == '__main__':
    app.run(port=8000,debug=True)