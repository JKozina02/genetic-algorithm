import Zad1 as Z
import matplotlib.pyplot as plt

items = Z.buildItems(8)
actualBackpackPopulation = Z.BuildBackbackPopulation(6, 8)

# Uruchomienie algorytmu genetycznego
def run_genetic_algorithm(penalty_func, items=items, population=actualBackpackPopulation):

    #definicja zmiennych
    best_in_population = [0, 0, 0, 0, 0]
    maxLoad = 25

    #generacja populacji
    actualBackpackPopulation = population
    best_in_population = Z.GetBestBackpack(actualBackpackPopulation, items, best_in_population, maxLoad)
    best_values_per_generation = []

    #iteracja po generacjach
    for i in range(100):
        nextPopulation = Z.GenerateNewPopulation(actualBackpackPopulation, items, maxLoad, penalty_func)
        repairedPopulation = Z.RepairBackpackRatio(nextPopulation, items, maxLoad)
        mutadedPopulation = Z.MutatePopulation(repairedPopulation)
        exchangedPopulation = Z.CrossPopulation(mutadedPopulation)
        actualBackpackPopulation = exchangedPopulation
        
        #znalezienie najlepszego plecaka
        best_in_population = Z.GetBestBackpack(actualBackpackPopulation, items, best_in_population, maxLoad)
        best_values_per_generation.append(Z.CalculateBackpackValue(best_in_population, items))
    return best_values_per_generation

# Uruchomienie algorytmu dla różnych funkcji kary
penalty_funcs = [Z.penalty_log, Z.penalty_linear, Z.penalty_squared]
penalty_names = ["Logarytmiczny", "Liniowy", "Kwadratowy"]

for i in range(len(penalty_funcs)):
    penalty_func = penalty_funcs[i]
    penalty_name = penalty_names[i]
    best_values = run_genetic_algorithm(penalty_func)
    plt.plot(best_values, label=penalty_name)

#   Rysowanie wykresu
plt.xlabel('Generacja')
plt.ylabel('Najlepsza wartość plecaka')
plt.legend()
plt.show()