def otx(strr):
    otxobiti = strr
    atobiti = 0
    for i, digit in enumerate(reversed(otxobiti)):
        atobiti += int(digit) * 4 ** i
    return atobiti
print(otx("12121212"))
