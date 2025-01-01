## A Flask REST API
### This repository implements a simple REST API using the Flask microframework.

#### Installation
1. Create a virtual environment:

- Isolate project dependencies using a virtual environment. You can use python3 -m venv .venv to create one named .venv.
- Activate the virtual environment using . .venv/bin/activate.
Install Flaskr:

2. Install the project in editable mode using pip install -e .. This allows you to make changes to the code and test them without reinstalling.

#### Usage

1. Initialize the database:

- Create the database schema (if applicable).
```shell
flask --app flaskr init-db 
```
2. Run the development server:

- Start the development server with 
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
*This install any additional packages needed for running tests.*

2. Run tests:
```shell
pytest
```
*This will discover and run all test cases in the project. 

3. Generate coverage report:

```shell
run -m pytest
```
- *This will execute tests while collecting coverage data.
To get an overview of code coverage, use coverage* 


- Generates a human-readable coverage report using coverage report.
- For a more detailed HTML report, run coverage html.
    - This will create an HTML report in the htmlcov directory,
 which you can open in your browser (usually file:///path/to/project/htmlcov/index.html).