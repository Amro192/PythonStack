from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/play')                           
def hello_world():

    return render_template('index.html',number_sq=3)  

@app.route('/play/<number>')                           
def play(number):

    return render_template('index.html',number_sq=int(number))  

@app.route('/play/<number>/<color>')                           
def playColor(number,color):

    return render_template('index.html',number_sq=int(number),cColor=color)  
    

if __name__=="__main__":
    app.run(debug=True)                   
