# Aim:
# To develop a Flask web application that sets and retrieves cookies using HTML forms.

from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

# HTML template with a form and links to get and clear cookies.
template = """
<!doctype html>
<title>Cookie Demo</title>
<h2>Cookie Example</h2>

<!-- Simple form to accept user's name -->
<form method="POST" action="/setcookie">
  Enter your name: <input type="text" name="username">
  <input type="submit" value="Set Cookie">
</form>
<br>

<!-- Links to check and clear cookies -->
<a href="/getcookie">Check Cookie</a> <br>
<a href="/clearcookie">Clear Cookie</a>
"""

@app.route('/')
def home():
    # Render the HTML template
    return render_template_string(template)

@app.route('/setcookie', methods=['POST'])
def setcookie():
    username = request.form.get('username')
    
    if username:
        # Create a response and set the cookie
        resp = make_response(f"Cookie has been set for user: {username}<br><a href='/'>Go back</a>")
        resp.set_cookie('username', username)
        return resp
    else:
        # Handle empty input
        return "Please enter a valid name. <br><a href='/'>Go back</a>"

@app.route('/getcookie')
def getcookie():
    username = request.cookies.get('username')
    
    if username:
        return f"Hello {username}, welcome back!<br><a href='/'>Go back</a>"
    else:
        return "No cookie found. Please enter your name first.<br><a href='/'>Go back</a>"

@app.route('/clearcookie')
def clearcookie():
    # Create a response and delete the cookie
    resp = make_response("Cookie has been cleared!<br><a href='/'>Go back</a>")
    resp.set_cookie('username', '', expires=0)
    return resp

if __name__ == '__main__':
    # Use a different port if 5000 is already in use
    app.run(debug=True, port=5001)
