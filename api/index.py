import json
import pandas as pd

# Load CSV file (Ensure this is in the project root)
df = pd.read_csv("marks.csv")

def handler(request):
    """Serverless function to return student marks based on query params."""
    query_params = request.args.getlist("name")  # Get all 'name' query params
    marks = []

    for name in query_params:
        student = df[df["name"] == name]
        if not student.empty:
            marks.append(int(student["marks"].values[0]))  # Convert to int
        else:
            marks.append(None)  # Return None if student not found

    return json.dumps({"marks": marks}), 200, {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}
