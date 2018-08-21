import re
import json

def encode(string):
    with open('config.json') as f:
        config = json.load(f)['binary']
    string = str(string)
    string = ' '.join(format(ord(i), 'b') for i in string)
    string.replace('100000', '00100000')
    if config['1'] != '1' or config['0'] != '0':
        string = string.replace('1', '%temp%').replace('0', config['0']).replace('%temp%', config['1'])
    return string

def decode(string):
    with open('config.json') as f:
        config = json.load(f)['binary']
    string = str(string)
    if string[-1] != ' ':
        string += ' '
    if not re.match('[0-1]+', string):
        string = string.replace(config['1'], '1')
        string = string.replace(config['0'], '0')        
    return ''.join(chr(int(string[i * 8:i * 8 + 8], 2)) for i in range(len(string) // 8))
