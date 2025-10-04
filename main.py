import sys
import random

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "example.mb" #REPLACE with your own file

def readFile(path):
    with open(path, 'r') as f:
        return f.read()
    f.close()

def logFiles(data):
    with open("Log.txt", 'a') as f:
        f.write(data)
        f.close()

try:
    import config
    tapeLength = config.tapeLength
    logOutput = config.logOutput
    fileInput = config.fileInput

except FileNotFoundError:
        tapeLength = 1000
        logOutput = False
        fileInput = False
        

tape = []
pointers = []

for i in range(tapeLength):
    tape.append(0)


def main():
    if logOutput:
        logFiles("\n--BEGIN PROGRAM--\n")

    skip = False
    leftBrace = False

    numbers = ['0','1','2','3','4','5','6','7','8','9']

    idx = 0
    array = list(readFile(file))

    if fileInput:
        try:
            inputFile = list(readFile("Input.txt"))
        except FileNotFoundError:
            pass

    i=0
    ib = 0
    pb = 0
    luop = ''
    fileIdx = 0
    while i != len(array):
        if array[i] == '>' and skip == False:
            idx+=1
            luop = '>'
        if array[i] == '<' and skip == False:
            idx-=1
            luop = '<'
        if array[i] == '+' and skip == False:
            tape[idx] += 1
            luop = '+'
        if array[i] == '-' and skip == False:
            tape[idx] -= 1
            luop = '-'


        if array[i] == '.' and skip == False:
            print(chr(tape[idx]), end='')
            if logOutput:
                logFiles(chr(tape[idx]) + " / " + tape[idx] + "\n")

        if array[i] == ',' and skip == False:
            if fileInput:
                tape[idx] = ord(inputFile[fileIdx])
                fileIdx += 1
            else:
                temp = input('>')
                if temp == '':
                    tape[idx] = 0
                else:
                    tape[idx] = ord(temp)

        if array[i] == "\\" and skip == False:
            if fileInput:
                temp = inputFile[fileIdx:]
            else:
                temp = input(">>")
                temp = list(temp)
            ib=idx
            for j in temp:
                idx+=1
                tape[idx] = ord(j)
            idx = ib
            tape[idx] = len(temp)

        if array[i] == '#' and skip==False:
            pass
            luop = "#"

        if array[i] == '[' and skip == False:
            if tape[idx] != 0:
                skip = True
            else:
                skip = False
        if array[i] == ']':
            skip = False

        if array[i] == '{' and pointers[idx][1] == 'T' and leftBrace != True and skip == False:
            pb = idx
            idx = pointers[idx][0]
            leftBrace = True

        if array[i] == '}' and leftBrace == True and skip == False:
            leftBrace = False
            idx = pb

        if array[i] in numbers and skip == False:
            for j in range(int(array[i])):
                if luop == '>':
                    idx+=1
                if luop == '<':
                    idx-=1
                if luop == '+':
                    tape[idx] += 1
                if luop == '-':
                    tape[idx] -= 1
                if luop == '#':
                    pass

        if array[i] == '$' and skip == False:
            pointers.append([tape[idx], 'T'])
        if array[i] == '&':
            pointers.append([tape[idx], 'P'])

        if array[i] == '*' and skip == False:
            pointer = pointers[tape[idx]]
            if pointer[1] == 'T':
                idx = pointer[0]
            if pointer[1] == 'P':
                i = pointer[0]

        if array[i] == '^' and skip == False:
            idx = tape[idx]
        if array[i] == '@' and skip == False:
            pointer = pointers[tape[idx]]
            if pointer[1] == 'T':
                tape[idx] = tape[pointer[0]]
        if array[i] == '!' and skip == False:
            pointer = pointers[tape[idx]]
            if pointer[1] == 'P':
                array[pointer[0]] = chr(tape[idx])
        if array[i] == '%' and skip == False:
            limit = tape[idx]
            templ = []
            ib = idx
            for j in range(limit):
                idx+=1
                templ.append(chr(tape[idx]))
            templ.reverse()
            idx = ib
            for j in templ:
                array.insert(i+1, j)

        if array[i] == '?':
            tape[idx] = random.randint(0, tape[idx])

        if array[i] == ';':
            break


        i+=1

    if logOutput:
        logFiles("\n--END PROGRAM--\n")


if __name__ == "__main__":
    main()