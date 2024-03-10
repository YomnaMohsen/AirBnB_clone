#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """ command interpreter class

    Args:
        cmd.Cmd (class): class Cmd that conatins fn that
        parse and execute commands
    """
    prompt = "(Hbnb)"

    def do_EOF(self, line):
        """function handles EOF command"""
        return True
                
    def do_quit(self, line):
        """function handles quit command"""
        return True
    
    def help_quit(self):
        print("Quit command to exit the program")
        
    def help_EOF(self):
        print("EOF (end of file) command to exit the program")   
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
