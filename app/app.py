from flask import Flask,jsonify,make_response,request
from flask_migrate import Migrate
from model import db,Restaurant,Pizza,RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)
db.init_app(app)



# Route to get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    data = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
    return jsonify(data)

# Route to get a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    pizza_data = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in restaurant.pizzas]
    data = {"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "pizzas": pizza_data}
    return jsonify(data)

# Route to delete a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    # Delete associated RestaurantPizzas first
    RestaurantPizza.query.filter_by(restaurant_id=id).delete()
    db.session.delete(restaurant)
    db.session.commit()

    return make_response('', 204)

# Route to get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    data = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
    return jsonify(data)

# Route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    
    price = request.form.get('price')
    pizza_id = request.form.get('pizza_id')
    restaurant_id = request.form.get('restaurant_id')

    # Validate price
    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)

    if not restaurant or not pizza:
        return jsonify({"errors": ["Restaurant or Pizza not found"]}), 400

    restaurant_pizza = RestaurantPizza(price=price, restaurant=restaurant, pizza=pizza)
    db.session.add(restaurant_pizza)
    
    try:
        db.session.commit()
        return jsonify({"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}), 201
    except:
        db.session.rollback()
        return jsonify({"errors": ["Validation errors"]}), 400



if __name__ == "__main__":
    app.run(port=5555, debug=True)