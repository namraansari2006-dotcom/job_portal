
from flask import Flask, render_template, request

app = Flask(__name__)


# Home Page
@app.route('/')
def home():
    return render_template('home.html')


# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Registration and MongoDB code will be added here
        return "Registration form submitted successfully!"

    return render_template('register.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Login verification will be added here
        return f"Login form received for: {email}"

    return render_template('login.html')


# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
