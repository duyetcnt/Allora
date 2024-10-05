# Cập nhật app.py để tương thích với mô hình RandomForestRegressor
new_app_content = '''
import os
import pickle
import pandas as pd
import json
from flask import Flask, Response
from config import model_file_path

app = Flask(__name__)


def get_eth_inference():
    # Load the trained model from file
    with open(model_file_path, "rb") as f:
        model = pickle.load(f)

    # Generate a sample input (current timestamp)
    current_timestamp = pd.Timestamp.now().timestamp()
    sample_input = [[current_timestamp]]

    # Predict the ETH price using the model
    prediction = model.predict(sample_input)

    return prediction[0]  # Return the first (and only) prediction


@app.route("/inference/<token>")
def generate_inference(token):
    """Generate inference for given token."""
    if not token or token != "ETH":
        error_msg = "Token is required" if not token else "Token not supported"
        return Response(json.dumps({"error": error_msg}), status=400, mimetype='application/json')

    try:
        inference = get_eth_inference()
        return Response(str(inference), status=200)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500, mimetype='application/json')


@app.route("/update")
def update():
    """Update data and return status."""
    try:
        # Placeholder for data update function
        return "0"
    except Exception:
        return "1"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
'''

# Ghi lại nội dung mới vào app.py
with open(app_file_path, 'w') as file:
    file.write(new_app_content)

new_app_content
