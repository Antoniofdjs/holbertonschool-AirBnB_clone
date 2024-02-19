#!/usr/bin/python3


"""Defines all common atributes/methods for other classes"""

import uuid
import datetime
class BaseModel:

    def __init__(self):
        id = uuid.uuid4()
        date = datetime.datetime.now()
        self.id = str(id)
        self.created_at = date.isoformat()
        self.updated_at = date.isoformat()


obj = BaseModel()
print(obj.id)
print(obj.created_at)
print(obj.updated_at)
 # TESTTINGGGG