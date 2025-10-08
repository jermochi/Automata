
def isidentifier(token):
    for ch in token:
        if not ch.isalnum() and ch != '_':
            return False
    return True

def main():
    text = input("Enter assignment statement: ")
    tokens = text.split()
    state = 0

    for token in tokens:
        if state == 0:
            if not isidentifier(token):
                break
            state += 1
    if state == 1:
        print("Valid assignment operator")
    else:
        print("Invalid assignment operator")

if __name__ == '__main__':
    main()