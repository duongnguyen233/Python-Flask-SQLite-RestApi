from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Go to /puppy_name/name and see the result!</h1>"

@app.route('/puppy_latin/<name>')
def puppyLatin(name):
    pupname = ''

    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    return "<h1>Your puppy Latin name is: {}</h1>".format(pupname)

if __name__ == '__main__':
    app.run()
