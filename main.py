import fitness as f
import generate as g
import selection
import breed
import mutate
from mypass import mypassword
password=mypassword

N=1000

#First population:
population=g.generateFirstPopulation(20,password)
#print(population)

for i in range(1,N):

	population_perf=selection.computePerfPopulation(population,password)
	#print(population_perf)

	next_gen=selection.selectFromPopulation(population_perf,10,10)
	#print(next_gen)

	#Next generation breeding:
	breeded_gen=breed.createChildren(next_gen,5)

	#Mutation of breeded generation:
	mutated_gen=mutate.mutatePopulation(breeded_gen,5)

	population=mutated_gen

mutated_gen_perf=selection.computePerfPopulation(population,password)
final_population=dict(mutated_gen_perf)

for k,v in final_population.items():
	print(k,"  ",v)