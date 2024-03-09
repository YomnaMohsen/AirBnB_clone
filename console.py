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
    
    def postcmd(self, stop: bool, line: str) -> bool:

        if not stop:

            if line.strip() == "quit":

                print("$")

                return True

        return stop

if __name__ == '__main__':
    HBNBCommand().cmdloop()