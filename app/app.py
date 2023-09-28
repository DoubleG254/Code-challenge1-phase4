from flask import Flask,jsonify,make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from model import db,Restaurant,Pizza,RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)
db.init_app(app)

@app.route("/restaurant/",methods=["GET"])
def restaurants():
    restaurants = []
    for restaurant in Restaurant.query.all:
        restaurant_dict = restaurant.to_dict()
        restaurants.append(restaurant_dict)
    response = make_response(
        jsonify(restaurants),200
    )
    return response
@app.route("/pizza/",method=["GET"])
def pizzas():
    pizzas =[]
    for pizza in Pizza.query.all:
        pizza_dict = pizza.to_dict()
        pizzas.append(pizza_dict)
    response = make_response(
        jsonify(pizzas),200
    )
if __name__ == "__main__":
    app.run(port=5555, debug=True)