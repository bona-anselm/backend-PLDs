#!/usr/bin/env python3
""" module """


def schools_by_topic(mongo_collection, topic):
    """ FUnction """
    sch = mongo_collection.find({"topics": topic})
    return list(sch)
