# <i>Django CRUD</i>


## Description

Django CRUD is a Django web application that provides functionality for handling blog posts creation/deletion.

## Table of Contents

- [Set up project](#set-up-project)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Available routes](#available-routes)
- [Running Tests](#running-tests)

## Set up project

### Prerequisites
Before running the application, make sure you have the following dependencies installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repository to your local machine and make it your current working directory:

```
git clone https://github.com/RogerRabbit32/Python_Django---TestTask_CRUD.git
cd CRUD
```


2. Build and run the Docker container. Run the commands:

```
docker build -t <your-image-name> .
docker run -it -p 8000:8000 <your-image-name>
```
<i>NB! If you encounter permissions management issues on your system while running Docker commands, you can try using `sudo` to run the command with elevated privileges</i>


3. To stop the container, if run in interactive mode, use CTRL + C


If the installation is successful, your app should be available at [http://localhost:8000](http://localhost:8000)

## Available Routes

## DJoser Routes

### Register a New User

- **Endpoint**: `POST api/auth/users/`
- **Description**: Register a new user with the provided `username` and `password` fields in the request body.

### Generate an Access Token

- **Endpoint**: `POST api/auth/token/login/`
- **Description**: Generate an access token by sending a `POST` request with `username` and `password` fields in the request body. The response will contain the access token.

### Retrieve User Details

- **Endpoint**: `GET api/auth/users/me/`
- **Description**: Retrieve user details by sending a `GET` request to this endpoint with the user's access token in the `Authorization` header.

### Logout a User

- **Endpoint**: `POST api/auth/token/logout/`
- **Description**: Logout a user by sending a `POST` request to this endpoint with the user's access token in the `Authorization` header.

## Custom Routes

### Display All Users for Authenticated User

- **Endpoint**: `GET api/users/`
- **Description**: Retrieve a list of all users and their respective posts for any authenticated user. The request must include a valid access token in the Authorization header. 

### Display All User Posts

- **Endpoint**: `GET api/posts/`
- **Description**: Retrieves only the current user posts

### Create a Post

- **Endpoint**: `POST api/posts/`
- **Description**: Creates a new post with the current user as its author

### Delete a Post

- **Endpoint**: `DELETE api/posts/`
- **Description**: Deletes a post only if the current user is its author

## Running tests

When the containers are up, you can run the tests for the application by typing the following command in a new terminal:

```
docker exec <container id or name> pytest
```

This will execute the pytest autotests suite, stored in <b>/tests</b> directory
