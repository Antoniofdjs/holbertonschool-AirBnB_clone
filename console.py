#!/usr/bin/python3

"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
import json

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
            try:
                with open("file.json", 'r') as file:
                    dict_from_json = json.load(file)
                    name_id = arg[0] + "." + arg[1]
                    if name_id in dict_from_json:
                        obj_dict = dict_from_json[name_id]
                        print(f"{BaseModel(**obj_dict)}")
                    else:
                        print("** no instance found **")
            except FileNotFoundError:
                print("** file not found **")
    
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
            try:
                with open("file.json", 'r') as file:
                    dict_from_json = json.load(file)
                    name_id = arg[0] + "." + arg[1]
                    if name_id in dict_from_json:
                        del dict_from_json[name_id]
                    else:
                        print("** no instance found **")
            except FileNotFoundError:
                print("** file not found **")

            #  Reload the data back into dictionary
            try:
                with open("file.json", 'w') as file:
                    json.dump(dict_from_json, file)
            except FileNotFoundError:
                print("** file not found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
