# Holberton-AirBnB_clone

### Table of Contents

- [Description](#description)
- [Files](#files)
- [Commands](commands)
- [Use](#use)
- [Examples](#examples)
- [Resources](#resources)
- [Credits](#credits)
  
## Description
The Airbnb Console is a command-line interface (CLI) application designed to manage Airbnb-like property listings and user interactions. This console provides functionalities to create, retrieve, update, and delete data related to various instances of the Airbnb ecosystem, including users, properties, reviews, and more.



## Files

| Files                  | Content                                           |
|------------------------|---------------------------------------------------------|
| *README.md*     | Contains Description of Project                                              |
| *console.py*    | Command interpreter using cmd import                                         |
| *file_storage.py*  | Serializes instances to a JSON file and deserializes JSON file back to instances|  
| *base_model.py*     | Super class, the base for all sub classes                                   |
| *console.py*     | Command interpreter using cmd import                                         |
| *user.py*     | User sub class, the base for user instances                                      |


## Commands

| Commands   | Description                                                                                           |
|-----------|-------------------------------------------------------------------------------------------------------|
| `create`| Creates a new instance of the specified class, also prints id of the instance                         |
| `show`  | Print string representation of an instance based on the class and id                                  |
| `all`   | Prints list of string representation of all instances or just from specified class                     |
| `destroy`| Delete an instance based on the class name and id                                                      |
| `update`| Update values for an attribute of a specified instance from a class                                    |
| `count` | Prints total number of instances of a class or all instances                                           |

## Use 
To start using the console...


```
exampleeee hereee
```
In the console running

```
usagee examplee
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

 - *[Example_resource](link_here)*


## Credits

 - *[Antonio De Jesus Santiago](https://github.com/Antoniofdjs)*
 - *[Juan Gabriel Collazo](https://github.com/juancollazo5)*
