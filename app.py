from flask import Flask, jsonify, request, abort
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# Load characters from the JSON file
def load_characters():
    with open('data/characters.json', 'r') as file:
        return json.load(file)


# Save characters to the JSON file
def save_characters():
    with open('data/characters.json', 'w') as file:
        json.dump(characters, file, indent=4)

characters = load_characters()


def find_character_by_id(char_id):
    """Find a character by their ID.

    Args:
        char_id (int): The ID of the character to find.

    Returns:
        dict or None: The character dictionary if found, otherwise None.
    """
    for char in characters:
        if char["id"] == char_id:
            return char
    return None


# Feature 1: Fetch all characters (with Pagination) - 10 Points
@app.route('/characters', methods=['GET'])
def get_characters():
    """Fetch all characters with optional pagination.

    Query Parameters:
        limit (int): The number of characters to return (default is 20).
        skip (int): The number of characters to skip for pagination (default is 0).

    Returns:
        JSON: A list of characters.
    """
    limit = int(request.args.get('limit', 20))
    skip = int(request.args.get('skip', 0))

    filtered_characters = characters

    paginated_characters = filtered_characters[skip:skip + limit]
    if limit == 20 and skip == 0:
        import random
        paginated_characters = random.sample(characters, min(20, len(characters)))

    return jsonify(paginated_characters)


# Feature 2: Fetch a specific character by ID - 5 Points
@app.route('/characters/<int:id>', methods=['GET'])
def get_character_by_id(id):
    """Fetch a specific character by their ID.

    Args:
        id (int): The ID of the character to fetch.

    Returns:
        JSON: The character data or an error message if not found.
    """
    character = find_character_by_id(id)
    if not character:
        return jsonify({"error": "Character not found"}), 404
    return jsonify(character)


# Feature 3: Fetch a filtered character list - 10 Points
@app.route('/characters/filter', methods=['GET'])
def filter_characters():
    """Fetch a list of characters filtered by specified criteria.

    Query Parameters:
        age_more_than (int): Filter characters older than this age.
        Other character attributes: Filter by other character attributes like name, house, etc.

    Returns:
        JSON: A list of filtered characters.
    """
    filters = {key: value.lower() for key, value in request.args.items()}
    age_more_than = filters.pop('age_more_than', None)

    filtered_characters = characters

    if age_more_than:
        try:
            age_threshold = int(age_more_than)
            filtered_characters = [
                char for char in filtered_characters
                if 'age' in char and char['age'] and int(char['age']) > age_threshold
            ]
        except ValueError:
            return jsonify({"error": "Invalid age filter"}), 400

    for k, v in filters.items():
        filtered_characters = [
            char for char in filtered_characters
            if k in char and str(char[k]).lower() == v
        ]

    return jsonify(filtered_characters)


# Feature 4: Fetch a sorted character list - 10 Points
@app.route('/characters/sorted', methods=['GET'])
def sorted_characters():
    """Fetch a sorted list of characters based on a specified field.

    Query Parameters:
        sort_field (str): The field to sort by (e.g., name, age, house).
        order (str): The order of sorting, either 'asc' or 'desc' (default is 'asc').

    Returns:
        JSON: A sorted list of characters or an error message for invalid fields.
    """
    sort_field = request.args.get('sort_field', 'name')
    sort_order = request.args.get('order', 'asc')

    valid_sort_fields = {'name', 'age', 'house'}
    if sort_field not in valid_sort_fields:
        return jsonify({"error": f"Invalid sort field. Valid fields are: {', '.join(valid_sort_fields)}"}), 400

    try:
        sorted_characters = sorted(characters, key=lambda x: x.get(sort_field, '').lower())

        if sort_order.lower() == 'desc':
            sorted_characters = sorted_characters[::-1]

        return jsonify(sorted_characters)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Feature 5: Add a new character to the list - 25 points
@app.route('/characters', methods=['POST'])
def add_character():
    """Add a new character to the list.

    Request Body:
        JSON: Character data including id, name, house, role, age, death, strength, animal, symbol, nickname.

    Returns:
        JSON: The added character data or an error message for missing fields.
    """
    new_char = request.json
    required_fields = ["id", "name", "house", "role", "age", "strength"]

    if not new_char or not all(field in new_char and new_char[field] is not None for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    if not isinstance(new_char['age'], int) or new_char['age'] < 0:
        return jsonify({"error": "Age must be a non-negative integer"}), 400

    optional_fields = ["animal", "symbol", "nickname", "death"]

    for field in optional_fields:
        if field not in new_char:
            new_char[field] = None

    characters.append(new_char)
    save_characters()
    return jsonify(new_char), 201


# Feature 6: Edit a character - 30 points
@app.route('/characters/<int:id>', methods=['PATCH'])
def edit_character(id):
    """Edit an existing character's details.

    Args:
        id (int): The ID of the character to edit.
        Request Body:
            JSON: Fields to update in the character data.

    Returns:
        JSON: The updated character data or an error message if not found.
    """
    character = find_character_by_id(id)
    if not character:
        return abort(404, description="Character not found")

    data = request.json
    valid_fields = ["name", "house", "role", "age", "strength", "animal", "symbol", "nickname", "death"]

    # Update only valid fields
    for field in valid_fields:
        if field in data:
            character[field] = data[field]

    save_characters()
    return jsonify(character)


# Feature 7: Delete a character - 10 points
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    """Delete a character by their ID.

    Args:
        id (int): The ID of the character to delete.

    Returns:
        str: A success message or an error message if not found.
    """
    character = find_character_by_id(id)
    if not character:
        return abort(404, description="Character not found")

    characters.remove(character)
    save_characters()
    return jsonify({"message": "Character deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
