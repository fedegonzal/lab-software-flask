# Laboratorio de Software

## Universidad Nacional de Tierra del Fuego, Argentina

### REST API with Flask

This project is a simple example of a REST API using Flask, a Python microframework. It's part of the Software Laboratory course at the National University of Tierra del Fuego, Argentina.

The API is a simple CRUD (Create, Read, Update, Delete) example to manage Universities. It has the following endpoints:

### Installation

1. Clone the repository
2. Create a virtual environment
3. Install the dependencies
4. Run the DB seed (to create the databse from seed.csv)

```bash
# Clone the repository
git clone git@github.com:fedegonzal/lab-software-flask.git
cd lab-software-flask

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Run the DB seed
python seed.py
```

### About Virtual Environments

A Virtual Environment is a tool to keep dependencies required by different projects in separate places, by creating virtual Python environments. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

Most common commands with virtual environments are:

- `python3 -m venv venv`: Create a virtual environment
- `source venv/bin/activate`: Activate the virtual environment
- `deactivate`: Deactivate the virtual environment

### About Flask and the libraries used

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies, and several common framework related tools.

In our case, we are using Flask with SQLAlchemy and Marshmallow. SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language. Marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

### About SQLite

SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. 

SQLite is built into all mobile phones, browsers, most computers, and comes bundled inside countless other applications that people use every day.

### Running the API

To run the API, you can use the following command:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`

### Endpoints

- `GET /universities`: List all universities
- `GET /universities/<id>`: Get a university by ID
- `POST /universities`: Create a new university
- `PUT /universities/<id>`: Update a university by ID
- `DELETE /universities/<id>`: Delete a university by ID

Do not forget to add the `Content-Type: application/json` header when sending data to the API. Also remember to send the data in JSON format.

### Useful tools

- [HTTPie](https://httpie.io/): HTTPie is a command-line HTTP client for the API era. Its goal is to make CLI interaction with web services as human-friendly as possible. It provides a simple http command that allows for sending arbitrary HTTP requests using a simple and natural syntax, and displays colorized responses. HTTPie can be used for testing, debugging, and generally interacting with HTTP servers. A new graphical user interface is also available for those who prefer a more visual experience.

- [Postman](https://www.postman.com/): Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster.

- [DBeaver](https://dbeaver.io/): DBeaver is a free multi-platform database tool for developers, database administrators, analysts, and all people who need to work with databases. It supports all popular databases: MySQL, PostgreSQL, SQLite, Oracle, DB2, SQL Server, Sybase, MS Access, Teradata, Firebird, Apache Hive, Phoenix, Presto, etc.
