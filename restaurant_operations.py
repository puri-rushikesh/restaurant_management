from flask_sqlalchemy import SQLAlchemy
from utils.config import app
from sqlalchemy import Column, String, Integer
from utils.logger import logger

# Initializing our database
db = SQLAlchemy(app)


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    restaurant = Column(String(100), nullable=False)
    type_of_food = Column(String(100), nullable=False)
    cuisine = Column(String(100), nullable=False)
    price = Column(String(20), nullable=False)
    specialties = Column(String(100), nullable=False)

    def json(self):
        """this method we are defining will convert our output to json"""
        return {'id': self.id,
                'restaurant': self.restaurant,
                'type_of_food': self.type_of_food,
                'cuisine': self.cuisine,
                'price': self.price,
                'specialties': self.specialties}

    def add_restro(self, restaurant_name, food_type, _cuisine, _price, _specialties):
        """function to add restaurant to database using _name, _year, _address as parameters"""
        # creating an instance of our Restaurant constructor
        new_restaurant = Restaurant(restaurant=restaurant_name, type_of_food=food_type, cuisine=_cuisine, price=_price,
                                    specialties=_specialties)
        db.session.add(new_restaurant)  # add new restaurant to database session
        db.session.commit()  # commit changes to session
        logger(1, "Restaurant Added Successfully")

    def get_restro(self, _id):
        """function to get restaurant using the id of the restaurant as parameter"""
        logger(1, f"Restaurant id : {str(_id)} Fetching")
        return [Restaurant.json(Restaurant.query.filter_by(id=_id).first())]
        # Restaurant.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_restro(self, _id, restaurant_name, food_type, _cuisine, _price, _specialties):
        """function to update the details of a restaurant using id as key"""
        restaurant_to_update = Restaurant.query.filter_by(id=_id).first()
        restaurant_to_update.restaurant = restaurant_name
        restaurant_to_update.type_of_food = food_type
        restaurant_to_update.cuisine = _cuisine
        restaurant_to_update.price = _price
        restaurant_to_update.specialties = _specialties
        db.session.commit()
        logger(1, "Restaurant Updated Successfully")

    def delete_restro(self, _id):
        """function to delete a restaurant from our database using the id of the restaurant as a parameter"""
        Restaurant.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # committing the new change to our database
        logger(1, "Restaurant Deleted Successfully")

    def get_all_restro(self):
        """function to get all restaurants in our database"""
        logger(1, "Getting All Restaurants Data")
        return [Restaurant.json(restaurant) for restaurant in Restaurant.query.all()]
