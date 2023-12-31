from rotator import Rotator

def printNumbers(inputList):
    numItems = len(inputList)

    toPrint = "["
    for i in range(numItems - 1):
        toPrint += str(inputList[i]) + ", "
    toPrint += str(inputList[numItems - 1]) + "]"
    print(toPrint)

def run():
    numRotations = 1
    print("Num rotations: " + str(numRotations) + "\n")

    numbers = [1, 2, 3, 4, 5, 6]

    rotator = Rotator()
    
    print("Before:")
    printNumbers(numbers)
    print("")

    rotator.rotateRepeat(numbers, numRotations)
    
    print("After:")
    printNumbers(numbers)
    print("")

run()