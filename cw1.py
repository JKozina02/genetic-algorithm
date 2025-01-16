import numpy as np

#returns decimal value of binary number
def BinaryCalc(binaryList: list) -> int:
    sum = 0
    binaryList.reverse()
    for i in range(len(binaryList)):
        sum += binaryList[i] * 2 ** i
    return sum

def BinaryInRange(binaryList: list, a: int, b: int) -> float:
    return a + (BinaryCalc(binaryList) / (2 ** len(binaryList) - 1)) * (b - a)

#returns 0 or 1
def RandomNum() -> int: 
    return int(np.random.choice([0,1]))

#returns random binary number with $length
def GetRandomBinary(length:int) -> list:  
    num = []
    for i in range(length):
        num.append(RandomNum())
    return num

#returns value of function
def calcY(x) -> float: 
    return (np.sin(x) + np.sin((10/3) * x))

#zad5 returns list containing population
def GetNewPopulation(chromosom:int, length:int) -> list: 
    population = []
    for i in range(chromosom):
        population.append(GetRandomBinary(length))
    return population

#zad6 returns list of adaptations of population
def GetAdaptationOfPopulation(population:list, a:int = 0, b:int = 10) -> list: 
    adaptations = []
    for i in population:
        adaptations.append(BinaryInRange(i, a, b))
    return adaptations

#Roulete
def MakeRouleteList(adaptations:list) -> list:
    wholeAdaptation = sum(adaptations)
    for i in range(len(adaptations)):
        adaptations[i] = adaptations[i] / wholeAdaptation
    return adaptations

def GetRandomIndexFromRoulete(roulete: list) -> list:
    ranNum = np.random.rand()
    for i in range(len(roulete)):  
        ranNum -= roulete[i]
        if ranNum <= 0:
            return i
            
#zad7
def ProcessNewPopulation(population:list) -> list:
    newPopulation = []
    adaptations = GetAdaptationOfPopulation(population)
    roulete = MakeRouleteList(adaptations)
    for i in range(len(population)):
        newPopulation.append(population[GetRandomIndexFromRoulete(roulete)])
    return newPopulation
    
#zad8
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

#zad9
#losowa mutacja
def MutateGene(number: int, propability: float = 0.01) -> int:
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

# Funkcja obliczająca najlepsze rozwiązanie
def GetBestSolution(population: list, a: int = 0, b: int = 10) -> float:
    adaptations = GetAdaptationOfPopulation(population, a, b)
    best_index = np.argmin([calcY(adaptation) for adaptation in adaptations])
    return adaptations[best_index]

