from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mydatabase_setup import Category, Item, Base

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Items for Soccer
Category1 = Category(name = "Soccer")

session.add(Category1)
session.commit()

Item1 = Item(cat_id=1, item_name = "soccer cleats",
             item_description = "These are specailized shoes worn while playing soccer games.")

session.add(Item1)
session.commit()

Item2 = Item(cat_id=1, item_name = "soccer bags",
             item_description = "These are sturdy, spacious bags used to keep soccer balls and other soccer gear.")

session.add(Item2)
session.commit()

# Items for Basketball
Category2 = Category(name = "Basketball")

session.add(Category2)
session.commit()

Item1 = Item(cat_id=2, item_name = "basketball headbands",
             item_description = "These are headbands worn during basketball games.")

session.add(Item1)
session.commit()

Item2 = Item(cat_id=2, item_name = "basketball jersey",
             item_description = "These are team jersey's worn during basket ball games.")

session.add(Item2)
session.commit()

# Items for Baseball
Category3 = Category(name = "Baseball")

session.add(Category3)
session.commit()

Item1 = Item(cat_id=3, item_name = "baseball caps",
             item_description = "These are team caps worn during basetball games.")

session.add(Item1)
session.commit()

Item2 = Item(cat_id=3, item_name = "baseball bats",
             item_description = "These are special bats used by baseball players use to play baseball games .")

session.add(Item2)
session.commit()

# Items for Frisbee
Category4 = Category(name = "Frisbee")

session.add(Category4)
session.commit()

Item1 = Item(cat_id=4, item_name = "frisbee disc ",
             item_description = "A frisbee (also called a flying disc or simply a disc) is a gliding toy or sporting item .")

session.add(Item1)
session.commit()

Item2 = Item(cat_id=4, item_name = "frisbee wristbands",
             item_description = "These are special bands worn while playing with a frisbee.")

session.add(Item2)
session.commit()

# Items for Snowboarding
Category5 = Category(name = "Snowboarding")

session.add(Category5)
session.commit()

Item1 = Item(cat_id=5, item_name = "snowboarding googles",
             item_description = "snowboard goggles can help protect your eyes from these on-mountain hazards, making your outing a lot more enjoyable.")

session.add(Item1)
session.commit()

Item2 = Item(cat_id=5, item_name = "snowboarding ski helmet",
             item_description = "A ski helmet is a helmet specifically designed and constructed for winter sports.")

session.add(Item2)
session.commit()

# Items for Snowboarding
Category6 = Category(name = "Rock Climbing")

session.add(Category6)
session.commit()

Item1 = Item(cat_id=6, item_name = "rock climbing rope",
             item_description = "These are one of the main gear need to go Rock Climbing.")

session.add(Item1)
session.commit()

Item2 = Item(cat_id=6, item_name = "rock climbing helmet",
             item_description = "A rock climbing helmet is a helmet specifically designed and constructed for rock climbing and to ensure climbers safety.")

session.add(Item2)
session.commit()

print "added menu items."
