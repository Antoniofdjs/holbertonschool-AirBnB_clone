#!/usr/bin/python3

"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
import json
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

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
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(f"{new_model.id}")

    def do_show(self, arg):
        """ Print string rprsnt of an instance based on the class and id"""
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
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
        """Deletes an instance based on the class name and id """
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
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
            #  Reload the dict back into file
            storage.save()

    def do_update(self, arg):
        """update <class name> <id> <attribute name> <attribute value>"""
        arg = arg.split()
        argc_dict = {
            0: "** class name missing **",
            1: "** instance id missing **",
            2: "** attribute name missing **",
            3: "** value missing **"
            }
        if len(arg) in argc_dict:
            print(f"{argc_dict[len(arg)]}")
        else:
            print("do stuff")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
