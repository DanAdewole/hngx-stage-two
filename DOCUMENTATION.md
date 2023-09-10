# Simple CRUD API Documentation

This documentation outlines the requirements and usage guidelines for the Simple CRUD API.

## Requirements

- Python 3.6 or higher
- Django 4 or higher

BASE URL: `http://localhost:5000/`

## Standard Formats
Append the following to the base URL to access the API

For each endpoint, the API follows the following request and response formats:

### Create Person (POST /api)
- **Request:**
	- HTTP Method: POST
	- Endpoint: `/api`
	- Request Body: 
		```
		json
		{
			"name": "agbaChakra"
		}
		```
- **Response:**
	- HTTP Status Code: 201 Created
	- Response Body:
		```
		json
		{
			"id": 1,
			"name": "agbaChakra"
		}
		```

### Read Person (GET /api)
- **Request:**
	- HTTP Method: GET
	- Endpoint: `/api`

- **Response:**
	- HTTP Status Code: 200 OK
	- Response Body:
		```
		json
		{
			"id": 1,
			"name": "agbaChakra"
		}
		```

### Read Single Person (GET /api/{id})
-  **Request:**
	- HTTP Method: GET
	- Endpoint: `/api/{id}`

- **Response:**
	- HTTP Status Code: 200 OK
	- Response Body:
		```
		json
		{
			"id": 1,
			"name": "Daniel"
		}
		```


### Update Person (PUT /api/{id})
-  **Request:**
	- HTTP Method: PUT
	- Endpoint: `/api/{id}`
	- Request Body:
		```
		json
		{
			"name": "Daniel"
		}
		```

- **Response:**
	- HTTP Status Code: 200 OK
	- Response Body:
		```
		json
		{
			"id": 1,
			"name": "Daniel"
		}
		```

### Delete Person (DELETE /api/{id})
- **Request:**
	- HTTP Method: DELETE
	- Endpoint: `/api/{id}`

- **Response:**
	- HTTP Status Code: 204 No Content


## Sample Usage

Below are some examples of how to use the API:

### Create a New Person

``` shell
curl -X POST -H "Content-Type: application/json" -d '{
	"name": "agbaChakra"
}' http://.../api

```

### Read a Person's Details

```shell
curl http://.../api/1
```

### Update a Person's Details

```shell
curl -X PUT -H "Content-Type: application/json" -d '{
	"name": 'Daniel"
} http://.../api/1
```

### Delete a Person

```shell
curl -X DELETE http://.../api/1
```
