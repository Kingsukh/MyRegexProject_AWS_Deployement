import re
from flask import Flask, render_template, request


app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

##########################################################
# Route to handle form submission and regex matching
@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string')
    regex_pattern = request.form.get('regex_pattern')
    matches = re.findall(regex_pattern, test_string)
    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

# Email validation route
@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email')
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    is_valid = re.match(email_pattern, email) is not None
    return render_template('index.html', email=email, is_valid=is_valid)
##########################################################

#127.0.0.1=>Loop back address

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
