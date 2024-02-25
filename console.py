#!/usr/bin/python3

"""
The console v:0.1
Contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex  # Tokenizes " strings like this" as one argument


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    __classes_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }
    __place_dict = {
        "city_id": str,
        "user_id": str,
        "name": str,
        "description": str,
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
        "amenity_ids": []
    }

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """ Ctrl + D to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes_dict:
            print("** class doesn't exist **")
        else:
            new_model = self.__classes_dict[arg]()  # Create instance
            new_model.save()
            print(f"{new_model.id}")

    def do_show(self, arg):
        """ Print string rprsnt of an instance based on the class and id"""
        arg = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.__classes_dict:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            dict_from_storage = storage.all()  # From storage{'name.id': obj}
            name_id = arg[0] + "." + arg[1]
            if name_id in dict_from_storage:
                print(f"{dict_from_storage[name_id]}")
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances;
            In case of "<classname>.count()" special arg is used
            From default method, we receive a "__special__case__"
            This will return a list instead of printing it
            Default will receive the list and print len
        """
        arg = shlex.split(arg)
        list_of_objs = []
        if not arg:
            for obj in storage.all().values():  # Gets all class objects
                list_of_objs.append(str(obj))
            print(list_of_objs)
        elif arg[0] not in self.__classes_dict:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if type(obj).__name__ == arg[0]:  # Add objs of specified class
                    list_of_objs.append(str(obj))
            if len(arg) > 1 and arg[1] == "__special__case__":
                return list_of_objs
            print(list_of_objs)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id """
        arg = shlex.split(arg)  # Tokenizes "strings like this" as one argument
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.__classes_dict:  # Check if class exists
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            dict_from_storage = storage.all()  # From storage{'name.id':object}
            name_id = arg[0] + "." + arg[1]
            if name_id in dict_from_storage:
                del dict_from_storage[name_id]
            else:
                print("** no instance found **")

            storage.save()  # Save changes to json

    def do_update(self, arg):
        """update <class name> <id> <attribute name> <attribute value>"""
        arg = shlex.split(arg)
        total_arguments = len(arg)
        argc_dict = {
            0: "** class name missing **",
            1: "** instance id missing **",
            2: "** attribute name missing **",
            3: "** value missing **"
            }

        if total_arguments in argc_dict:  # Prints error messages for argc
            print(f"{argc_dict[total_arguments]}")
        else:
            if arg[0] not in self.__classes_dict:  # Check if class exists
                print("** class doesn't exist **")
            else:
                class_name = self.__classes_dict[arg[0]]
                dict_from_storage = storage.all()  # Get dict from storage
                name_id = arg[0] + "." + arg[1]
                attribute = arg[2]
                attribute_value = arg[3]

                if name_id in dict_from_storage:
                    obj = dict_from_storage[name_id]  # Get object

                    """
                    Classes have class attributes with reserved values
                    we must cast the new value to the type of original
                    class attribute
                    """

                    if hasattr(class_name, attribute):
                        attribute_type = type(getattr(class_name, attribute))
                        attribute_value = attribute_type(attribute_value)
                    setattr(obj, attribute, attribute_value)
                    obj.save()  # Save new update date and storage changes
                else:
                    print("** no instance found **")

    def default(self, line):
        commands_dict = {
            "all()": self.do_all,
            "count()": self.do_all
            }

        #  Still woking this part below...
        arguments = line.split(".")  # split line by "."
        if len(arguments) > 1:
            class_name = arguments[0]
            command = arguments[1]

            if command in commands_dict:
                if command == "all()":  # Call do_all method
                    commands_dict[command](class_name)

                elif command == "count()":  # Call do_all with new arg
                    new_arg = class_name + " " + "__special__case__"
                    list_of_objs = commands_dict[command](new_arg)  # do_all
                    if list_of_objs is None:
                        pass  # Class doesnt exist msg will print
                    else:
                        print(f"{len(list_of_objs)}")

            else:
                self.do_help(str(line))  # Command doesnt exist
        else:
            self.do_help(str(line))  # Command doesnt exist


if __name__ == "__main__":
    HBNBCommand().cmdloop()
