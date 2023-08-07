#!/usr/bin/python3

"""
entry point of the command interpreter:
"""
    
    
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    
    prompt = "(hbnb)"
    class_names = ["BaseModel"]
    
    def do_EOF(self, line):
        """CTR+D"""
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """shouldn't execute anything"""
        pass
    
    def do_create(self, line):
        """Creates a new instance"""
        if line:
            if line in self.class_names:
                class_inst = eval(line)()
                print(class_inst.id)
                #save
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        if line:
            line_args = line.split()
            if line_args[0] in self.class_names:
                try:
                    if line_args[1]:
                        #do smething
                        pass
                except IndexError:
                    print ("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    