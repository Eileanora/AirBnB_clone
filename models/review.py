#!/usr/bin/python3
'''Module representing the review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Class representing the review'''
    place_id = ""
    user_id = ""
    text = ""
