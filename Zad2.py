import random
import numpy as np

#returns random object [P, W]
def createRandomItem() -> list: 
    return([random.randint(1, 5), random.randint(1, 5)])

#returns list of objects
def buildItems(n:int) -> list: 
    elements = []
    for i in range(n):
        elements.append(createRandomItem())
    return elements

#returns 0 or 1
def RandomNum() -> int: 
    return int(np.random.choice([0,1]))

#returns random binary number with $length
def GetRandomBinary(length:int) -> list:  
    num = []
    for i in range(length):
        num.append(RandomNum())
    return num

#returns list of backbacks
def BuildBackbackPopulation(n:int, length:int) -> list: 
    population = []
    for i in range(n):
        population.append(GetRandomBinary(length))
    return population

#returns value of Backpack
def CalculateBackpackValue(backpack:list, items:list) -> int:
    sum = 0
    for i in range(len(backpack)):
        sum += backpack[i] * items[i][0]
    return sum

#returns weight of Backpack
def CalculateBackpackWeight(backpack:list, items:list) -> int:
    sum = 0
    for i in range(len(backpack)):
        sum += backpack[i] * items[i][1]
    return sum

#returns penalty of Backpack
def CalculateBackpackPenalty(backpack:list, items:list, maxLoad:int) -> int:
    weight = CalculateBackpackWeight(backpack, items)
    v = max([0, weight - maxLoad])

    p = []
    for i in range(len(backpack)):
        p.append(backpack[i] * (items[i][0] / items[i][1]))
    
    return max(p) * v

#returns list of adaptations from population
def MakeRouleteList(population:list, items:list, maxLoad:int) -> list:
    adaptations = []
    for i in population:
        score = CalculateBackpackValue(i, items) - CalculateBackpackPenalty(i, items, maxLoad)
        if score < 0:
            adaptations.append(0)
        else:
            adaptations.append(score)
    wholeAdaptation = sum(adaptations)
    for i in range(len(adaptations)):
        adaptations[i] = adaptations[i] / wholeAdaptation
    return adaptations

#returns random index from roulete
def GetRandomIndexFromRoulete(roulete: list) -> list:
    ranNum = np.random.rand()
    for i in range(len(roulete)):  
        ranNum -= roulete[i]
        if ranNum <= 0:
            return i

#returns new population
def GenerateNewPopulation(population:list) -> list:
    newPopulation = []
    roulete = MakeRouleteList(population)
    for i in range(len(population)):
        newPopulation.append(population[GetRandomIndexFromRoulete(roulete)])
    return newPopulation