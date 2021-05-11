from flask import Flask, render_template 
app = Flask(__name__)       

@app.route('/check/<int:rows>/<int:coulmns>')                           
def checkbox(rows,coulmns):

    return render_template('index.html',rows=rows,coulmns=coulmns) 

if __name__=="__main__":
    app.run(debug=True) 