#!/usr/bin/python3

import json
import os

class FileStorage:

    __file_path = "file.json"
    __objects = {}
        
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
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                if os.path.getsize(FileStorage.__file_path) == 0:
                    pass
                else:
                    my_object = json.load(f)
                    for key, val in my_object.items():
                        FileStorage.__objects[key] = BaseModel(**val)
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
