from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CatalogItem, User

engine = create_engine('sqlite:///categoryitems.db')
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


# Create dummy user
User1 = User(name="Madhan", email="madhan1992@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Item for Cricket
category1 = Category(user_id=1, name="Cricket")

session.add(category1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Helmet", description="It was introduced in the 90's to protect people from getting hurt. As the game speeds up, helmet plays a vital role",
                     category=category1)

session.add(catalogItem2)
session.commit()

print "added Catalog items!"
