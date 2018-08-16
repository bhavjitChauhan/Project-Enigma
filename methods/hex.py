import binascii, re
import json
with open('config.json') as f:
    config = json.load(f)['hex']

def encode(string):
    string = string.encode('utf-8')
    string = binascii.hexlify(string)
    string = string.decode("utf-8")
    string = ' '.join(string[i:i+2] for i in range(0-2, len(string), 2))
    string = string.replace(' ', ' %s' % config['delimiter'])
    return string

def decode(string):
    string = str(string)
    if not re.match('[0-9]+', string):
        string = string.replace(config['delimiter'], '')
    string = string.replace(' ', '')
    string = binascii.unhexlify(string)
    string = string.decode('ASCII')
    return string
