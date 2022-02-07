from flask import request, Response, jsonify
from utils.config import app
from restaurant_operations import Restaurant

restro = Restaurant()


@app.route('/', methods=['GET', 'POST'])
def main_func():
    """Function to add new restaurant to our database"""
    return {"Response": "Success, Please hit specific routes"}


# route to add new restaurant
@app.route('/restaurant', methods=['POST'])
def add_restro():
    """Function to add new restaurant to our database"""
    request_data = request.get_json()  # getting data from client
    restro.add_restro(request_data["restaurant"], request_data["type_of_food"], request_data["cuisine"],
                      request_data["price"], request_data["specialties"])
    response = Response("Restaurant added", 201, mimetype='application/json')
    return response


# route to get restaurant by id
@app.route('/restaurant/<int:id>', methods=['GET'])
def get_restro_by_id(id):
    return_value = restro.get_restro(id)
    return jsonify(return_value)


# route to update restaurant with PUT method
@app.route('/restaurant/<int:id>', methods=['PUT'])
def update_restro(id):
    """Function to edit restaurant in our database using id"""
    request_data = request.get_json()
    restro.update_restro(id, request_data["restaurant"], request_data["type_of_food"], request_data["cuisine"],
                      request_data["price"], request_data["specialties"])
    response = Response("Restaurant details updated", status=200, mimetype='application/json')
    return response


# route to delete restaurant using the DELETE method
@app.route('/restaurant/<int:id>', methods=['DELETE'])
def remove_restro(id):
    """Function to delete restaurant from our database"""
    restro.delete_restro(id)
    response = Response("Restaurant Deleted", status=200, mimetype='application/json')
    return response


# route to get all restaurant
@app.route('/restaurant', methods=['GET'])
def get_restro():
    """Function to get all the restaurants in the database"""
    return jsonify({'Restaurants': restro.get_all_restro()})


if __name__ == "__main__":
    app.run(debug=True)
