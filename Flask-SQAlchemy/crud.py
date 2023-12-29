from basic import db, Puppy

## CREATE ##
# myPup = Puppy('Frankie',4)
# db.session.add(myPup)
# db.session.commit()

## READ ##
all_pups = Puppy.query.all()
print(all_pups)

# SELECT BY ID
# pup_one = Puppy.query.get(1)
# print(pup_one)

# FILTERS
# pup_frankie = Puppy.query.filter_by(name='Frankie')
# print(pup_frankie.all())

# UPDATE
# first_pup = Puppy.query.get(1)
# first_pup.age = 10
# db.session.add(first_pup)
# db.session.commit()

# DELETE
# delete_pup = Puppy.query.get(1)
# db.session.delete(delete_pup)
# db.session.commit()
