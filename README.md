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

pip install -r requirements.txt

3. 	Run the application:

python app.py

API Endpoints

	•	GET /characters: Fetch all characters with optional pagination.
	•	GET /characters/<id>: Fetch a character by ID.
	•	GET /characters/filter: Fetch filtered characters based on query parameters.
	•	GET /characters/sorted: Fetch sorted characters based on query parameters.
	•	POST /characters: Add a new character.
	•	PATCH /characters/<id>: Edit an existing character by ID.
	•	DELETE /characters/<id>: Delete a character by ID.

Running Tests

pytest test_app.py

### Instructions

1. **`README.md`**: This file contains all the necessary information to understand, set up, and use your API.
2. **`requirements.txt`**: This file specifies the dependencies needed to run your application and tests.

Make sure to replace the placeholder in the README (like the GitHub link) with actual information. Let me know if you need any more modifications or additional information!

