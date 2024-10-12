# Character API

This is a Flask-based API for managing a collection of characters. It provides endpoints for fetching, filtering, adding, editing, and deleting character data.

## Features

1. **Fetch all characters**: Supports pagination with `limit` and `skip` parameters.
2. **Fetch a specific character by ID**: Retrieve character details using their unique ID.
3. **Filter characters**: Fetch a list of characters based on various criteria, including age.
4. **Sort characters**: Retrieve a sorted list of characters based on a specified field and order.
5. **Add a new character**: Add new character details to the collection.
6. **Edit a character**: Update existing character information.
7. **Delete a character**: Remove a character from the collection.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/laistdomiciano/webeet.git
   cd webeet

2. Install the required packages:

pip3 install -r requirements.txt

3. 	Run the application:

python3 app.py

API Endpoints

	•	GET /characters: Fetch all characters with optional pagination.
       •	Query parameters:
          •	limit: The number of characters to return (default: 20).
          •	skip: The number of characters to skip from the start (default: 0).
	•	GET /characters/<id>: Fetch a character by ID.
	•	GET /characters/filter: Fetch filtered characters based on query parameters.
       •	Query parameters (any of the following):
          •	house: Filter characters by house.
          •	role: Filter characters by role.
          •	age_more_than: Return characters whose age is greater than the specified value.
	•	GET /characters/sorted: Fetch sorted characters based on query parameters.
       •	Query parameters:
          •	sort_field: Field to sort by (default: name).
          •	order: Sort order (asc for ascending or desc for descending, default: asc).
	•	POST /characters: Add a new character.
          •	Body: JSON object containing the following fields:
          •	id, name, house, role, age, death, strength (all required).
	•	PATCH /characters/<id>: Edit an existing character by ID.
          •	Body: JSON object with the fields to update.
          •	DELETE /characters/<id>: Delete a character by ID.

Running Tests

pytest test_app.py

License

This project is licensed under the MIT License.

### Instructions

1. **`README.md`**: This file contains all the necessary information to understand, set up, and use your API.
2. **`requirements.txt`**: This file specifies the dependencies needed to run your application and tests.


