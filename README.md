# Holberton-AirBnB_clone
!https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240227%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240227T103738Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=116ac1ced4e13c97d9c07d0c8523fb5d5b6db1ee10d273bc21727408aee9e15f

## Description
The Airbnb Console is a command-line interface (CLI) application designed to manage Airbnb-like property listings and user interactions. This console provides functionalities to create, retrieve, update, and delete data related to various instances of the Airbnb ecosystem, including users, properties, reviews, places, and more.

At the core of the application lies the FileStorage engine, implemented through the file_storage.py module. This engine is managing data storage and retrieval operations. It handles the serialization and deserialization of instances to and from a JSON file, serving as a local database for the application. It offers functionalities such as retrieving all stored instances, saving the current state of data to the JSON file, and reloading data from the file into memory.

### Table of Contents

- [Description](#description)
- [Files](#files)
- [Commands](#commands)
- [Use](#use)
- [Examples](#examples)
- [Resources](#resources)
- [Credits](#credits)
  

## Files

| Files                  | Content                                           |
|------------------------|---------------------------------------------------------|
| [*README.md*](README.md) | Contains the description of the project and usage instructions. |
| [*console.py*](console.py)| Command interpreter using the cmd module.|                      |
| [*file_storage.py*](models/engine/file_storage.py) | Serializes instances to a JSON file and deserializes JSON file back to instances.|  
| [*models/__init__.py*](models/__init__.py) | Init for reloading from JSON file to storage|
| [*base_model.py*](models/base_model.py) | Super class serving as the base for all subclasses.   |
| [*user.py*](models/user.py) | Sub class representing User instance. |
| [*city.py*](models/city.py) | Sub class representing City instance. |
| [*place.py*](models/place.py) | Sub class representing Place instance.|
| [*review.py*](models/review.py) | Sub class representing Review instance.|
| [*state.py*](models/state.py) | Sub class representing State instance.|
| [*amenity.py*](models/amenity.py) | Sub class representing User instance. |


## Commands

| Commands   | Description                                                                                           |
|-----------|-------------------------------------------------------------------------------------------------------|
| `create`| Creates a new instance of the specified class, also prints id of the instance                         |
| `show`  | Print string representation of an instance based on the class and id                                  |
| `all`   | Prints list of string representation of all instances or just from specified class                     |
| `destroy`| Delete an instance based on the class name and id                                                      |
| `update`| Update values for an attribute of a specified instance from a class                                    |
| `count()` | Prints total number of instances of a class or all instances                                           |

## Use 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installing

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

```
git clone git@github.com:Antoniofdjs/holbertonschool-AirBnB_clone.git
```
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

##This is how it would work:

The console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

To run .count() command

```
(hbnb) .count()
```
Basic usage example


## Examples

```
(hbnb) all
[]     
(hbnb) create User
be9d66bf-a5a3-4c5d-8de5-6afb86bad424
(hbnb) all
["[User] (be9d66bf-a5a3-4c5d-8de5-6afb86bad424) {'id': 'be9d66bf-a5a3-4c5d-8de5-6afb86bad424',
'created_at': datetime.datetime(2024, 2, 25, 19, 42, 26, 233003),
'updated_at': datetime.datetime(2024, 2, 25, 19, 42, 26, 233003)}"]
(hbnb) destroy User be9d66bf-a5a3-4c5d-8de5-6afb86bad424
(hbnb) all                                               
[]     
(hbnb) 
```

## Resources

 - *[CMD Module](https://docs.python.org/3/library/cmd.html)*
- *[UUID Module](https://docs.python.org/3/library/uuid.html)*
- *[Datetime Module](https://docs.python.org/3/library/datetime.html)*
- *[args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)*
- *[Python Test Sheets](https://www.pythonsheets.com/notes/python-tests.html)*



## Credits

 - *[Antonio De Jesus Santiago](https://github.com/Antoniofdjs)*
 - *[Juan Gabriel Collazo](https://github.com/juancollazo5)*
