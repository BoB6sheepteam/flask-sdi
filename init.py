from flask import Flask, render_template, redirect, url_for, request



app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])

def login():

    error = None

    if request.method == 'POST':

        if request.form['username'] != 'admin' or request.form['password'] != 'admin':

            error = 'Invalid Credentials. Please try again.'

        else:

            return redirect(url_for('secret'))

    return render_template('login.html', error=error)



@app.route('/secret')

def secret():

    return "This is a secret page!"



if __name__=="__main__":

	app.run()