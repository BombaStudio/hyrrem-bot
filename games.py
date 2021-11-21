import random

def mazeGame(x, y):
    mazes = [
        #wall
        "#",
        #water
        ".",
        #null
        " "
    ]
    map = {
        "type": [],
        "x": [],
        "y": []
    }
    for i in range(0,x):
        for j in range(0, y):
            pass

def randomMath(level):
    ops = [
        "+","-","*","/"
    ]
    islem = ""
    for i in range(0,level):
        islem += str(random.randint(1, int("1" + ("0" * level)))) + ops[random.randint(0, 3)]
    islem += str(random.randint(1, int("1" + ("0" * level))))
    #print(islem)
    return islem

#randomMath(3)