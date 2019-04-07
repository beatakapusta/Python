import re, csv
def linijka(line):
	words = re.split('[\W\d]+', line)
	return [w.lower() for w in words if w]
 
text = open("wiki.txt", "r")
slownik = dict()

for line in text:
	words = linijka(line)
	for word in words:
		if word in slownik.keys():
			slownik[word] = slownik[word]+1
		else:
			 slownik[word] = 1

sortowanie = sorted(slownik.items(), key = lambda p:p[1], reverse = True)

index = 1
with open('kimchi.csv', 'w', newline='') as csvfile:
	w = csv.writer(csvfile)
	for x in sortowanie:
		w.writerow( [index] + list(x) )
		index = index +1

