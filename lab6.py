def main():
    x = 2


def decode(pswd):
    output = ''
    for i in range(len(pswd)):
        num = int(pswd[i]) - 3
        output += str(num) if num >= 0 else str(10 + num)
    return output
