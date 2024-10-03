from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

with open('characters.json', 'r') as file:
    characters = json.load(file)


#Fetch all characters (with Pagination) - 10 Points
@app.route('/characters', methods=['GET'])
def get_characters():
    pass


#Feature 2: Fetch a specific character by ID - 5 Points
@app.route('/characters/<int:id>', methods=['GET'])
def get_character_by_id(id):
    pass

#Feature 3: Fetch a fIltered character list - 10 Points
@app.route('/characters/filter', methods=['GET'])
def filter_characters():
    pass


#Feature 4: Fetch a sorted character list - 10 Points
@app.route('/characters/sorted', methods=['GET'])
def sorted_characters():
    pass


#Feature 5: Add a new character to the list - 25 points
@app.route('/characters', methods=['POST'])
def add_character():
    pass


#Feature 6: Edit a character - 30 points
@app.route('/characters/<int:id>', methods=['PATCH'])
def edit_character(id):
    pass


#Feature 7: Delete a character - 10 points
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    pass

