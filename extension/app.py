from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from functions import check_malicious

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def index():
    # Retrieve the JSON data from the request
    data = request.get_json()
    # Extract the download link from the data
    download_link = data.get('downloadLink')
    # Call the check_malicious function to determine if the link is malicious
    is_malicious = check_malicious(download_link)
    # Return the result as a JSON response
    return jsonify({'is_malicious': is_malicious})

def run_app():
    # Run the Flask application in debug mode
    app.run(debug=True)

if __name__ == '__main__':
    # Start the Flask application
    run_app()
