# Academicportal

## Libraries required:

- django-admin --version
* 3.2.7

- python --version
* Python 3.9.7

- Pandas 1.3.3

- Mysqlclient 2.0.3

- Numpy 1.21.2

- Pip 21.2.4

- Mysql-client  0.0.1

- Mysql-connector 2.29

- Mysql-connector-python 8.026

- Django-import-export 2.6.0

## Commands:
**pip install mysqlclient**

**python manage.py migrate**
> migrate executes those SQL commands in the database file. So after executing migrate all the tables of your installed apps are created in your database file.

**python manage.py makemigrations**
> makemigrations basically generates the SQL commands for preinstalled apps (which can be viewed in installed apps in settings.py) and your newly created apps' model which you add in installed apps. It does not execute those commands in your database file. So tables are not created after makemigrations

## Description:

We have used Pycharm for this project.We have installed the above libraries to run the code.In the code we have imported the required libraries.  For the database connection we have installed a Mysql workbench and imported the datasets there. And then we have given the credentials to access the server in the manage.py file. And by using the Mysql connector package we are able to make a connection with the database.

We have designed a template which fetches data from the xml file to the template using Javascript and test.dtd validates the xml file. We have used the “Web Server for Chrome“ app which serves web pages from a local folder over the network, using HTTP.Once you install it, navigate to http://127.0.0.1:8887 . We have uploaded a sample file which shows how the output template looks like after fetching data from xml. 



