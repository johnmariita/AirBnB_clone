#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = ("(hbnb) ")
    def do_quit(self, line):
        """Quit command to exit the program
        """
        exit()

    def do_EOF(self, line):
        """End of File signal that exits the program
        """
        exit()

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line not in FileStorage.return_classes().keys():
            print("** class doesn't exist **")
        else:
            line = line.split()[0]
            new = eval("FileStorage.return_classes()[line]()")
            new.save()
            print(new.id)

    def do_show(self, line):
        if not line:
            print("** class name missing **")

        else:
            # Handle class missing
            args = line.split()
            if args[0] not in [obj.split(".")[0] for obj in FileStorage.get_obj().keys()]:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")

                else:
                    # Handle id missing
                    if args[1] not in [obj.split(".")[1] for obj in FileStorage.get_obj().keys()]:
                        print("** no instance found **")
                    else:
                        classId = ".".join(args)
                        print(FileStorage.get_obj()[classId])

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")

        else:
            # Handle class missing
            args = line.split()
            if args[0] not in [obj.split(".")[0] for obj in FileStorage.get_obj().keys()]:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")

                else:
                    # Handle id missing
                    if args[1] not in [obj.split(".")[1] for obj in FileStorage.get_obj().keys()]:
                        print("** no instance found **")

                    else:
                        # Handle id missing
                        classId = ".".join(args)
                        storage.destroy(classId)
                
    def do_all(self, line):
        objects = FileStorage.get_obj()
        my_list = []
        if not line:
            for key, val in objects.items():
                my_list.append(str(val))

        else:
            # Handle class missing
            args = line.split()
            if args[0] not in [obj.split(".")[0] for obj in FileStorage.get_obj().keys()]:
                print("** class doesn't exist **")

            else:
                for key, val in objects.items():
                    if key.split(".")[0] == args[0]:
                        my_list.append(str(val))
        print(my_list)

    def do_update(self, line):
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) == 1:
                if args[0] not in [obj.split(".")[0] for obj in FileStorage.get_obj().keys()]:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")

            elif len(args) == 2:
                if args[0] not in [obj.split(".")[0] for obj in FileStorage.get_obj().keys()]:
                    print("** class doesn't exist **")
                elif args[1] not in [obj.split(".")[1] for obj in FileStorage.get_obj().keys()]:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            elif len(args) == 3:
                if args[0] not in [obj.split(".")[0] for obj in FileStorage.get_obj().keys()]:
                    print("** class doesn't exist **")
                elif args[1] not in [obj.split(".")[1] for obj in FileStorage.get_obj().keys()]:
                    print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                if args[0] not in [obj.split(".")[0] for obj in FileStorage.get_obj().keys()]:
                    print("** class doesn't exist **")
                elif args[1] not in [obj.split(".")[1] for obj in FileStorage.get_obj().keys()]:
                    print("** no instance found **")
                else:
                    attr_name = args[2]
                    try:
                        val = float(args[3].strip('"'))
                    except ValueError:
                        try:
                            val = int(args[3].strip('"'))
                        except ValueError:
                            val = args[3].strip('"')

                    classId = ".".join(args[:2])
                    objects = FileStorage.get_obj()
                    for key, obj in objects.items():
                        if key == classId:
                            setattr(obj, attr_name, val)
                    storage.save()


               
if __name__ == "__main__":
    HBNBCommand().cmdloop()
