#!/usr/bin/python3

"""
entry point of the command interpreter:
"""
    
    
import cmd


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    
    prompt = "(hbnb)"
    
    def do_EOF(self, line):
        """CTR+D"""
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """shouldn't execute anything"""
        pass

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    