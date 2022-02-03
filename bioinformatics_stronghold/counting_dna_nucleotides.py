path = "/Users/bengisu/Desktop/rosalind/bioinformatics_stronghold/"
f_input = open(path + 'input.txt', 'r')
seq = f_input.readline()
d = {}
for letter in seq:
	if letter in d:
		d[letter] += 1
	else:
		d[letter] = 1
print(d['A'], end = ' ')
print(d['C'], end = ' ')
print(d['G'], end = ' ')
print(d['T'], end = '')