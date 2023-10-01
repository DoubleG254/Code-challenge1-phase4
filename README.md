FlaskCodeChallenge-PizzaRestaurants

Models
The following relationships have been created:

A Restaurant has many Pizzas through RestaurantPizza
A Pizza has many Restaurants through RestaurantPizza
A RestaurantPizza belongs to a Restaurant and belongs to a Pizza
Start by creating the models and migrations:

Validations
The followin validations have been applied to the  RestaurantPizza model:

must have a price between 1 and 30
Add validations to Restaurant Model:

must have a name less than 50 words in length
must have a unique name
Routes
The following routes have been placed :

GET /restaurantsLinks to an external site.

Return JSON data in the format below:

[ { "id": 1, "name": "Dominion Pizza", "address": "Good Italian, Ngong Road, 5th Avenue" }, { "id": 2, "name": "Pizza Hut", "address": "Westgate Mall, Mwanzi Road, Nrb 100" } ]

GET /restaurants/:idLinks to an external site.

If the Restaurant exists, return JSON data in the format below:

{ "id": 1, "name": "Dominion Pizza", "address": "Good Italian, Ngong Road, 5th Avenue", "pizzas": [ { "id": 1, "name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese" }, { "id": 2, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni" } ] }

If the Restaurant does not exist, return the following JSON data, along with the appropriate HTTP status code:

{ "error": "Restaurant not found" }

DELETE /restaurants/:id
If the Restaurant exists, it should be removed from the database, along with any RestaurantPizzas that are associated with it (a RestaurantPizza belongs to a Restaurant, so you need to delete the RestaurantPizzas before the Restaurant can be deleted).

After deleting the Restaurant, return an empty response body, along with the appropriate HTTP status code.

If the Restaurant does not exist, return the following JSON data, along with the appropriate HTTP status code:

{ "error": "Restaurant not found" }

GET /pizzas
Return JSON data in the format below:

[ { "id": 1, "name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese" }, { "id": 2, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni" } ]

POST /restaurant_pizzas
This route should create a new RestaurantPizza that is associated with an existing Pizza and Restaurant. It should accept an object with the following properties in the body of the request:

{ "price": 5, "pizza_id": 1, "restaurant_id": 3 }

If the RestaurantPizza is created successfully, send back a response with the data related to the Pizza:

{ "id": 1, "name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese" }

If the RestaurantPizza is not created successfully, return the following JSON data, along with the appropriate HTTP status code:

{ "errors": ["validation errors"] }

Project Setup
To set up and run this Flask API project, follow these steps:

Clone the repository to your local machine:
git clone https://github.com/your-username/Code-challenge1-phase4.git
Navigate to the project directory: cd FlaskCodeChallenge-PizzaRestaurants
Author
Author Name: Glory Gweth

License
This project is licensed under the MIT License.