def incoder(massage, number):
    incoded = ''
    for i in massage:
        incoded += chr(ord(i)+number)
    return incoded
def decoder(massage, number):
    decoded = ''
    for i in massage:
        decoded += chr(ord(i)-number)
    return decoded