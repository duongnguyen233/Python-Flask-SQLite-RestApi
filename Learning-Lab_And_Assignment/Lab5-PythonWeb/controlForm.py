from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    lowerLetter = False
    upperLetter = False
    numEnd = False

    userName = request.args.get('username')
    lowerLetter = any(c.islower() for c in userName)
    upperLetter = any(c.isupper() for c in userName)
    numEnd = userName[-1].isdigit()

    report = lowerLetter and upperLetter and numEnd


    return render_template('report.html', report=report,
                                          lower=lowerLetter,
                                          upper=upperLetter,
                                          numEnd=numEnd)

if __name__ == '__main__':
    app.run(debug=True)
