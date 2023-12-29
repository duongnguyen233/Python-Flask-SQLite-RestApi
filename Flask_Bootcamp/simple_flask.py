from flask import Flask
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return "<h1>Hello World!</h1>"

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>Uppercase: {}</h1>".format(name[100])

if __name__ == '__main__':
    app.run(debug=True)
