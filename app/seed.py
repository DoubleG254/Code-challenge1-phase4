from app import db,app
from model import Restaurant, Pizza, RestaurantPizza


def seed_data():
    with app.app_context():
        # Create and add restaurants to the database
        restaurant1 = Restaurant(name="Pizza Hut", address="123 Main St")
        restaurant2 = Restaurant(name="Domino's", address="456 Elm St")
        db.session.add(restaurant1)
        db.session.add(restaurant2)
        
        # Create and add pizzas to the database
        pizza1 = Pizza(name="Pepperoni Pizza", ingredients="Pepperoni, cheese, tomato sauce")
        pizza2 = Pizza(name="Margherita Pizza", ingredients="Tomato, mozzarella, basil")
        db.session.add(pizza1)
        db.session.add(pizza2)
        
        # Create and add restaurant-pizza relationships with prices
        relationship1 = RestaurantPizza(price=10.99, restaurant=restaurant1, pizza=pizza1)
        relationship2 = RestaurantPizza(price=9.99, restaurant=restaurant1, pizza=pizza2)
        relationship3 = RestaurantPizza(price=11.99, restaurant=restaurant2, pizza=pizza1)
        db.session.add(relationship1)
        db.session.add(relationship2)
        db.session.add(relationship3)

        # Commit the changes to the database
        db.session.commit()

if __name__ == "__main__":
    seed_data()
