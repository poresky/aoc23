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
    string = string.replace('one','1')
    string = string.replace('two','2')
    string = string.replace('three','3')
    string = string.replace('four','4')
    string = string.replace('five','5')
    string = string.replace('six','6')
    string = string.replace('seven','7')
    string = string.replace('eight','8')
    string = string.replace('nine','9')
    return string

file1 = open('C:\\Users\\poresky\\Downloads\\input_aoc_1_23.txt','r')
Lines = file1.readlines()
total = 0
for line in Lines:
    modifiedLine = replaceStringNumber(line)
    print(modifiedLine)
    total += float(checkCalibration(modifiedLine))
    print(total)