maior = 1
numSeqMaior = 0
n = 1
while (n < 1000000):
	val = n
	numseq = 1
	while (val > 1):
		if (val % 2 == 0):
			val = val / 2
		else:
			val = 3 * val + 1
		numseq = numseq + 1

	if (numseq > numSeqMaior):
		maior = n
		numSeqMaior = numseq

	n = n+1

print maior
print numSeqMaior 
