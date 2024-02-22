#!/usr/bin/python3

"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd

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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
