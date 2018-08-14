def encode(string):
    words = string.split(" ")
    for i in range(len(words)):
        words[i] = words[i][1:] + words[i][0] + "a"
    return " ".join(words).lower()

def decode(string):
    words = string.split(" ")
    for i in range(len(words)):
        words[i] = words[i][-2] + words[i][0:-2]
    return " ".join(words).lower()