from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'This is the content of the first post.',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is the content of the second post.',
        'date_posted': 'April 21, 2024'
    }
]

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_post = {
            'author': 'Anonymous',
            'title': request.form['title'],
            'content': request.form['content'],
            'date_posted': 'May 14, 2024'
        }
        posts.append(new_post)
        return redirect(url_for('home'))
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
