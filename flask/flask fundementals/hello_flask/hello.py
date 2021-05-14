from flask import Flask ,render_template
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!'
    
@app.route('/dojo')
def dojo():
    return 'dojo'
@app.route('/say/<name>')
def say(name):
    return f"hi {name}" 

@app.route('/lists')
def render_lists():
    
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

@app.route('/repeat/<name>/<number>')
def repeat(name,number):
    post = " "
    for i in range(int(number)):
        post+=name+ " "
    return post 


if __name__=="__main__":    
            app.run(debug=True)    
