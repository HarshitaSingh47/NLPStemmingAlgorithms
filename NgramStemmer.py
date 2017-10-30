import nltk
from nltk.corpus import brown
import numpy as np

stem_word = 'feels'
thresh = 0
brown_words = brown.words()

def get_frequency(word):
	i = 0
	for w in brown_words:
		if word in w:
			i += 1
	return i

#Initialization
freq = np.zeros(len(stem_word) - 3)

for i in range(0, len(freq)):
	freq[i] = get_frequency(stem_word[:i+4])

print 'Frequency of internal n-grams', freq

lmds = np.zeros(len(freq))
lmds[0] = float('inf')
psi = 4

i = 1
while True:
	if i == len(freq):
		break
	delta = lmds[i] - lmds[i-1]
	if delta > 0:
		break
	lmds[i] = np.absolute(freq[i] - freq[i-1])
	if lmds[i] > thresh:
		if freq[i] > freq[i-1]:
			psi = i + 4
		else:
			psi = i + 3
	else:
		psi = i + 4
	i += 1

if psi == len(stem_word):
	if psi - 3 > 3:
		psi -= 3

print 'Original word :', stem_word
print 'Stem word :', stem_word[:psi]