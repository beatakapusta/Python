import re

def linijka(line):
	words = re.split('[\W]+', line)
	napis=""
	for x in words:
		if len(x) > 2:
			napis = napis + " " + x
	return str(napis).lower()

def LCS(tab1,tab2):
        n = len(tab1)
        m = len(tab2)
        macierz = [[0 for x in range(n+1)] for y in range(m+1)]
        result = 0
        for i in range(n+1):
                for j in range(m+1):
                        if i == 0 or j == 0:
                                macierz[j][i] = 0
                        elif tab1[i-1] == tab2[j-1]:
                                macierz[j][i] = macierz[j-1][i-1] + 1
                                result  = max(result,macierz[j][i])
                        else:
                                macierz[j][i] = 0
        return result
	
adres = open("addresses.txt", "r", encoding = "utf8")
klaster = [] #lista z listą klastrów

for line in adres: #każdy adres po kolei
	i = 0
	check = 0 #nie ma w klastrze adresu
	newline = linijka(line) #małymi literami i bez 1- i 2-znakowych słów
	if klaster: #jeśli klaster nie jest pusty
		while(i < (len(klaster))):
			number = len(klaster[i][0])
			lcs = LCS(newline, klaster[i][0]) #najdłuższy podciągu

			if ((lcs/min(number,len(newline))) > 0.55): #metryka replit 13.2
				#print("\nMETRYKA ",lcs/(len(klaster[i][0])))
				#print("sprawdzam ", klaster[i][0], " z ", newline)
				check = check+1
				#print(i, " PAUZA ", klaster[i],"\n")
				if len(newline) < len(klaster[i][0]):
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
print(klaster)

#with open('klaster_wynik.txt', 'w') as plik:
#	plik.writelines("%s\n" % adres for adres in klaster)
#plik.close()
	
	  
	
