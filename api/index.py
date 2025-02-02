import pandas as pd
from flask import request, jsonify
from flask_cors import cross_origin

# Load the CSV file (Make sure it's in the project root)
df = pd.read_csv("marks.csv")

def handler(request):
    """Serverless function to return student marks based on query params."""
    names = request.args.getlist("name")  # Extract 'name' params from URL
    marks = []

    for name in names:
        student = df[df["name"] == name]
        if not student.empty:
            marks.append(int(student["marks"].values[0]))  # Convert to int
        else:
            marks.append(None)  # Return None if student not found

    response = jsonify({"marks": marks})
    response.headers["Access-Control-Allow-Origin"] = "*"  # Enable CORS
    return response
