#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """ command interpreter class

    Args:
        cmd.Cmd (class): class Cmd that conatins fn that
        parse and execute commands
    """
    prompt = "(hbnb) "
    __classes ={"BaseModel", "User", "State", "Review", "Place", "Amenity", "City"}

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
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()
            
    def do_all(self,line):
        """prints all string representation of all instances 
        based or not on the class name"""
        l_obj = []
        args = shlex.split(line)
        inst_dict = storage.all()
        
        if (len(args) > 0 and args[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")
        else: 
            for obj in inst_dict.values():
                if (len(args) == 0 or args[0] == obj.__class__.__name__):
                    l_obj.append(obj.__str__())
            print(l_obj)        
                  
        
    def do_show(self, line):
        """Prints the string representation of an instance 
        based on the class name and id"""
        args = shlex.split(line)
        inst_dict = storage.all()
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")  
        elif (len(args) < 2):
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1]) not in inst_dict.keys()):
            print("** no instance found **")     
        else:
            print(inst_dict["{}.{}".format(args[0], args[1])])
            
    def do_destroy(self, line):
        """ Deletes an instance based on the class name 
        and id (save the change into the JSON file"""
        args = shlex.split(line)
        inst_dict = storage.all()
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")  
        elif (len(args) < 2):
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1]) not in inst_dict.keys()):
            print("** no instance found **")
        else:
            del(inst_dict["{}.{}".format(args[0], args[1])])
            storage.save()
            
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or 
        updating attribute (save the change into the JSON file)"""
        args = shlex.split(line)
        inst_dict = storage.all()
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")  
        elif (len(args) < 2):
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1]) not in inst_dict.keys()):
            print("** no instance found **")
        elif (len(args) < 3):
            print("** attribute name missing **")
        elif (len(args) < 4):
            print("** attribute value missing **")
        else:
           setattr(inst_dict["{}.{}".format(args[0], args[1])],args[2], (args[3]))       
     
if __name__ == '__main__':
    HBNBCommand().cmdloop()
