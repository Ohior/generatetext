import os
from uuid import uuid1


def generateUuidName():
    # Generate a UUID based on the host ID and current time
    uid = uuid1()
    uid_string = str(uid)
    return uid_string.split("-")[0]


def createDirectory() -> str:
    directory = os.path.join(os.getcwd(), "raw", generateUuidName())
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
