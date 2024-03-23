#!/usr/bin/python3

import cmd
import sys
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    prompt = ("(hbnb) ")

    def precmd(self, line):
        """Precmd method that modifies the input
        """
        reg1 = r"(\w+)\.(\w+)\(\)"
        reg2 = r"(\w+)\.(\w+)\(\"([a-zA-Z0-9-]+)\"\)"
        reg3 = r"(\w+)\.(\w+)\((\"[a-zA-Z0-9-]+\"),\s?(\"\w+\"),\s?(\"\w+\")\)"
        reg4 = r"(\w+)\.(\w+)\((\"[a-zA-Z0-9-]+\"),\s?(\{.+\})"
        matched1 = re.match(reg1, line)
        matched2 = re.match(reg2, line)
        matched3 = re.match(reg3, line)
        matched4 = re.match(reg4, line)

        if matched1:
            class_name = matched1.group(1)
            method = matched1.group(2)
            return f"{method} {class_name}"
        elif matched2:
            class_name = matched2.group(1)
            method = matched2.group(2)
            class_id = matched2.group(3)
            return f"{method} {class_name} {class_id}"
        elif matched3:
            class_name = matched3.group(1)
            method = matched3.group(2)
            class_id = matched3.group(3).strip('"')
            attr_name = matched3.group(4).strip('"')
            attr_val = matched3.group(5)
            return f"{method} {class_name} {class_id} {attr_name} {attr_val}"
        elif matched4:
            class_name = matched4.group(1)
            method = matched4.group(2)
            class_id = matched4.group(3).strip('"')
            my_dict = eval(matched4.group(4))
            for key, val in my_dict.items():
                self.do_update(f'{class_name} {class_id} {key} {val}')
            return "nothing"

        else:
            return line

    def do_nothing(self, line):
        """Method called after updating a class
        """
        return ""

    def do_count(self, line):
        """Method that counts the instances of a class
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            count = 0
            if args[0] not in list(FileStorage.return_classes().keys()):
                print("** class doesn't exist **")
            else:
                for key, obj in FileStorage.get_obj().items():
                    if key.split(".")[0] == args[0]:
                        count += 1
                print(count)

    def do_quit(self, line):
        """Quit command to exit the program
        """
        exit()

    def do_EOF(self, line):
        """End of File signal that exits the program
        """
        exit()

    def do_create(self, line):
        """Method that creates a new instance of a class
        """
        if not line:
            print("** class name missing **")
        elif line.split()[0] not in FileStorage.return_classes().keys():
            print("** class doesn't exist **")
        else:
            line = line.split()[0]
            new = eval("FileStorage.return_classes()[line]()")
            new.save()
            print(new.id)

    def do_show(self, line):
        """Method that displays an instance
        """
        if not line:
            print("** class name missing **")

        else:
            # Handle class missing
            args = line.split()
            if args[0] not in [obj.split(".")[0]
                               for obj in FileStorage.get_obj().keys()]:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")

                else:
                    # Handle id missing
                    if args[1] not in [obj.split(".")[1]
                                       for obj in
                                       FileStorage.get_obj().keys()]:
                        print("** no instance found **")
                    else:
                        classId = ".".join(args[:2])
                        print(FileStorage.get_obj()[classId])

    def do_destroy(self, line):
        """Method that deletes an instance
        """
        if not line:
            print("** class name missing **")

        else:
            # Handle class missing
            args = line.split()
            if args[0] not in [obj.split(".")[0]
                               for obj in FileStorage.get_obj().keys()]:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")

                else:
                    # Handle id missing
                    if args[1] not in [obj.split(".")[1]
                                       for obj in
                                       FileStorage.get_obj().keys()]:
                        print("** no instance found **")

                    else:
                        # Handle id missing
                        classId = ".".join(args[:2])
                        storage.destroy(classId)

    def do_all(self, line):
        """Method that displays all instances of a class
        """
        objects = FileStorage.get_obj()
        my_list = []
        class_found = False
        if not line:
            class_found = True
            for key, val in objects.items():
                my_list.append(str(val))

        else:
            # Handle class missing
            args = line.split()
            if args[0] not in [obj.split(".")[0]
                               for obj in FileStorage.get_obj().keys()]:
                print("** class doesn't exist **")

            else:
                class_found = True
                for key, val in objects.items():
                    if key.split(".")[0] == args[0]:
                        my_list.append(str(val))
        if class_found:
            print(my_list)

    def do_update(self, line):
        """Method that updates an instance
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) == 1:
                if args[0] not in [obj.split(".")[0]
                                   for obj in
                                   FileStorage.get_obj().keys()]:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")

            elif len(args) == 2:
                if args[0] not in [obj.split(".")[0]
                                   for obj in
                                   FileStorage.get_obj().keys()]:
                    print("** class doesn't exist **")
                elif args[1] not in [obj.split(".")[1]
                                     for obj in FileStorage.get_obj().keys()]:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            elif len(args) == 3:
                if args[0] not in [obj.split(".")[0]
                                   for obj in FileStorage.get_obj().keys()]:
                    print("** class doesn't exist **")
                elif args[1] not in [obj.split(".")[1]
                                     for obj in FileStorage.get_obj().keys()]:
                    print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                if args[0] not in [obj.split(".")[0]
                                   for obj in FileStorage.get_obj().keys()]:
                    print("** class doesn't exist **")
                elif args[1] not in [obj.split(".")[1]
                                     for obj in FileStorage.get_obj().keys()]:
                    print("** no instance found **")
                else:
                    attr_name = args[2]
                    try:
                        val = int(args[3].strip('"'))
                    except ValueError:
                        try:
                            val = float(args[3].strip('"'))
                        except ValueError:
                            val = args[3].strip('"')

                    classId = ".".join(args[:2])
                    objects = FileStorage.get_obj()
                    for key, obj in objects.items():
                        if key == classId:
                            setattr(obj, attr_name, val)
                            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
