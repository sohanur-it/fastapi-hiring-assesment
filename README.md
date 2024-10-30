# FastAPI Assignment

## Objective

The goal of this assignment is to develop a simple FastAPI application that connects to a PostgreSQL database and performs CRUD (Create, Read, Update, Delete) operations asynchronously to manage a bookstore.

## Project Description

Each book will have the following properties:

```
id: Auto-incremented unique identifier for each book (primary key)
title: Title of the book (string, required)
author: Author of the book (string, required)
description: Description of the book (string, optional)
price: Price of the book (float, required)
is_available: Boolean to indicate whether the book is currently available for purchase (default is True)
```

## Required Endpoints

* Create a new book
* Retrieve all books (with additional filtering based on availability)
* Retrieve a single book by ID
* Update an existing book
* Delete a book by ID


## Requirements

Technical Stack:

* FastAPI for the web framework
* PostgreSQL for the database
* SQLAlchemy
* Docker for containerization

## Expectations

* Asynchronous database operations
* Data validation: Validate request data using Pydantic models
* Dockerization: Provide a Dockerfile and a docker-compose.yml file to easily spin up the FastAPI app and PostgreSQL instance
* Assume any information that is not provided

## Submission Instructions

* Fork the repository and submit the link to your GitHub repository
* Ensure that the project can be run and tested easily using the instructions provided in your README file

**Note: Make sure you use all the best practices wherever possible and provide an explanation for choosing otherwise.**
