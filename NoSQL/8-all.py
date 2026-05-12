#!/usr/bin/env python3
""" List all documents in a MongoDB collection. """


def list_all(mongo_collection):
    """Return every document in the collection, or [] if there are none."""
    return list(mongo_collection.find())
