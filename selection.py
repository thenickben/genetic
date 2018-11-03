import operator
import random
import fitness as f

def computePerfPopulation(population, password):
	populationPerf = {}
	for individual in population:
		populationPerf[individual] = f.fitness(password, individual)
	return sorted(populationPerf.items(), key = operator.itemgetter(1), reverse=True)

def selectFromPopulation(populationSorted, best_sample, lucky_few):
	nextGeneration = []
	for i in range(best_sample):
		nextGeneration.append(populationSorted[i][0])
	for i in range(lucky_few):
		nextGeneration.append(random.choice(populationSorted)[0])
	random.shuffle(nextGeneration)
	return nextGeneration