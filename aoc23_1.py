def checkCalibration(string):
    oneFound = False
    twoFound = False
    for character in string:
        if oneFound:
            break
        else:
            if character.isdigit():
                calibrationOne = character
                oneFound = True
    for character in reversed(string):
        if twoFound:
            break
        else:
            if character.isdigit():
                calibrationTwo = character
                twoFound = True
    return calibrationOne + calibrationTwo

def replaceStringNumber(string):
    string = string.replace('one','o1e')
    string = string.replace('two','t2o')
    string = string.replace('three','t3e')
    string = string.replace('four','f4r')
    string = string.replace('five','f5e')
    string = string.replace('six','s6x')
    string = string.replace('seven','s7n')
    string = string.replace('eight','e8t')
    string = string.replace('nine','n9e')
    return string

file1 = open('C:\\Users\\poresky\\Downloads\\input_aoc_1_23.txt','r')
Lines = file1.readlines()
total = 0
for line in Lines:
    modifiedLine = replaceStringNumber(line)
    print(modifiedLine)
    total += float(checkCalibration(modifiedLine))
    print(total)
