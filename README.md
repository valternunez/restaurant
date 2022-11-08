# Restaurant REST API
##  About the project

This API serves as an demo of what I'm able to do with **Django** and the **Django REST Framework**.
The project is called *'Restaurant*' and it emulates a food business that gets orders from clients through their API. They obtain 4 fields:

 - Client's Name
 - Client's Phone Number
 - Client's Address
 - Client's Order

In this project, the restaurant can visualize the incoming data in real-time through a front-end.

## How to run it

### Pre-requisites
 - Docker
 - Git
 - Postman (or similar)


### Installation
 1. Download the project from the GitHub repository inside your preferred location in your local computer.

	    git clone https://github.com/valternunez/restaurant.git

 2. Enter the folder just created.

	    cd restaurant

 3. Create the containers on Docker.

	    docker-compose up -d --build

 4. When the containers are done, you will need to run migrations. 

	    docker-compose exec web python manage.py migrate

 5. *(Optional)* If you want to create an admin/super user, you can run the next command.

	    docker-compose exec web python manage.py createsuperuser

Now the project is running! Go to http://localhost:8000/api/orders to see the list of orders. (Which will be empty at the moment)

## API's Usage

### POST - Create a new order
Send a POST request to http://localhost:8000/api/

On the *Body*, select *Raw* data of type *JSON* and send a valid JSON. Here is an example:

	{
		"client_name":  "Fernando Rosales",
		"client_address":  "El Rosal #14, Colonia Arboledas",
		"client_phone":  "+554422471349",
		"client_order":  "2 sandwiches y 5 cervezas"
	}
### GET  - Obtain all orders
Send a GET request to http://localhost:8000/api/

### GET  - Obtain a specific order
Send a GET request to http://localhost:8000/api/1   (change the number to the id of the order you want to obtain)

### PUT - Update an existing order
Send a PUT request to http://localhost:8000/api/1   (change the number to the id of the order you want to update)

On the *Body*, select *Raw* data of type *JSON* and send a valid JSON. Here is an example:

	{
		"client_name":  "Miguel De la Madrid",
		"client_address":  "El Rosal #14, Colonia Arboledas",
		"client_phone":  "+554422471349",
		"client_order":  "1 sandwich y 1 Boing de mango"
	}

### DELETE - Remove an existing order
Send a DELETE request to http://localhost:8000/api/1   (change the number to the id of the order you want to remove)

## Front-end visualization
Go to http://localhost:8000/api/orders to see the list of all orders. From that view you can see the detail of each order. 

If you add, update or remove an order, you'll see the change in the front-end at most 5 seconds later. 