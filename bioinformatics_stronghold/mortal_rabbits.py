def mortal_rabbits(month, lifespan):
	population= [1, 1]
	for i in range(2, month):
		if i < lifespan:
			n = population[i - 1] + population[i - 2]
		elif i == lifespan:
			n = population[i - 1] + population[i - 2] - 1
		else:
			n = population[i - 1] + population[i - 2] - population[i - lifespan - 1]
		population.append(n)
	return population[month - 1]

print(mortal_rabbits(88, 18))