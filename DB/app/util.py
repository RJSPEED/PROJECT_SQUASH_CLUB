import hashlib
import requests
import json

def hash_password(password):
    hasher = hashlib.sha512()
    hasher.update(password.encode())
    return hasher.hexdigest()
    

    