#!/usr/bin/python3

"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
import shlex  # Tokenizes " strings like this" as one argument


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    __classes_dict = {"BaseModel" : BaseModel, "User": User}

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
            new_model = self.__classes_dict[arg]()  # Creates instance thanks to dict
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
            dict_from_storage = storage.all()  # Load dict from storage {'name.id': object}
            name_id = arg[0] + "." + arg[1]
            if name_id in dict_from_storage:
                print(f"{dict_from_storage[name_id]}")
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id """
        arg = shlex.split(arg)  # Tokenizes " strings like this" as one argument
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.__classes_dict:  # Check if class exists
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            dict_from_storage = storage.all()  # Load dict from storage {'name.id': object}
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
                dict_from_storage = storage.all()  # Get dict from storage
                name_id = arg[0] + "." + arg[1]
                attribute = arg[2]
                atribute_value = arg[3]

                if name_id in dict_from_storage:
                    obj = dict_from_storage[name_id]  # Get object
                    setattr(obj, attribute, atribute_value)
                    obj.save()  # Save new update date and storage changes
                else:
                    print("** no instance found **")    


if __name__ == "__main__":
    HBNBCommand().cmdloop()
