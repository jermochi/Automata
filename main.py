def isidentifier(token):
    if len(token) == 0:
        return False
    if token[0].isdigit():
        return False
    for ch in token:
        if not ch.isalnum() and ch != '_':
            return False
    return True

def isequalsign(token):
    if token != "=":
        return False
    return True

def isoperand(token):
    return token in ['+', '-', '*', '/']

def checkiflast(count, size):
    return count == size

def isfloat(token):
    if token.count('.') == 1:
        left, right = token.split('.')
        if left.isdigit() and right.isdigit() and left != '' and right != '':
            return True
    return False

def isint(token):
    return token.isdigit()

def ischar(token):
    return len(token) == 3 and token[0] == "'" and token[2] == "'"

def main():
    text = input("Enter assignment statement: ")
    tokens = text.split()
    state = 0
    count = 0
    for token in tokens:
        if state == 0:
            count += 1
            if not isidentifier(token):
                break
            state += 1
        elif state == 1:
            count += 1
            if not isequalsign(token):
                break
            state += 1
        elif state == 2:
            count += 1
            if checkiflast(count, len(tokens)):
                if not token[-1] == ";":
                    break
                newtoken = token[:-1]
                if isidentifier(newtoken) or isfloat(newtoken) or isint(newtoken) or ischar(newtoken):
                    state = 4
                    break
                else:
                    break
            if isoperand(token):
                break
            if isidentifier(token) or isfloat(token) or isint(token) or ischar(token):
                state += 1
            else:
                break
        elif state == 3:
            count += 1
            if isoperand(token):
                state = 2
                continue
            else:
                break
    if state == 4:
        print("Valid assignment statement")
    else:
        print("Invalid assignment statement")
    return

if __name__ == '__main__':
    main()