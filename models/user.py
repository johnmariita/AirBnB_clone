#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """Definition of the user class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
