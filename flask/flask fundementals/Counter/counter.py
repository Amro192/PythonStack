from typing import Counter
from flask import Flask, render_template, request, redirect , session
app = Flask(__name__)
app.secret_key="Secret"


@app.route('/')
def counter_times():
    if 'counter' in session:
        session['counter'] = session.get('counter') + 1
    else:
        session['counter'] = 1

    return "COUNTER: {}".format(session.get('counter'))

@app.route('/destroy_session')
def result_form():
    session.clear()
    return "Deleted"

if __name__ == "__main__":
    app.run(debug=True)