def rabbits(month, baby):
	population = [1, 1]
	for i in range(2, month):
		n = population[i - 1] + (population[i - 2] * baby)
		population.append(n)
	return(population[month - 1])

print(rabbits(5, 3))
