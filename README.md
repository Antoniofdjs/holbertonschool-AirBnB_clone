# Holberton-AirBnB_clone
![AirbnbClone Logo](https://www.tabbykatz.com/hbnb.png)

## Description
The Airbnb_clone consists of 3 major components. One of them is the command-line interface (CLI) application ***-console.py-*** designed to manage Airbnb-like property listings and user interactions. This console provides functionalities to create, retrieve, update, and delete data related to various instances of the Airbnb ecosystem, including users, properties, reviews, places, and more.

At the core of the application lies the **FileStorage** engine, implemented through the ***-file_storage.py-*** module. This engine is managing data storage and retrieval operations. It handles the serialization and deserialization of instances to and from a JSON file, serving as a local database for the application. It offers functionalities such as retrieving all stored instances, saving the current state of data to the JSON file, and reloading data from the file into memory.The reload functionality is enabled by the file from: ***-models/__init__.py-***

The third major component is the **BaseModel** super class, implemented through the ***-base_model.py-*** module. BaseModel allows to create multiple instances based on it self or from the other subclasses. It assigns a random generated id with UUID, the date in wich the instances was created and the date when it was last updated. Any instance created from BaseModel will be saved to the storage.

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

| Commands   | Description                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------|
| `create`| Creates a new instance of the specified class, also prints id of the instance                         |
| `show`  | Print string representation of an instance based on the class and id                                  |
| `all`   | Prints list of string representation of all instances or just from specified class                    |
| `destroy`| Delete an instance based on the class name and id                                                    |
| `update`| Update values for an attribute of a specified instance from a class                                   |
| `.count()` | Prints total number of instances of a class or all instances                                       |
| `.all()`| Sub class representing User instance.                                                                 |
| `quit`| Exit console                                                                                            |
| `help`| Display available commands                                                                              |
## Use 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Installing:

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

```
git clone git@github.com:Antoniofdjs/holbertonschool-AirBnB_clone.git
```
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

## This is how it would work:

The console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) quit
$
```

## Examples

* **create**
  * Usage: `create <class>`

```
$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb) quit
$ cat file.json
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T2
1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}
```

* **show**
  * Usage: `show <class> <id>`

```
$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb) 
```

* **destroy**
  * Usage: `destroy <class> <id>`

```
$ ./console.py
(hbnb) create Place
3e-8329-4f47-9947-dca80c03d3ed
(hbnb) destroy Place 3e-8329-4f47-9947-dca80c03d3ed
(hbnb) 
(hbnb) quit
$ cat file.json
{}
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()` or `.all()`

```
$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb) create User
b742dbc3-f4bf-425e-b1d4-165f52c6ff81
(hbnb) create User
8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
(2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
(hbnb) User.all()
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User] 
(b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2
, 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44,
15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
(hbnb) 
(hbnb) all
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
del] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(20
19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21,
45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 2
1, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 97
4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 4
3, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348
), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb) quit
$
```

* **count**
  * Usage: `<class>.count()` or `.count()`

```
$ ./console.py
(hbnb) create Place
12c73223-f3d3-4dec-9629-bd19c8fadd8a
(hbnb) create Place
aa229cbb-5b19-4c32-8562-f90a3437d301
(hbnb) create City
22a51611-17bd-4d8f-ba1b-3bf07d327208
(hbnb) .count()
3
(hbnb) city.count()
1
(hbnb) quit
$
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"`

```
$ ./console.py
(hbnb) create User
6f348019-0499-420f-8eec-ef0fdc863c02
(hbnb)
(hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
time.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
ef0fdc863c02'}
(hbnb) quit
$
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
