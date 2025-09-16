"""Flask is a micro web framework for Python. 
It allows you to build web applications easily and quickly. 
The term “micro” means that Flask is lightweight and doesn’t include extra tools or libraries by default, 
giving you the flexibility to choose what you want to use.
"""

from flask import Flask, redirect, url_for, render_template, jsonify

# Create a Flask web server object
server = Flask(__name__)  

# ------------------- ROUTES -------------------

@server.route("/")
def home():
    """
    Home route.
    URL: http://localhost:5000/
    Method: GET
    Returns a simple HTML string as a response.
    """
    return "<h1>Hello Flask<h1/>"

@server.route("/user/<name>")
def user(name):
    """
    Dynamic route with a variable.
    URL: http://localhost:5000/user/<name>
    Method: GET
    Takes a 'name' from the URL and returns a personalized message.
    Example: /user/Rohan => "My name is Rohan"
    """
    return f"My name is {name}"

@server.route('/login')
def Login():
    """
    Login route.
    URL: http://localhost:5000/login
    Method: GET
    Redirects the user to the home page using `redirect` and `url_for`.
    """
    return redirect(url_for("home"))

@server.route("/html")
def html_render():
    """
    HTML rendering route.
    URL: http://localhost:5000/html
    Method: GET
    Renders an HTML template named 'dyn.html' located in the 'templates' folder.
    """
    return render_template("dyn.html")

@server.route("/json")
def json_Returning():
    """
    JSON API route.
    URL: http://localhost:5000/json
    Method: GET
    Returns a JSON response with sample data.
    Example response: {"Name":"Rohan", "age":20}
    """
    data = {"Name": "Rohan", "age": 20}
    return jsonify(data)

# ------------------- RUN SERVER -------------------

if __name__ == "__main__":
    # Run the Flask development server
    # Accessible at http://localhost:5000/
    server.run()
