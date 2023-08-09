#!/usr/bin/python3

"""
entry point of the command interpreter:
"""
       
import cmd
import ast
import re
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    
    prompt = "(hbnb)"
    class_names = ["BaseModel", "User", "State", "Review", "Place", "City", "Amenity"]

    
    def do_EOF(self, line):
        """CTR+D"""
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """shouldn't execute anything"""
        pass

    def do_count(self, line):
        '''count number of instances of a class'''
        count = 0
        if line in self.class_names:
            for key in storage.all().keys():
                if line in key:
                    count += 1
        print(count)

    def do_create(self, line):
        """Creates a new instance"""
        if line is None or line == "":
            print("** class name missing **")
        elif line not in self.class_names:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            print(new_instance.id)
            new_instance.save()



    def do_show(self, line):
        """Prints the string representation 
of an instance based on the class name and id"""

        if line is None or line == "": # if line is empty
            print("** class name missing **")
        else:
            line_args = line.split()
            if line_args[0] not in self.class_names:
                print("** class doesn't exist **")
            elif len(line_args) < 2:
                print("** instance id missing **")
            else:
                key = line_args[0] + "." + line_args[1].replace('"', '')
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])




    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line is None or line == "":
            print("** class name missing **")
        
        else:
            line_args = line.split()
            if line_args[0] not in self.class_names:
                print("** class doesn't exist **")
            elif len(line_args) < 2:
                print("** instance id missing **")
            else:
                key = line_args[0] + "." + line_args[1].replace('"', '')
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()


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
        if line is None or line == "":
            print("** class name missing **")
        else:
            line_args = line.split()
            if line_args[0] not in self.class_names:
                print("** class doesn't exist **")
            elif len(line_args) < 2:
                print("** instance id missing **")
            elif len(line_args) < 3:
                print("** attribute name missing **")
            elif len(line_args) < 4:
                print("** value missing **")
            else:
                key = line_args[0] + "." + line_args[1].replace('"', '')
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    val = ast.literal_eval(line_args[3])
                    setattr(storage.all()[key], line_args[2], val)
                    setattr(storage.all()[key], 'updated_at', datetime.now())
                    storage.save()
                    
    def parse(self, line):
        """parsing line to <method_name> <class_name>"""
        arg_list = []
        match = re.match(r'^(\w+)\.(\w+)\((.*?)\)?$', line)
        if match:
            class_name = match.group(1)
            method_name = match.group(2)
            arg_list.append(method_name)
            arg_list.append(class_name)
            try:
                arguments = match.group(3)
                if arguments != '':
                     arg_list.append(arguments)
            except IndexError:
                pass
            return arg_list
            #print(class_name)
            #print(method_name)
        
            
    def default(self, line):
        """dealing with unkown command"""
        arg_list = self.parse(line)
        if arg_list: 
            try:
                method_name = "do_" + arg_list[0]
                method = getattr(self, method_name)
                if len(arg_list) == 2:
                    method(arg_list[1])
                elif len(arg_list) == 3:
                    if "," in arg_list[2]:
                        arg = arg_list[1] + " " + arg_list[2].replace(',', '')
                    else:
                        arg = arg_list[1] + " " + arg_list[2]
                    method(arg)
            except SyntaxError:
                print(f"*** Unknown syntax: {line}")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
