#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
import shlex
from models import storage


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
            
    def do_all(self,line):
        """prints all string representation of all instances 
        based or not on the class name"""
        args = shlex.split(line)
        if (len(args) == 0 or args[0] == "BaseModel"):
            inst_dict = storage.all()
            for key in inst_dict:
                obj = inst_dict[key]
                print(obj.__str__())
            
        elif (len(args) > 1 and args[0] != "BaseModel"):
            print("** class doesn't exist **")   

      
if __name__ == '__main__':
    HBNBCommand().cmdloop()
