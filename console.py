#!/usr/bin/python3

"""
entry point of the command interpreter:
"""
    
    
import cmd
import ast
from models.base_model import BaseModel
from models import storage
from datetime import datetime


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
                class_inst.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            
    def do_show(self, line):
        """Prints the string representation 
        of an instance based on the class name and id"""
        if line:
            line_args = line.split()
            if line_args[0] in self.class_names:
                try:
                    if line_args[1]:
                        k = line_args[0] + "." + line_args[1]
                        if k in storage.all().keys():
                            print(storage.all()[k])
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                except IndexError:
                    print ("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line:
            line_args = line.split()
            if line_args[0] in self.class_names:
                try:
                    if line_args[1]:
                        k = line_args[0] + "." + line_args[1]
                        if k in storage.all().keys():
                            del storage.all()[k]
                            storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                except IndexError:
                    print ("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            
    def do_all(self, line):
        """Prints all string representation of 
        all instances based or not on the class name."""
        all_list = []
        if line:
            if line in self.class_names:
                for k, val in storage.all().items():
                    if line in k:
                        all_list.append(str(val))
                print(all_list)
            else:
                print ("** class doesn't exist **")
        else:
            for val in storage.all().values():
                all_list.append(str(val))
            print(all_list)
            
    def do_update(self, line):
        """Updates an instance based on the class name 
        and id by adding or updating attribute"""
        if line:
            line_args = line.split()
            if line_args[0] in self.class_names:
                try:
                    if line_args[1]:
                        name = line_args[0] + "." + line_args[1]
                        for k, v in storage.all().items():
                            if name == k:
                                try:
                                    if line_args[2]:
                                        try:
                                            if line_args[3]:
                                                val = ast.literal_eval(line_args[3])
                                                setattr(storage.all()[name], line_args[2], val)
                                                setattr(storage.all()[name], 'updated_at', datetime.now())
                                                storage.save()
                                        except ImportError:
                                            print("** value missing **")          
                                except IndexError:
                                    print("** attribute name missing **")
                except IndexError:
                    print ("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        
            

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    