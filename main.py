
def readFile(path):
    with open(path, 'r') as f:
        return f.read()
    f.close()

tape = []

for i in range(1000):
    tape.append(0)

def main():
    skip = False


    idx = 0
    array = list(readFile("example.mb"))
    for i in array:
        if i == '>' and skip == False:
            idx+=1
        if i == '<' and skip == False:
            idx-=1
        if i == '+' and skip == False:
            tape[idx] += 1
        if i == "." and skip == False:
            print(chr(tape[idx]))
        if i == ',' and skip == False:
            tape[idx] = int(input(">"))
        if i == '[' and skip == False:
            if tape[idx] != 0:
                skip = True
            else:
                skip = False
        if i == ']':
            skip = False


if __name__ == "__main__":
    main()