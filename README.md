
# Flask API Student-Address Project

This project is a minimal viable API for managing student and address records. It provides endpoints for creating, reading, updating, and deleting student and address records in a database. The API also includes authentication to ensure that only authorized users can access its endpoints.




## Authentication

Authentication is implemented to restrict access to the API's endpoints. Users must register, login, and authenticate themselves to access the API's features securely.
## Endpoints

The API serves the following endpoints for both student and address resources:

#### Student Endpoints
POST /api/student: Creates a new record of a student in the database.

**GET** /api/student: Retrieves all students from the database.

**GET** /api/student/<student_id>: Retrieves a student by their ID.

**PATCH** /api/student/<student_id>: Updates a student's details.

**DELETE** /api/student/<student_id>: Removes a student from the database.

#### Address Endpoints

**POST** /api/address: Creates a new record of an address in the database.

**GET** /api/address: Retrieves all addresses from the database.

**GET** /api/address/<address_id>: Retrieves an address by its ID.

**PATCH** /api/address/<address_id>: Updates an address's details.

**DELETE** /api/address/<address_id>: Removes an address from the database.