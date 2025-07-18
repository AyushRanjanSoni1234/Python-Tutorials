## PUT and DELETE - HTTP Verbs
## Working of APIs - JSON

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initailize a data in the form of list
items = [
    {
        'id': 1,
        'name': 'item1',
        'price': 10.99
    },
    {
        'id': 2,
        'name': 'item2',
        'price': 20.99
    },
    {
        'id': 3,
        'name': 'item3',
        'price': 30.99
    }
]

@app.route('/')
def home():
    return "Welcome to the API home page"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## get: Retrieve a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'Error': 'Item not found'}), 404


## post: Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json or 'price' not in request.json:
        return jsonify({'Error': 'Bad Request'}), 400
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'price': request.json['price']
    }
    items.append(new_item)
    return jsonify(new_item), 201

## put: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'Error': 'Item not found'}), 404
    if not request.json:
        return jsonify({'Error': 'Bad Request'}), 400
    item['name'] = request.json.get('name', item['name'])
    item['price'] = request.json.get('price', item['price'])
    return jsonify(item)


## delete: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'Result': 'Item deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True, port=5004)