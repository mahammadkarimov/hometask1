
# User API Documentation

This API allows users to GET a list of users and POST a new user to the system. It uses simple memory or CSV storage to manage users.

## Base URL

http://localhost:8080


## Endpoints

### 1. Get All Users
Endpoint: `GET /users`  
Description: Fetches a list of all users stored in the system.  
Response:
- 200 OK: A JSON array containing all users.
- 404 Not Found: If the endpoint is not found.

Response Example:
[
    {
        "id:"uuid",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    },
    {
        "id":"uuid",
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com"
    }
]

Error Response Example (404 Not Found):
{
    "error": "404"
}


### 2. Create User
Endpoint: `POST /users`  
Description: Creates a new user in the system. The user must provide `first_name`, `last_name`, and `email` in the request body.  
Request Body:  

{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}


Response:
- 201 Created: Returns the created user with the provided details.
- 400 Bad Request: If required data is missing or the data is invalid.

Response Example:
{
    "id":"uuid",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}


Error Response Example (400 Bad Request):
{
    "error": "Missing or invalid data"
}


---

## Error Codes

| **Error Code** | **Description**                              |
|----------------|----------------------------------------------|
| **404**        | Endpoint not found.                          |
| **400**        | Bad request, usually caused by missing or invalid input. |

