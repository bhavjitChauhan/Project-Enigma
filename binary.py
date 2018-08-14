def encode(string):
    string = str(string)
    string = ' '.join(format(ord(i), 'b') for i in string)
    string.replace('100000', '00100000')
    return string

def decode(string):
    string = str(string)
    return ''.join(chr(int(string[i * 8:i * 8 + 8], 2)) for i in range(len(string) // 8))
