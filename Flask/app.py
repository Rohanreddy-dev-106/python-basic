"""
Flask is a micro web framework for Python.
It allows you to build web applications easily and quickly.
The term “micro” means that Flask is lightweight and doesn’t include extra
tools or libraries by default, giving you the flexibility to choose what you want to use.
"""

from flask import Flask, redirect, url_for, render_template, jsonify

# -----------------------------------------------------------
# Create a Flask web server object
# -----------------------------------------------------------
server = Flask(__name__)

# -----------------------------------------------------------
# ROUTES
# -----------------------------------------------------------

@server.route("/")
def home():
    """
    Home route
    URL: http://localhost:5000/
    Method: GET
    Returns a simple HTML string as a response.
    """
    return "<h1>Hello Flask</h1>"  # ✅ fixed closing </h1> tag


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


@server.route("/login")
def login():
    """
    Login route.
    URL: http://localhost:5000/login
    Method: GET
    Redirects the user to the home page using redirect() and url_for().
    """
    return redirect(url_for("home"))


@server.route("/html")
def html_render():
    """
    HTML rendering route.
    URL: http://localhost:5000/html
    Method: GET
    Renders templates/dyn.html and passes variable 'name' to the template.
    """
    return render_template("dyn.html", name="Rohan")


@server.route("/page")
def page_html():
    """
    Page rendering route.
    URL: http://localhost:5000/page
    Method: GET
    Renders templates/page.html and passes variable 'name' to the template.
    """
    return render_template("page.html", name=" ! Class !")


@server.route("/js")
def js_html():
    """
    Page rendering route.
    URL: http://localhost:5000/page
    Method: GET
    Renders templates/js.html
    """
    return render_template("script.html")

@server.route("/json")
def json_returning():
    """
    JSON API route.
    URL: http://localhost:5000/json
    Method: GET
    Returns a JSON response with sample data.
    Example response: {"Name": "Rohan", "age": 20}
    """
    data = {"Name": "Rohan", "age": 20}
    return jsonify(data)

# -------------------- SAMPLE DATA  BASE --------------------
students = [
    {"id": 1, "name": "Alice",   "score": 72},
    {"id": 2, "name": "Bob",     "score": 64},
    {"id": 3, "name": "Charlie", "score": 90},
    {"id": 4, "name": "Diana",   "score": 58},
    {"id": 5, "name": "Ethan",   "score": 79}
]

@server.route("/api/students/high-scorers", methods=["GET"])
def high_scorers():
    """
    GET /api/students/high-scorers
    Returns a JSON list of students whose score > 65.
    Uses a normal for-loop instead of list comprehension.
    """
    filtered = []
    for student in students:
        if student["score"] > 65:
            filtered.append(student)
    return jsonify(filtered)




# -----------------------------------------------------------
if __name__ == "__main__":
    # Run the Flask development server
    # Accessible at http://localhost:5000/
    server.run(debug=True)  # debug=True for auto-reload during development
