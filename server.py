import re
from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key = "key."


@app.route('/')
def index():
    if 'num' not in session:
        # Then create it
        # 'num' is now a KEY in a dictionary via session
        session['num'] = random.randint(1, 100)
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
