redMax = 12
greenMax = 13
blueMax = 14

def badGameCheck(game):
    badGame = False
    gameNumber = int(game.split(':')[0][5:])
    drawsOnly = game.split(':')[1:]
    drawsList = drawsOnly[0].split(';')
    balls = []
    for draw in drawsList:
        balls.append(draw.split(','))
    for draw in balls:
        for ball in draw:
            if 'green' in ball:
                greenCount = int([int(i) for i in ball.split() if i.isdigit()][0])
                if greenCount > greenMax:
                    badGame = True
                    break
            elif 'red' in ball:
                redCount = int([int(i) for i in ball.split() if i.isdigit()][0])
                if redCount > redMax:
                    badGame = True
                    break
            elif 'blue' in ball:
                blueCount = int([int(i) for i in ball.split() if i.isdigit()][0])
                if blueCount > blueMax:
                    badGame = True
                    break
            else:
                print('What kind of color is this?!')
    return gameNumber, badGame

def minCubePower(game):
    redMin = 0
    greenMin = 0
    blueMin = 0
    drawsOnly = game.split(':')[1:]
    drawsList = drawsOnly[0].split(';')
    balls = []
    for draw in drawsList:
        balls.append(draw.split(','))
    for draw in balls:
        for ball in draw:
            if 'green' in ball:
                greenCount = int([int(i) for i in ball.split() if i.isdigit()][0])
                if greenCount > greenMin:
                    greenMin = greenCount
            elif 'red' in ball:
                redCount = int([int(i) for i in ball.split() if i.isdigit()][0])
                if redCount > redMin:
                    redMin = redCount
            elif 'blue' in ball:
                blueCount = int([int(i) for i in ball.split() if i.isdigit()][0])
                if blueCount > blueMin:
                    blueMin = blueCount
    power = redMin * greenMin * blueMin
    return power, redMin, greenMin, blueMin

file = open('C:\\Users\\poresky\\Downloads\\input_aoc_2_23.txt','r')
Games = file.readlines()
total = 0
powerTotal = 0
gameList = []
for game in Games:
    result = badGameCheck(game)
    gameList.append(result)
    if False in result:
        print(result)
        total += result[0]
    powerResult = minCubePower(game)
    print(powerResult)
    powerTotal += powerResult[0]


