import random
import numpy as np

#returns random object [P, W]
def createRandomItem() -> list: 
    return([random.randint(1, 8), random.randint(1, 8)])

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
def CalculateBackpackPenalty(backpack:list, items:list, maxLoad:int, penalty_func) -> int:
    weight = CalculateBackpackWeight(backpack, items)
    v = max([0, weight - maxLoad])
    return penalty_func(v)

def penalty_log(v):
    return np.log2(1 + v)

def penalty_linear(v):
    return v

def penalty_squared(v):
    return v ** 2

#returns list of adaptations from population
def MakeRouleteList(population:list, items:list, maxLoad:int, penalty_func) -> list:
    adaptations = []
    for i in population:
        score = CalculateBackpackValue(i, items) - CalculateBackpackPenalty(i, items, maxLoad, penalty_func)
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
def GenerateNewPopulation(population:list, items:list, maxLoad:int, penalty_func) -> list:
    newPopulation = []
    roulete = MakeRouleteList(population, items, maxLoad, penalty_func)
    for i in range(len(population)):
        newPopulation.append(population[GetRandomIndexFromRoulete(roulete)])
    return newPopulation

#mutate population
def MutateGene(number: int, propability: float = 0.05) -> int:
    random = np.random.rand()
    if random <= propability:
        return 1-number
    else:
        return number

def MutateChromosome(chromosome: list) -> list:
    mutatedChromosome = []
    for i in chromosome:
        mutatedChromosome.append(MutateGene(i))
    return mutatedChromosome

def MutatePopulation(population: list) -> list:
    mutatedPopulation = []
    for i in population:
        mutatedPopulation.append(MutateChromosome(i))
    return mutatedPopulation

#Wymiana genów dla 2 chromosomów
def Exchange(first: list, second: list):
    pointOfCut = round(len(first)/2)
    newFirst = second[:pointOfCut] + first[pointOfCut:]
    newSecond = first[:pointOfCut] + second[pointOfCut:]
    return [newFirst, newSecond]

#Wymienia geny dla chromosomów całej tablicy
def CrossPopulation(population: list, propability: float = 1) -> list:
    if len(population) % 2 != 0:
        print("ERROR population is not even")
        return None
    index = 0
    crossedPopulation = []
    while index < len(population):
        first = population[index]
        second = population[index+1]
        #print("first", first, "second",second)
        random = np.random.rand()
        if random <= propability:
            #print('succes', Exchange(first, second))
            crossedPopulation += (Exchange(first, second))
        else:
            #print("fail", [first, second])
            crossedPopulation.extend([first, second])
        index += 2
    return crossedPopulation

# Funkcja obliczająca plecak o największej wartości
def GetBestBackpack(population: list, items: list, current_best: list, maxLoad: int) -> list:
    best_value = CalculateBackpackValue(current_best, items)
    best_backpack = current_best
    for backpack in population:
        if CalculateBackpackWeight(backpack, items) <= maxLoad:
            value = CalculateBackpackValue(backpack, items)
            if value > best_value:
                best_value = value
                best_backpack = backpack
    return best_backpack
