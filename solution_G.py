vaults = int(input("Enter a number of vaults: "))
input_money = input("Enter an amount of money: ")

money = [int(x) for x in input_money.split(',')]
copied = money.copy()


def find_max_in_adjacent(adjacent):
	first = max(adjacent)
	adjacent[adjacent.index(first)] = 0
	second = max(adjacent)
	adjacent = money.copy()
	return first + second


n_chunks = len([money[x:x+5] for x in range(0, vaults, 5)]) 
koef = 5 - vaults % 5
if koef == 5: koef = 0

results = []

for i in range(5):
	chunks = [money[i:][x:x+5] for x in range(0, len(money[i:]), 5)]

	if len(chunks[-1]) < 5 and i > 0:
		chunks[-1] = chunks[-1] + money[:5-len(chunks[-1])-koef]

	if len(chunks) < n_chunks:
		chunks += money[:5-koef]

	result = 0
	for j in chunks:
		result += find_max_in_adjacent(j)

	results.append(result)

print (max(results))