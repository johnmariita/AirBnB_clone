#!/usr/bin/python3

import json
import os


class FileStorage:

    __file_path = "file.json"
    __objects = {}
    
    @classmethod
    def return_classes(cls):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        return {"BaseModel": BaseModel, "User": User, "Place": Place, \
                "State": State, "City": City, "Amenity": Amenity, \
                "Review": Review}
    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        objIdentity = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[objIdentity] = obj

    def save(self):
        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            obj_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                if os.path.getsize(FileStorage.__file_path) == 0:
                    pass
                else:
                    my_object = json.load(f)
                    for key, val in my_object.items():
                        class_name = key.split(".")[0]
                        FileStorage.__objects[key] = eval("FileStorage.return_classes()[class_name](**val)")
        else:
            pass
    def destroy(self, objId):
        del FileStorage.__objects[objId]
        self.save()

    @classmethod
    def get_obj(cls):
        return cls.__objects

    @classmethod
    def get_filepath(cls):
        return cls.__file_path
