#!/usr/bin/env python3
""" Module Comment """


def list_all(mongo_collection):
    """ function comment """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
