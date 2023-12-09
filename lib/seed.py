from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review
from faker import Faker

engine = create_engine('sqlite:///restaurants.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Create restaurants
for _ in range(10):
    restaurant = Restaurant(name=fake.company(), price=fake.random_int(min=20, max=200))
    session.add(restaurant)

# Create customers
for _ in range(10):
    customer = Customer(first_name=fake.first_name(), last_name=fake.last_name())
    session.add(customer)

# Commits the session to add these objects to the database
session.commit()

# Get all restaurants and customers
restaurants = session.query(Restaurant).all()
customers = session.query(Customer).all()

# Create reviews
for _ in range(20):
    review = Review(
        customer_id=fake.random_element(customers).id,
        restaurant_id=fake.random_element(restaurants).id,
        star_rating=fake.random_int(min=1, max=5)
    )
    session.add(review)

session.commit()
