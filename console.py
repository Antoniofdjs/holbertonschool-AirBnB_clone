#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        quit()

    def help_quit(self, arg):

        print("Command to exit the program")

    def do_EOF(self, arg):
        """ Ctrl + D to exit the program"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
