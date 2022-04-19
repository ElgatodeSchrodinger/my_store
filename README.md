## Template to build an API Rest using FastAPI and Postgresql

# Project Name: My Store

## Description
---
Simple API for Catalog System written with Python using FastAPI, SQL Alchemy.

### Construction 🛠️
* **Language:** Python 3
* **Framework:** FastAPI, SQL Alchemy
* **Database:** PostgreSQL

## Requirements
---
- Docker installed

## Installation and execution
---
Clone or Fork the project.

Run ```docker-compose``` command inside **docker-python** folder.

* Building the containers: ```docker-compose build```

* Starting the services: ```docker-compose up -d```

* Stoping the services: ```docker-compose stop```

By default the microservice will run under the following port:
- my_store_service: 8000

#### Note 🔍
The FastAPI application will probably throw an exception the first time, because it will try to connect to the PostgreSQL service that is still initializing for the first time; in this case wait for PostgreSQL to fully initialize first and then run the command `docker-compose restart my_store_service` in another terminal to restart the crashed service.

## Project Structure
---
The following diagram describe the project structure used for this API
```
my_store
│   .gitignore          
│   Dockerfile
│   README.md                   
│   docker-compose.yml     
│   requirements.txt          
│
└───app
│   │   .env
│   │   main.py
│   │
│   └───api                     Contains all modules for API uses
│   │   │
│   │   └───endpoints           Module for define endpoints
│   │   │   │   
│   │   │   │
│   │   │   └───auth.py         Endpoints related to Authentication
│   │   │   │
│   │   │   └───product.py      Endpoints related to CRUD Product
│   │   │   │
│   │   │   └───user.py         Endpoints related to CRUD Users
│   │   │   
│   │   └───utils.py            Functions that define what component from infrastructure will use for each service
│   │   
│   └───core                    Used to manage settings of the application
│   │   
│   └───domain                  Modules for Bussiness Logic (Ports)
│   │   │
│   │   └───auth                Logic for authenticate users
│   │   │
│   │   └───events              Message Bus for manage events
│   │   │
│   │   └───productManagment    CRUD Operation Logics for Products
│   │   │
│   │   └───userManagment       CRUD Operation Logics for Users
│   │   
│   │   
│   └───infrastructure          Modules for external services or libraries which the application interact (Adapters)
│   │   │
│   │   └───auth                Implementation of auth algorithms using external libraries
│   │   │
│   │   └───database            Implementation of Models using SQLAlchemy
│   │   │
│   │   └───notification        Implementation of Notifications Services (SES, others)
│   │   
│   └───tests                   Contains test suite for application
│   │   
...

```
### Architecture

In this project the ports and adapters architecture was applied. This allows the business logic to be separated from the specifications of each third-party component that is integrated into the system, in such a way that it is decoupled in interfaces and allows for better changeability. This means that when a change of an external service or its configuration is required, it will not affect the logic of the Domain. Another benefit of this architecture design is that it is much easier to test different levels by being able to replace real implementations with fake ones.
Following the principle of sole responsibility, a message bus was also contemplated to manage the different events, in the same way, decoupling external services.


## Documentation
---

The detailed API Documentation is available on the endpoint `http://localhost:8000/redoc`\
For somes tests you can also visit `http://localhost:8000/docs`

### Making a request

To make a request for all the store's products & users you would do the following in curl:

```curl 
curl -H 'Authorization: Bearer ACCESS_TOKEN ' \
  http://localhost:8000/products/5
```

where `ACCESS_TOKEN` is the store's access token (see Authentication).

### Authentication

This project follow the OAuth2 framework for letting users authorize use endpoints

To get the access token you need to run the following curl:
```curl 
curl --request POST \
  --url http://localhost:8000/token \
  --header 'Content-Type: multipart/form-data;' \
  --form username=admin@example.com \
  --form password=string \
  --form grant_type=password
```

#### Note 🔍 
The endpoint `POST /users` for create users was intentionally left freely accessible so that the first admin user can be created


## Testing ⚙️

To run the tests:

- Have the services running using `docker-compose up`.
- In another console, run `docker exec -it my_store_service pytest`.


### Authors ✒️

* **Author:** Javier Quintana, <javier.taipe.1998@gmail.com>