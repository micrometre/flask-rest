## A Flask REST API
### This repository implements a simple REST API using the Flask microframework.

#### Routes
- /auth/user 
    - Register a new user
- /auth/login
    - Login with a Registered user
- /api/uploads
    - Simple File upload Route
- /api/forms
    - Simple Forms submission

*The data for the forms submitted and the registered users name and password are stored in a lite sqlite data base.*

#### Installation
1. Create a virtual environment:

- Isolate project dependencies using a virtual environment. 

```shell
python3 -m venv .venv 
#to create one named .venv.
```
- Activate the virtual environment using 
```shell
. .venv/bin/activate.
```

Install Flaskr:

2. Install the project in editable mode 
```shell
pip install -e . 
#This allows you to make changes to the code and test them without reinstalling.
```
#### Usage

1. Initialize the database:

```shell
flask --app flaskr init-db 
```

- Start the development server 
```shell
flask --app flaskr run --debug. 
```
*This will enable debugging features and make the API accessible at http://127.0.0.1:5000 in your browser.*

#### Testing
Install test dependencies:

1. Install requirements 
```shell
pip install '.[test]. 
```
*Install any additional packages needed for running tests.*

2. Run tests:
```shell
pytest
```
*This will discover and run all test cases in the project.* 

3. Generate coverage report:

```shell
coverage run -m pytest
```
*This will execute tests while collecting coverage data To get an overview of code coverage.* 


4. Generate a human-readable coverage report 
```shell
coverage report
```

5. For a more detailed HTML report

```shell
 coverage html
```
*This will create an HTML report in the htmlcov directory*