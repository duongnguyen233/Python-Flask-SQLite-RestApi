# Create Entries into the tables
from models import db, Puppy, Owner, Toy

# Create 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add puppies to Database
db.session.add_all([rufus, fido])
db.session.commit()

# Check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create owner
jose = Owner('Jose', rufus.id)

# Give toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
print(rufus.report_toys())
