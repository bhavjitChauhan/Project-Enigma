from methods import binary, pig_latin, hex

def encode(string, method):
    # if string[-1] == ' ':
    #     string = string[:-1]
    switch = {
        'Pig Latin': pig_latin.encode(string),
        'Binary': binary.encode(string),
        'Hex': hex.encode(string)
    }
    try:
        return switch.get(method)
    except:
        raise ValueError('Invalid encoding method')
