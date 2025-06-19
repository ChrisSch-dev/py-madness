from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
POSTS = []

HTML = """
<!doctype html>
<title>Flask Blog</title>
<h1>Simple Blog</h1>
<form method=post>
  <input name=title placeholder="Title" required>
  <br>
  <textarea name=content placeholder="Content" required></textarea>
  <br>
  <button type=submit>Post</button>
</form>
<ul>
{% for post in posts %}
  <li><b>{{ post.title }}</b><br>{{ post.content }}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        POSTS.append({"title": request.form["title"], "content": request.form["content"]})
        return redirect("/")
    return render_template_string(HTML, posts=POSTS)

if __name__ == "__main__":
    app.run(debug=True)