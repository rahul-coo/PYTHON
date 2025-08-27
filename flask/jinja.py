## Building Url Dynamically
## variable rule
## Jinja 2 Template Engine

# Jinja 2 template engine :
'''
{{  }} expression to print output in html 
{%...%} condition for loops
{#...#} this is for comments

'''



from flask import Flask, render_template,request
'''
    It create an instance of the flask class,
    which will be your WSGI (Web Server Gateway Interface) application
'''
## WSGI Apllication 
app=Flask(__name__)

@app.route("/")
def welcome():
    return " <html><h1>    Welcome to Flask course    </h1></html> "

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

#Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=" "
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    return render_template('result.html',results=res)

    
#Variable Rule2
@app.route('/successres/<int:score>')
def success(score):
    res=" "
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp={'score':score, "res":res}
    
    return render_template('result1.html',results=exp)
    


if __name__=="__main__":
    app.run(debug =True)

