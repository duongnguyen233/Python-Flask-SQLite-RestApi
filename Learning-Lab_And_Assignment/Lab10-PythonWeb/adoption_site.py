import os
from form import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

#################################
### SQL Database Section ########
#################################

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app, db)

api = Api(app)

#################################
###           Models     ########
#################################
class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and no owner assigned yet!"

    def json(self):
        if self.owner:
            return {'id':self.id, 'name':self.name, 'owner':self.owner.name}
        else:
            return {'id':self.id, 'name':self.name, 'owner':'Not has yet'}

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

#################################
#####            API     ########
#################################
class PuppyApi(Resource):

    def get(self):
        puppies = Puppy.query.all()
        return [pup.json() for pup in puppies]

class PuppyDelApi(Resource):
    def delete(self, id):
        pup = Puppy.query.filter_by(id=id).first()
        db.session.delete(pup)
        db.session.commit()
        return {'note':'delete success'}

#################################
###   View Functions     ########
#################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)

@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def delete_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))

    return render_template('delete.html', form=form)

@app.route('/addOwner', methods=['GET', 'POST'])
def add_owner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        name = form.name.data
        id = form.id.data
        new_owner = Owner(name, id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list_pup'))

    return render_template('addOwner.html', form=form)

api.add_resource(PuppyApi,'/listapi')
api.add_resource(PuppyDelApi,'/deleteapi/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
