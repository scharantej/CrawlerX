
# Import the necessary modules.
from flask import Flask, render_template

# Create a Flask application.
app = Flask(__name__)

# Define the routes.
@app.route("/")
def index():
    """Render the index page."""
    return render_template("index.html")

@app.route("/intro-to-crawling")
def intro_to_crawling():
    """Render the intro to crawling page."""
    return render_template("introtocrawling.html")

@app.route("/types-of-crawlers")
def types_of_crawlers():
    """Render the types of crawlers page."""
    return render_template("typesofcrawlers.html")

@app.route("/web-crawling-tools")
def web_crawling_tools():
    """Render the web crawling tools page."""
    return render_template("webcrawlingtools.html")

@app.route("/ethics-of-crawling")
def ethics_of_crawling():
    """Render the ethics of crawling page."""
    return render_template("ethicsofcrawling.html")

# Run the application.
if __name__ == "__main__":
    app.run(debug=True)
