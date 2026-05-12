#!/usr/bin/env python3
""" Find schools that include a given topic. """


def schools_by_topic(mongo_collection, topic):
    """Return all schools whose topics list contains the given topic string."""
    return list(mongo_collection.find({"topics": topic}))
