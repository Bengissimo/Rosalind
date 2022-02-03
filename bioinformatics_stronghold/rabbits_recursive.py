memo = {}
def rabbits(months, baby):
	args = (months, baby)
	if args in memo:
		return memo[args]
	if months == 1:
		result = 1
	elif months == 2:
		result = 1
	elif (months > 2 and months <= 40 and baby <= 5):
		result = (rabbits(months - 2, baby) * baby) + rabbits(months - 1, baby)
	else:
		return (-1)
	memo[args] = result
	return result

print(rabbits(33, 2))