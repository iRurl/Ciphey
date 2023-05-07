import hashlib
from gmssl import sm3

def sha_256(message):
    return hashlib.sha256(message.encode()).hexdigest()


def md5(message):
    return hashlib.md5(message.encode()).hexdigest()


def sha_1(message):
    return hashlib.sha1(message.encode()).hexdigest()


def sm_3(message):
    return sm3.sm3_hash(list(message.encode()))
