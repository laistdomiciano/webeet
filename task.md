# webeet

## Backend Home Assignment

### **Objective**

Build a **RESTful API usin**g Python and Flask, or Express.js and Typescript that performs CRUD operations on a Python list (or a Javascript Array) representing a mock database of characters from a Game of Thrones (the list will be provided below in a `json` file). The API should handle operations like pagination, filtering, and validation, creating, editing and deleting characters.

### Project Overview

You will create a backend REST API that allows users to interact with a list of characters. The operations include getting all characters with pagination, filtering by fields, and CRUD operations (Create, Read, Update, Delete) for individual characters.

### **Requirements**

<aside>
⚠️

Make sure to use the write HTTP functions (GET, POST, PATCH, DELETE) for each one of the following functionalities. 

</aside>

- **Feature 1: Fetch all characters (with Pagination) - 10 Points**
    - Implement an endpoint that returns a list of characters.
    - Include pagination parameters: `limit` (number of results per page) and `skip` (number of results to skip).
    - If no limit or skip where defined, the API should return a maximum of random 20 characters from the entire list.
- **Feature 2: Fetch a specific character by ID - 5 Points**
    - Implement an endpoint to return a single character by their unique `id`.
- **Feature 3: Fetch a fIltered character list - 10 Points**
    - Implement more complex filtering options, such as combining multiple filters (e.g., filter by both `name` and `house`). There should be a filter option for each one of the characters’ attributes (name, house, role, age…).
    - For age, there should be also an option for a filter `age_more_than` and `age_less_then` to return a range of ages (i.e., `age_more_than=18` should return all the characters that their age is greater or equal to 18).
    - This should not be case sensitive, so for example `house=stark` should give the same result as `house=STArk`.
- **Feature 4: Fetch a sorted character list - 10 Points**
    - Implement sorting of the results based on different fields (e.g., sort by `name`, `age`, or `house`).
    - Allow for both ascending and descending order sorting (`sort_asc` and `sort_des`).

<aside>
⚠️

 Users should be able to filter and sort in the same request. 

</aside>

- **Feature 5: Add a new character to the list - 25 points**
    
    The server should ensure that all the relevant fields are not empty, and have information as expected (strings for example). Because we are not using a persistant data, the new character should saved in the list (on RAM).

  - **Feature 6: Edit a character - 30 points**
    
    Using the correct HTTP function, a user should be able to change any of the character’s fields. Not only the ones they created. They should use the ID of the character to change it.
    
- **Feature 7: Delete a character - 10 points**
    
    Users should be able to delete characters using a character ID.
    

### Important Notes

1. **Data Handling**:
    
    <aside>
    ⚠️ There is no Database, so you should use the following `json` file as a database. You can load it into a variable as list (into RAM), and then mutate the list (when POST, UPDATE, or DELETE are executed).
    
    You can download the file and use it in your code:
    
    [characters.json](https://prod-files-secure.s3.us-west-2.amazonaws.com/3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c/7ab1906f-449b-4f00-aa94-c1a69ea7544f/characters.json)
    
    </aside>
    
2. **Error Handling**:
    - Implement comprehensive error handling to cover cases like:
        - Requesting a character by an `id` that doesn't exist.
        - If the next “page” (using skip and limit) does not exist.
        - If we tried to filter by a non-existent attribute (for example `height` ).
     
  ### **Bonus Points (Optional)**

- **Authentication & Authorization:**
    - Create an endpoint (e.g., `/login`) that accepts a username and password.
    - Validate the username and password against a predefined list of users stored in the code (no database required).
    - If the credentials are valid, generate a JWT that includes the user's information (e.g., `username`, `role`).
    - Use a library such as `PyJWT` to generate and decode JWTs.
    - Ensure the JWT is signed with a secret key to prevent tampering.
    - Implement middleware to protect certain API endpoints (e.g., `POST`, `PUT`, `DELETE` operations).
    - The middleware should verify the JWT provided in the `Authorization` header of the request.
    - If the JWT is valid, allow the request to proceed; if not, return an appropriate error message and status code (e.g., `401 Unauthorized`).
- **Testing**:
    - Write unit tests for the API endpoints using a testing framework like `unittest` or `pytest`.
    - Cover various edge cases, such as invalid data, missing fields, and unauthorized access.
 
  - **Additional Features**:
    - Add any additional features you think would improve the functionality or user experience of the API.

### **Deliverables**

- **Source Code**:
    - A link to a **public** GitHub repository containing the project code with clear instructions on how to set up and run the project locally.
- **README.md**:
    - Include setup instructions, how to run the server, any assumptions you made, and a brief description of your approach.
    - Provide a list of all API endpoints, explaining what each one does, along with an example of how to use them.
- **Postman Collection**:
    - Provide a Postman collection with sample requests for each API endpoint. This will allow easy testing of the API.
 
    - 
Evaluation Criteria
Fail (<65)
Basic (65-84)
Good (85-100)
Great (>100)
Code Quality
Poorly organized, lacks comments, difficult to understand
Basic organization, minimal comments
Well-organized, adequately commented
Exceptionally clear, well-structured, with excellent comments and code readability
Functionality
Fails to meet core requirements
Meets core requirements with some issues
Fully meets core requirements with minor issues
Exceeds expectations, handles all core requirements smoothly without any issues
Error Handling
Little to no error handling
Basic error handling, some edge cases missed
Comprehensive error handling
Thorough and thoughtful error handling, covers all possible edge cases
Problem-Solving
Lacks effective solutions to challenges
Addresses challenges with basic solutions
Effective problem-solving with well-considered solutions
Innovative solutions, anticipates challenges and handles them proactively
Bonus Features
—
—
—
Implements multiple bonus features with high quality and enhances overall functionality
