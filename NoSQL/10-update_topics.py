#!/usr/bin/env python3
""" Update topics for school documents by name. """


def update_topics(mongo_collection, name, topics):
    """Set topics to the given list for every document with this school name."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
