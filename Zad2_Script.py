import Zad2 as Z


items = Z.buildItems(5)
maxLoad = 10

print("Items: ", items)

actualBackpackPopulation = Z.BuildBackbackPopulation(5, 5)
print("Population: ", actualBackpackPopulation)

weights = []
values = []
penalties = []

for i in actualBackpackPopulation:
    weights.append(Z.CalculateBackpackWeight(i, items))
    values.append(Z.CalculateBackpackValue(i, items))
    penalties.append(Z.CalculateBackpackPenalty(i, items, maxLoad))

roulete = Z.MakeRouleteList(actualBackpackPopulation, items, maxLoad)
print("Roulete: ", roulete)

rouleteIndex = Z.GetRandomIndexFromRoulete(roulete)
print("Random index from roulete: ", rouleteIndex)