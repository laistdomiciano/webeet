
# Additional Features:
- requirements.txt: makes it easy to replicate the same environment
- Swagger: allows users to easily explore and test the API
- Added pre-commit confiuration: prevent broken code of being commited


# Further ideas for improvement (if I had more time):
- Authentication & Authorization - Bonus point in the assignment
- Create a better database: SQLite, PostgreSQL
  - Deploy database
- Create a UI - work on the Frontend


# Why I did what I did?

## Fetch all characters (with Pagination) - 10 Points
GET /characters: Fetch all characters with optional pagination.
- I went with skip and limit for pagination because it gives users control over how much data they want and where to start. 
- I used Python’s list slicing ([skip:skip + limit]) since it’s simple and works well with in-memory data.


## Feature 2: Fetch a specific character by ID - 5 Points
GET /characters/<id>: Fetch a character by ID.
- I created a separate function for finding characters by ID to avoid repeating code. This way, the same logic is reused across different endpoints, keeping things clean and maintainable.


## Feature 3: Fetch a fIltered character list - 10 Points
GET /characters/filter: Fetch filtered characters based on query parameters.
- I made the filters case-insensitive (.lower()) so users don’t have to worry about capitalization.
- Instead of hardcoding filters, I used request.args to build them dynamically, which makes it easy to filter by any character attribute.
- I also added a special filter for age_more_than because sometimes you want to search by a range, not just an exact number.


## Feature 4: Fetch a sorted character list - 10 Points
GET /characters/sorted: Fetch sorted characters based on query parameters.
- I used Python’s sorted() with a lambda function to allow sorting by any field (like name or age). 
- For descending order, I just reversed the sorted list ([::-1]), which is quick and keeps the code simple.


## Feature 5: Add a new character to the list - 25 points
POST /characters: Add a new character.
- I’m appending new characters to the list in memory for now because that’s fast and fits the task, but a real app would need a database.


## Feature 6: Edit a character - 30 points
PATCH /characters/<id>: Edit an existing character by ID.
- I used update() to apply changes dynamically.


## Feature 7: Delete a character - 10 points
DELETE /characters/<id>: Delete a character by ID.
- I’m removing characters by their unique ID using remove()


## Error handling
- Detailed error messages for things like 404 (not found) or 400 (bad input) help users know exactly what went wrong and how to fix it.


## Debug=True
- I enabled debug=True for development so I could easily catch and fix bugs. Of course, this would be turned off in a production environment.
