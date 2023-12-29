import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Puppy (ID: {self.id}) {self.name} with age {self.age}"

def addPuppy():
    name = input('\nPuppyName: ')
    age = int(input('PuppyAge: '))
    puppy = Puppy(name, age)
    db.session.add(puppy)
    db.session.commit()
    print()

def changeInfoPuppy():
    name = input('\nPuppyName want to change: ')
    age = int(input('Age update: '))
    puppy = Puppy.query.filter_by(name=name).first()
    puppy.age = age
    db.session.add(puppy)
    db.session.commit()
    print()

def printAllPuppies():
    print()
    puppies = Puppy.query.all()
    for pup in puppies:
        print(pup)
    print()

continueMenu = True
while (continueMenu):
    print('1. Add a pet')
    print('2. Change a pet information')
    print('3. Display all pets')
    print('4. Quit')

    option = int(input('Your option: '))
    if option == 1:
        addPuppy()
    elif option == 2:
        changeInfoPuppy()
    elif option == 3:
        printAllPuppies()
    elif option == 4:
        continueMenu = False
    else:
        continue
