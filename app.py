from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

# Configure SMTP server details
smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_username = 'Current.SolutionsLLC@hotmail.com'
smtp_password = 'Xcatnipplesx714!'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
@app.route('/contact', methods=['GET'])
def contact():
    if request.method == 'POST':
        # Handle POST request as before
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        # ... (rest of the code)

    # Handle GET request separately
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()














