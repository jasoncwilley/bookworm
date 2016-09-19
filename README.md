# Bookworm

A Django project for managing and organizing books on bookcases

## Setup
* `mkvirtualenv -p PYTHON_3_PATH bookworm`
* `pip install -r requirements.txt`
* Create an environment variable `SECRET_KEY`
* `./manage.py migrate`

## Run server
* `./manage.py runserver`


## Apps
A list of internal Django apps created for this project

### Bookcases
Bookcases app controls bookcases and what is in them.

#### Models
* Bookcase
    * name: A short descriptive name of the bookcase. Ex: "Dining Room Bookcase."
    * description: A longer optional descrtiption about the bookcase. Ex: "Located in the dining room, it has most of my cookbooks on it."
* Bookshelf
    * shelf_label: A short label that can be printed and stuck to the shelf to identify it on the bookcase.
    * bookcase: The bookcase that contains the bookshelf
* Book
    * title: The title of the book
    * genre: The genre the book belongs to
    * date_added: The date the book was added to the shelf
    * wikipedia_url: The wikipedia entry about this book
    * bookshelf: The shelf the book is on

### Core
Core Django app contains the base templates and static files to display the site and other base or miscellaneous pieces that don't fit in one of our other apps.
