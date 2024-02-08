# Webapp application for CSYE-6225 Network Structures and Cloud computing (Spring 2024)

## Requriemnts to install this project
- Pipenv 
To install, run `pip install pipenv`
- Fork the repository and then clone the repository
To clone, run ` git clone <https://github.com/Spring2024-CSYE6225/webapp.git>`
- Activate the environment at the root of the webapp folder
` pipenv shell`
- Install all the dependencies
` pipenv install`

## Creating a postgreSQL database
On a new terminal window
- Create a postgreSQL database

```bash
CREATE DATABASE your_database_name;
```

- Grant all privileges to the user

```bash
GRANT ALL PRIVILEGES ON <your_database_name.> TO <your_username>;
```

- Update all the information in an .env file
    -  SAMPLE .env:

    ```bash
    DEBUG='True'
    DB_HOST=localhost
    DB_NAME=<test>
    DB_USER=<test>
    DB_PASSWORD=<test>
    DB_PORT=5432
    ```
- Start your postgreSQL server

## Run the application

- Run all the migrations
```bash
 python manage.py makemigrations
```
now, 
``` bash
python manage.py migrate
```
- Run the server
```bash
python manage.py runserver
```

## Endpoints to get if the server connection is healthy

``` bash
GET /healthz
```
This should return, 
STATUS CODE 200 if the connection is healthy.

## User auuthentication endpoints

```bash
POST /v1/user
```
Body:
```json
{  
    "username": "test@gmail.com",
    "firstname":"tester",
    "lastname":"tester",
    "password":"password!!!"
}
```

Sample response:

```bash
{
    "id": "49e5d3b6-62d9-441e-9cb6-a025ac92993d",
    "username": "test@gmail.com",
    "firstname": "tester",
    "lastname": "tester",
    "account_created": "2024-02-07T23:58:34.202651Z",
    "account_updated": "2024-02-07T23:58:34.202665Z"
}
```

```bash
GET /v1/user/self
```
This is an authenticated route, the user must provide appropriate username and password to get response. 

Sample response when authenticated:
```bash
{
    "id": "49e5d3b6-62d9-441e-9cb6-a025ac92993d",
    "username": "test@gmail.com",
    "firstname": "shreya",
    "lastname": "guptaaa",
    "account_created": "2024-02-07T23:58:34.202651Z",
    "account_updated": "2024-02-07T23:58:34.202665Z"
}
```

Sample response when unauthenticated:

```bash
{
    "detail": "Authentication credentials were not provided."
}
```

```bash
PUT /v1/user/self
```
This is an authenticated route, the user must be authenticated to modify only fields like 
- password
- firstname
- lastname

If the user tries to change fields like `username`, `account_created` and `account_updated` the status code `400 BAD REQUEST` is raised. 
