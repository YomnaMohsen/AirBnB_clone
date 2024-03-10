# Description of the project

The goal of the project is to build a simple web application like the AirBnB website.

# Main feature
Phase 1: A command interpreter to manipulate data without a visual interface, which make the user able to create, destory, update and reterive objects through the terminal

# What’s a command interpreter?
It is a program, it behaves like shell, it accepts commands from user then excutes them
# commands 
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

# How to use command interpreter
* first we need to run script console.py (./console.py), once the script is executed  a prompt like this
"(hbnb)" will appear.
* The user can enter any allowed command or type help command to get info about thsi command

* the interpreter can run in either interactive mode, as described in the above line or in non interactive mode like this echo "help" | ./console.py

# Main components of project:

BaseModel class: the base class for all sub_classes

FileStorage class: the storage engine for all the objects of the base and subclasses


