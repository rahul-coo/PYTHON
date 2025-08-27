from flask import Flask
'''
    It create an instance of the flask class,
    which will be your WSGI (Web Server Gateway Interface) application
'''
## WSGI Apllication 
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Universe . The Universe . 001 "

@app.route("/index")
def index():
    return "Welcome to my Index Universe "



if __name__=="__main__":
    app.run(debug =True)
