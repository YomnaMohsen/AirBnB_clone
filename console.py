#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """ command interpreter class

    Args:
        cmd.Cmd (class): class Cmd that conatins fn that
        parse and execute commands
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
         
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
 
    def emptyline(self):
        """prints empty line"""
        pass
    
    def do_create(self, line):
        """create new instances from different classes"""
        args = shlex.split(line)
        if(len(args) < 1):
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            B = BaseModel()
            B.save()
            print(B.id)
        

      
if __name__ == '__main__':
    HBNBCommand().cmdloop()
