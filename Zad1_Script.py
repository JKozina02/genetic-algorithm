import Zad1 as S
import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 100
chromosome_length = 8
population_size = 6

# Generate initial population
population = S.GetNewPopulation(population_size, chromosome_length)
actualPopulation = population
global_best = S.GetBestSolution(actualPopulation)

# Evolve the population
for i in range(n):
    nextPopulation = S.ProcessNewPopulation(actualPopulation)
    crossedPopulation = S.CrossPopulation(nextPopulation)
    mutatedPopulation = S.MutatePopulation(crossedPopulation)
    actualPopulation = mutatedPopulation

    best_in_population = S.GetBestSolution(actualPopulation)
    
    if S.calcY(best_in_population) < S.calcY(global_best):
        global_best = best_in_population

best_y = S.calcY(global_best)

x = np.linspace(0, 10, 100)
y = np.sin(x) + np.sin((10 / 3) * x)

plt.plot(x, y, label="Function y = sin(x) + sin(10/3 * x)", color='blue')
plt.scatter(global_best, best_y, color='red', label=f"Best solution: x={global_best:.2f}, y={best_y:.2f}")
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print("Final population:", actualPopulation)