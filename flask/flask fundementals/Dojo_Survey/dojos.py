from flask import Flask, render_template, request, redirect , session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def dojo_Form():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def result_form():
    print(request.form)
    session['name']=request.form['namee']
    session['dojo']=request.form['dojoo']
    session['favorite']=request.form['languagee']
    session['comment']=request.form["comments"]
    return redirect("/display")

@app.route('/display')
def display_form():
    print(request.form)
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)