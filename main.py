
def readFile(path):
    with open(path, 'r') as f:
        return f.read()
    f.close()

tape = []

for i in range(1000):
    tape.append(0)

def basics(op, idx):
        if op == '>':
            idx+=1
        if op == '<':
            idx-=1
        if op == '+':
            tape[idx] += 1
        if op == '-':
            tape[idx] -= 1

def main():
    skip = False

    numbers = ['0','1','2','3','4','5','6','7','8','9']

    idx = 0
    array = list(readFile("example.mb"))

    i=0
    ib = 0
    nu = ''
    while i != len(array):
        if array[i] == '>' and skip == False:
            idx+=1
        if array[i] == '<' and skip == False:
            idx-=1
        if array[i] == '+' and skip == False:
            tape[idx] += 1
        if array[i] == '-' and skip = False:
            tape[idx] -= 1
        if array[i] == "." and skip == False:
            print(chr(tape[idx]))
        if array[i] == ',' and skip == False:
            tape[idx] = int(input(">"))
        if array[i] == '[' and skip == False:
            if tape[idx] != 0:
                skip = True
            else:
                skip = False
        if array[i] == ']':
            skip = False
        if array[i] in numbers:
            op = array[i-1]
            for i in int(array[i]):
                basics(op, idx)


        i+=1


if __name__ == "__main__":
    main()