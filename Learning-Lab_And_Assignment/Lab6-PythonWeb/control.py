from flask import Flask, render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):
    breed = StringField("What Breed are you?")
    submit = SubmitField('Click Me !!!')

@app.route('/', methods=['GET', 'POST'])
def index():

    simpleForm = SimpleForm()
    if simpleForm.validate_on_submit():
        session['breed'] = simpleForm.breed.data
        flash(f"You just change your breed to: {session['breed']}")
        return redirect(url_for('index'))

    return render_template('index.html', form=simpleForm)


if __name__ == '__main__':
    app.run(debug=True)
