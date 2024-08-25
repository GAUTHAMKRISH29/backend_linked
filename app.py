import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST', 'GET'])
def handle_bfhl():
    if request.method == 'POST':
        data = request.json.get('data', [])
        print(data)

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        irregular_characters = [item for item in data if not item.isalnum()]
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "gautham29",
            "email": "gauthamposani11@gmail.com",
            "roll_number": "21BCE2075",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
            "irregular_characters": irregular_characters  # Add irregular characters to the response
        }

        # If irregular characters are found, mark the response as not successful
        if irregular_characters:
            response["is_success"] = False
            response["message"] = "Irregular characters found in input."

        return jsonify(response), 200

    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable, or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
