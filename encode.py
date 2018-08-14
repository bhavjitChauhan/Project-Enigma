import pig_latin
import binary

def encode(string, method):
    return {
        'Pig Latin': pig_latin.encode(string),
        'Binary': binary.encode(string)
    }.get(method, invalid_method())

def invalid_method():
    raise ValueError('Invalid encoding method')