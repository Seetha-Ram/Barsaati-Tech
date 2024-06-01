from flask import Flask, render_template, jsonify
from twitter_trending import run_selenium_script  # Import the function that runs the Selenium script

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_script")
def run_script():
    # Execute the Selenium script and get the results
    results = run_selenium_script()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
