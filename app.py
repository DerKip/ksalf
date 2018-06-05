from flask import Flask

app=Flask(__name__) #setting up our WSGI app from flask

@app.route('/')
def home():
    return "hello, world"

if __name__=='__main__':
    app.run(debug=True)
