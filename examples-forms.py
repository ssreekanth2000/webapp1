from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'

@app.route('/index', methods=['GET', 'POST'])
def index():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        name = request.form['name']
        deviceID = request.form['deviceID']
        room = request.form['room']

        # Validate form data
        if len(name) == 0 or len(deviceID) ==0 or len(room)== 0:
            # Form data failed validation; try again
            error = "No fields can be left blank"
        else:
            # Form data is valid; move along
            print deviceID
            return redirect(url_for('thank_you'))

    # Render the sign-up page
    return render_template('index.html', message=error)

@app.route('/thank-you', methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return render_template('thank-you.html')


# Run the application
app.run(debug=True)
