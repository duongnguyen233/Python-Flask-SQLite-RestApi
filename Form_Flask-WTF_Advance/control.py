from flask import Flask, render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextAreaField,
                     SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):
    submit = SubmitField('Click Me !!!')

class InfoForm(FlaskForm):
    breed = StringField('What Breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('Please chose your mood:',
                       choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField('Pick your favorite food:',
                               choices=[('chi', 'Chicken'),('bf', 'Beef'),('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou'))

    simpleForm = SimpleForm()
    if simpleForm.validate_on_submit():
        flash('You just clicked the button !')
        return redirect(url_for('index', form=simpleForm))

    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
