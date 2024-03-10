#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd

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
  
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
