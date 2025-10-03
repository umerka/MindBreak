
def readFile(path):
    with open(path, 'r') as f:
        return f.read()
    f.close()

tape = []

for i in range(1000):
    tape.append(0)


def main():
    skip = False

    numbers = ['0','1','2','3','4','5','6','7','8','9']

    idx = 0
    array = list(readFile("example.mb"))

    i=0
    ib = 0
    luop = ''
    while i != len(array):
        if array[i] == '>' and skip == False:
            idx+=1
            luop = '>'
        if array[i] == '<' and skip == False:
            idx-=1
            luop = '>'
        if array[i] == '+' and skip == False:
            tape[idx] += 1
            luop = '+'
        if array[i] == '-' and skip == False:
            tape[idx] -= 1
            luop = '-'
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
            for j in range(int(array[i])):
                if luop == '>':
                    idx+=1
                if luop == '<':
                    idx-=1
                if luop == '+':
                    tape[idx] += 1
                if luop == '-':
                    tape[idx] -= 1
        i+=1


if __name__ == "__main__":
    main()