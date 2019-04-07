import re

def linijka(line):
	line=line.replace('-', '')
	#print(line)
	#re.sub('[0-9]{2-5}-[0-9]{2-5}-[0-9]{2-5}', '[0-9]', line)
	line=re.sub(r'(\d)\s+(\d)', r'\1\2', line)
	words = re.split('[\W]+', line)
	napis=[]
	for x in words:
		if len(x) > 2:
			napis.append(x.lower())
	#print(napis)
	return napis

def levenstein(word1, word2):
	if (word1 in word2) or (word2 in word1):
		return 1
	else:
		m = len(word1)
		n = len(word2)
		macierz = [[0 for x in range(m+1)] for y in range(n+1)]
		for i in range(0, n):
			macierz[i][0] = i
		for j in range(1, m):
			macierz[0][j] = j
	
		for i in range(1, n):
			for j in range(1, m):
				if (word1[j] == word2[i]):
					kimchi = 0
				else:
					kimchi = 1
				macierz[i][j] = min(macierz[i-1][j]+1, macierz[i][j-1]+1, macierz[i-1][j-1] + kimchi)

		wynik = macierz[n-1][m-1]
		#print("wypisuje: ",wynik, n, m )
		return 1-(wynik/min(n,m))
	
adres = open("addresses.txt", "r", encoding = "utf8")
klaster = [] #lista z listą klastrów
z = 0
for line in adres: #każdy adres po kolei
	i = 0
	print('%.2f%s' % (z / 6751 * 100, '%'))
	z=z+1
	check = 0 #nie ma w klastrze adresu
	newline = linijka(line) #małymi literami i bez 1- i 2-znakowych słów
	if klaster: #jeśli klaster nie jest pusty
		while(i < (len(klaster))):
			lev = levenstein(newline, klaster[i][0]) #najdłuższy podciągu

			if lev > 0.55: #metryka replit 13.2
				#print("\nMETRYKA ",lcs/(len(klaster[i][0])))
				#print("sprawdzam ", klaster[i][0], " z ", newline)
				check = check+1
				#print(i, " PAUZA ", klaster[i],"\n")
				if len(newline) > len(klaster[i][0]):
					klaster[i][0]=newline
				klaster[i].append(line) #dodaj do istniejącego klastra
				i = len(klaster)+1
			else:
				i=i+1		
	

		if check < 1: #jeśli nie ma miejsca dla adresu 
			
			help = [] #utwórz nowy klaster i tam dodaj
			help.append(newline)
			help.append(line)
			klaster.append(help)
	else: #pierwszy klaster
		help = []
		help.append(newline)
		help.append(line)
		klaster.append(help)
print(len(klaster))

plik = open('clusters.txt', 'w')
for i in klaster:
	iteri = iter(i)
	next(iteri)
	for j in iteri:
		plik.write(j)
		plik.write("\n")
	plik.write("###############\n\n")
plik.close()
		
	  
	
