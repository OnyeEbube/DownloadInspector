from flask import Flask, request, render_template, redirect
from flask_cors import CORS
from functions import check_malicious

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form  # Get the form data
        download_link = data.get('link')  # Retrieve the download link from the form data
        is_malicious = check_malicious(download_link)  # Call the check_malicious function to determine if the link is malicious
        return render_template('result.html', is_malicious=is_malicious, link=download_link)  # Render the result.html template with the malicious status and link
    else:
        return render_template('index.html')  # Render the index.html template for the initial page load

def run_app():
    app.run(port=5001, debug=True)  # Run the application on port 5001 in debug mode

if __name__ == '__main__':
    run_app()
