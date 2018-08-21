import json

def encode(string):
    with open('config.json') as f:
        config = json.load(f)['pig-latin']
    end_length = len(config['end'])
    words = string.split(" ")
    for i in range(len(words)):
        words[i] = words[i][1:] + words[i][0] + config['end']
    if config['case'] == 'upper':
        words = ' '.join(words).upper()
    else:
        words = ' '.join(words).lower()
    return words

def decode(string):
    with open('config.json') as f:
        config = json.load(f)['pig-latin']
    end_length = len(config['end'])
    words = string.split(" ")
    for i in range(len(words)):
        words[i] = words[i][-(end_length + 1)] + words[i][0:-(end_length + 1)]
    if config['case'] == 'upper':
        words = ' '.join(words).upper()
    else:
        words = ' '.join(words).lower()
    return words
