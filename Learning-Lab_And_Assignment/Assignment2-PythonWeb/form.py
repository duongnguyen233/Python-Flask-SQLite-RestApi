from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, TextAreaField, HiddenField
from wtforms.validators import InputRequired

class AddBlogForm(FlaskForm):
    title = StringField('Title of Blog: ', [InputRequired()])
    subtitle = StringField('Subtitle of Blog: ', [InputRequired()])
    author = StringField('Author: ', [InputRequired()])
    content = TextAreaField('Content: ', [InputRequired()])
    submit = SubmitField('Add Blog')

class DeleteBlogForm(FlaskForm):
    id = StringField()
    submit = SubmitField('Delete Blog')

class SelectEditBlogForm(FlaskForm):
    id = StringField()
    submit = SubmitField('Edit Blog')

class EditBlogForm(FlaskForm):
    title = StringField('Title of Blog: ', [InputRequired()])
    subtitle = StringField('Subtitle of Blog: ', [InputRequired()])
    author = StringField('Author: ', [InputRequired()])
    content = TextAreaField('Content: ', [InputRequired()])
    submit = SubmitField('Send')
