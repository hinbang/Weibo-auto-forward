import sys
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62_decode(string, alphabet=ALPHABET):
        base = len(alphabet)
        strlen = len(string)
        num = 0
        idx = 0
        for char in string:
            power = (strlen - (idx + 1))
            num += alphabet.index(char) * (base ** power)
            idx += 1
        return num


if __name__ == '__main__':
    #HjodQzutN
    a = base62_decode('jodQ')
    print(a)