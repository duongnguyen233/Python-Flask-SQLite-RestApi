from basic import db, Puppy

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

# Check ids (haven't added sam and frank to database, so they should be None)
print(sam.id)
print(frank.id)

# Ids will get created automatically once we add these entries to the DB
db.session.add_all([sam, frank])

# Alternative for individual additions:
# db.session.add(sam)
# db.session.add(frank)

# Now save it to the database
db.session.commit()

print(sam.id)
print(frank.id)
