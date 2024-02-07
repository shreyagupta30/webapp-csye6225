# webapp application for CSYE-6225 Network Structures and Cloud computing (Spring 2024)

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
```
CREATE DATABASE your_database_name;
```
- Grant all privileges to the user
```
GRANT ALL PRIVILEGES ON <your_database_name.> TO <your_username>;
```
- Update all the information in an .env file
SAMPLE .env:

```
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
```
 python manage.py makemigrations
```
now, 
``` 
python manage.py migrate
```
- Run the server
```
python manage.py runserver
```

## Endpoints to get if the server connection is healthy

``` 
GET /healthz
```
This should return, 
STATUS CODE 200 if the connection is healthy.
