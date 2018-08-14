import json
with open('config.json') as f:
    config = json.load(f)['pig-latin']
end_length = len(config['end'])

def encode(string):
    words = string.split(" ")
    for i in range(len(words)):
        words[i] = words[i][1:] + words[i][0] + config['end']
    return " ".join(words).lower()

def decode(string):
    words = string.split(" ")
    for i in range(len(words)):
        words[i] = words[i][-(end_length + 1)] + words[i][0:-(end_length + 1)]
    return " ".join(words).lower()
