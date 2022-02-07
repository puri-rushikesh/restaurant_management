INTRODUCTION
------------

The Restaurant management project allows to perform basic CRUD operations.
Here we have used Postgresql as Database.
Directories & Files:
    * data : Contains Sample Data
    * log : Contains day specific logs of the execution
    * test_cases : Contains unit test cases
    * main.py : Contains services for CRUD operation
    * restaurant_operations : Contains Core logic for CRUD operation


REQUIREMENTS
------------

This project requires packages mentioned in requirements.txt:
Step to install requirements:
 * pip install -r requirements.txt  -> Execute this command in command prompt where the requirements.txt is located.


SAMPLE DATA
-----------

Execute insert_data.py file to get started with the sample data.
It will create the postgres.public.restaurant table.


EXECUTION
---------

Run main.py file to start the services.
Services will be hosted by default on http://127.0.0.1:5000/


TESTING
-------

Configure appropriate unit test case to validate each service.