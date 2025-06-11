from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return "<h2>This is the About page</h2><p><a href='/'>Back to Home</a></p>"


@app.route('/contactddd')
def contact():
    return "<h2>Contact us at analytics@example.com</h2><p><a href='/'>Back to Home</a></p>"


@app.route('/go-home')
def go_home():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=300)