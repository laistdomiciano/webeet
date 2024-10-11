from flask import Flask, jsonify, request, abort
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

with open('characters.json', 'r') as file:
    characters = json.load(file)


def find_character_by_id(char_id):
    for char in characters:
        if char["id"] == char_id:
            return char
    return None


# Fetch all characters (with Pagination) - 10 Points
@app.route('/characters', methods=['GET'])
def get_characters():
    limit = int(request.args.get('limit', 20))
    skip = int(request.args.get('skip', 0))

    filtered_characters = characters

    paginated_characters = filtered_characters[skip:skip + limit]
    return jsonify(paginated_characters)


# Feature 2: Fetch a specific character by ID - 5 Points
@app.route('/characters/<int:id>', methods=['GET'])
def get_character_by_id(id):
    character = find_character_by_id(id)
    if not character:
        abort(404, description="Character not found")
    return jsonify(character)


# Feature 3: Fetch a fIltered character list - 10 Points
@app.route('/characters/filter', methods=['GET'])
def filter_characters():
    filters = {key: value.lower() for key, value in request.args.items()}
    age_more_than = filters.pop('age_more_than', None)

    filtered_characters = characters

    if age_more_than:
        filtered_characters = [char for char in filtered_characters if int(char.get('age', 0)) > int(age_more_than)]

    for k, v in filters.items():
        filtered_characters = [char for char in filtered_characters if str(char.get(k, "")).lower() == v]

    return jsonify(filtered_characters)


# Feature 4: Fetch a sorted character list - 10 Points
@app.route('/characters/sorted', methods=['GET'])
def sorted_characters():
    sort_field = request.args.get('sort_field', 'name')
    sort_order = request.args.get('order', 'asc')

    sorted_characters = sorted(characters, key=lambda x: x.get(sort_field, '').lower())

    if sort_order == 'desc':
        sorted_characters = sorted_characters[::-1]

    return jsonify(sorted_characters)


# Feature 5: Add a new character to the list - 25 points
@app.route('/characters', methods=['POST'])
def add_character():
    new_char = request.json
    if not new_char or not all(key in new_char for key in ["id", "name", "house", "role", "age"]):
        return abort(400, description="Missing required fields")

    characters.append(new_char)
    return jsonify(new_char), 201


# Feature 6: Edit a character - 30 points
@app.route('/characters/<int:id>', methods=['PATCH'])
def edit_character(id):
    character = find_character_by_id(id)
    if not character:
        return abort(404, description="Character not found")

    data = request.json
    character.update(data)
    return jsonify(character)


# Feature 7: Delete a character - 10 points
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = get_character_by_id(id)
    if not character:
        return abort(400, description="Character not found")

    characters.remove(character)
    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
