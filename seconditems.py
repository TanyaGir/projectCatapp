from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mydatabase_setup import Category, Item, Base

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

#item1 = Item(cat_id = 1, item_name = "soccer clipboards",
#              item_description ="these are clipboards used by the coach and players to keep track of the game points")

#session.add(item1)
#session.commit()

item2 = Item(cat_id=2 ,item_name = "basketball mouthguards",
              item_description = "mouthguards worn during games to protect the teeth")

session.add(item2)
session.commit()

item3 = Item(cat_id=3 ,item_name = "baseball gloves",
              item_description = "gloves specially made for the game to help the players to catch the baseball")
session.add(item3)
session.commit()


item4 = Item(cat_id=4 ,item_name = "frisbee gloves",
              item_description = "gloves specially made for the game to help the players to catch the frisbee")
session.add(item4)
session.commit()

print "added items!"
