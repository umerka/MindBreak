
def readFile(path):
    with open(path, 'r') as f:
        return f.read()
    f.close()

tape = []

for i in range(1000):
    tape.append(0)

def main():
    idx = 0
    array = list(readFile("example.mb"))
    for i in array:
        if i == '>':
            idx+=1
        if i == '<':
            idx-=1
        if i == '+':
            tape[idx] += 1
        if i == ".":
            print(tape[idx])
        if i == ',':
            tape[idx] = int(input(">"))

if __name__ == "__main__":
    main()