from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all requests

# Load the CSV file with student marks
df = pd.read_csv("marks.csv")  # Ensure this file is in the project root

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get all 'name' query params
    marks = []

    for name in names:
        student = df[df["name"] == name]
        if not student.empty:
            marks.append(int(student["marks"].values[0]))  # Convert to int
        else:
            marks.append(None)  # If name not found, return None

    return jsonify({"marks": marks})

# Vercel expects a variable named `app`
def handler(request, *args):
    return app(request.environ, start_response)
