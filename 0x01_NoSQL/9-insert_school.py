#!/usr/bin/env python3
""" Module """

def insert_school(mongo_collection, **kwargs):
    """ Function """
    inserted_doc = mongo_collection.insert_one(kwargs)
    return inserted_doc.inserted_id
