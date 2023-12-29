from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    nameStr = "Testing string"
    mappingTest = {'name 1':'name 2'}
    myListTest = ['Fluffy', 'Rufuss', 'Cogi']
    return render_template('index.html', my_variable = nameStr,
                                         mapping = mappingTest,
                                         myList = myListTest)
if __name__ == '__main__':
    app.run(debug=True)
