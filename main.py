from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

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
def get_character_by_id(id):
    character = find_character_by_id(id)
    if not character:
        abort(404, description="Character not found")
    return jsonify(character)


# Feature 3: Fetch a fIltered character list - 10 Points
@app.route('/characters/filter', methods=['GET'])
def filter_characters():
    filters = {key: value.lower() for key, value in request.args.items()}
    filtered = [char for char in characters if all(str(char.get(k, "")).lower() == v for k, v in filters.items())]
    return jsonify(filtered)


# Feature 4: Fetch a sorted character list - 10 Points
@app.route('/characters/sorted', methods=['GET'])
def sorted_characters():
    pass


# Feature 5: Add a new character to the list - 25 points
@app.route('/characters', methods=['POST'])
def add_character():
    pass


# Feature 6: Edit a character - 30 points
@app.route('/characters/<int:id>', methods=['PATCH'])
def edit_character(id):
    pass


# Feature 7: Delete a character - 10 points
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
