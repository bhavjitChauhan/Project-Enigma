from methods import binary, pig_latin

def encode(string, method):
    switch = {
        'Pig Latin': pig_latin.encode(string),
        'Binary': binary.encode(string)
    }
    try:
        return switch.get(method)
    except:
        raise ValueError('Invalid encoding method')