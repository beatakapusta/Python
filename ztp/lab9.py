def ramenya(ramen,slowo):
	i = 0
	n = len(slowo)
	word = []
	word.extend(slowo)
	while( i < n-1 ):
		if( i < n-2):
			udon = word[i]+word[i+1]
			if udon in ramen:
				word[i] = udon
				word.remove(word[i+1])
				i = i + 1
		i = i + 1

	return word

def czy(word1,word2,i,j,slownik):

	if(word1[i] in slownik.keys())and(slownik[word1[i]] == word2[j]):
		return 1
	elif(word2[j] in slownik.keys()):
		if(slownik[word2[j]] == word1[i] ):
			return 1

def czeski(word1,word2,i,j):
	if (word1[i+1] == word2[j] and word1[i] == word2[j+1]):
		return 1
	elif(word1[i-1] == word2[j] and word1[i] == word2[j-1]):
		return 1

def czy_blad(word1,word2, i,j,n,m,niku, oden):
	if(i<n-1 and j<m-1):
		czy_dia = czy(word1,word2,i, j+1,niku)
		czy_dia2 = czy(word1,word2, i+1, j, niku)
		czy_ort = czy(word1,word2, i, j+1, oden)
		czy_ort2 = czy(word1,word2,i+1, j, oden)
	#	print("czy czeski?")
		if(czy_dia == 1 or  czy_dia2 == 1): 
			czy_czeski = 0
		elif(czy_ort2 == 1 or  czy_ort == 1):
			czy_czeski = 2
		else:
			czy_czeski = czeski(word1,word2,i,j)
	
	#	print(word1[i],word2[j],czy_czeski)
		return czy_czeski

def  levensteinA(word1, word2):
  # ----> do uzupełnienia
	niku = {'ą':'a','ę':'e','ó':'o','ż':'z','ź':'z','ć':'c','ń':'n','ł':'l','ś':'s'}
	ramen = ['rz']
	oden = {'ż':'rz','u':'ó','ch':'h'}
#	word1 = ramenya(ramen,word1)
#	word2 = ramenya(ramen,word2)
	n = len(word1)
	m = len(word2)
#	print(n,m, word1, word2)
	macierz = [[0 for x in range(n+1)] for y in range(m+1)]
#	print(macierz)
	for i in range(0,n+1):
		macierz[0][i] = i
		
	for j in range(0,m+1):
		macierz[j][0] = j

#	print(macierz)
	for i in range(0,n):
		for j in range(0,m):
			czy_diakrytyczny = czy(word1,word2,i,j,niku)
		#	print('czy_d', word1, word2, word1[i], word2[j],czy_diakrytyczny)
			czy_ortograficzny = czy(word1,word2,i,j,oden)
		#	print('czy_o', word1, word2, word1[i], word2[j],czy_ortograficzny)
			czy_czeski = czy_blad(word1,word2, i,j,n,m,niku,oden)
		#	print('czy_czeski', word1, word2, word1[i], word2[j],czy_czeski)
			if(word1[i] == word2[j]):
				kimchi = 0
	#			print("znaki są takie same")
			# znaki diakrytyczne
			elif( czy_diakrytyczny == 1):
				kimchi = 0.2
	#			print("znaki są dia")
			#błędy ortograficzne
			elif( czy_ortograficzny == 1):
				kimchi = 0.5
	#			print("znaki zawierają błąd ort")
			# czeskie błędy
			elif( czy_czeski ):
				if(czy_czeski == 1):  
					kimchi = 0.5
	#				print("czeski błąd")
				elif(czy_czeski == 0):
					kimchi = 0.7
	#				print("czeski bł + dia")
				elif(czy_czeski == 2):
					kimchi = 1
	#				print("czeski + ort")
			else:
				kimchi = 1
			
			macierz[j+1][i+1] = min(macierz[j+1][i]+1, macierz[j][i+1]+1, macierz[j][i] + kimchi)
		
	wynik = macierz[m][n]
#	print(macierz)
	return wynik
				
###############################################
def  levensteinB(word1, word2):
  # ----> do uzupełnienia
        niku = {'ą':'a','ę':'e','ó':'o','ż':'z','ź':'z','ć':'c','ń':'n','ł':'l','ś':'s'}
        ramen = ['ch','rz','dz','dż','dź']
        oden = {'ż':'rz','u':'ó','ch':'h'}
#       word1 = ramenya(ramen,word1)
#       word2 = ramenya(ramen,word2)
        n = len(word1)
        m = len(word2)
#       print(n,m, word1, word2)
        macierz = [[0 for x in range(n+1)] for y in range(m+1)]
#       print(macierz)
        for i in range(0,n+1):
                macierz[0][i] = i

        for j in range(0,m+1):
                macierz[j][0] = j

#       print(macierz)
        for i in range(0,n):
                for j in range(0,m):
                        czy_diakrytyczny = czy(word1,word2,i,j,niku)
                #       print('czy_d', word1, word2, word1[i], word2[j],czy_diakrytyczny)
                        czy_ortograficzny = czy(word1,word2,i,j,oden)
                #       print('czy_o', word1, word2, word1[i], word2[j],czy_ortograficzny)
                        czy_czeski = czy_blad(word1,word2, i,j,n,m,niku,oden)
                #       print('czy_czeski', word1, word2, word1[i], word2[j],czy_czeski)

                        if(word1[i] == word2[j]):
                                kimchi = 0
        #                       print("znaki są takie same")
                        # znaki diakrytyczne
                        elif( czy_diakrytyczny == 1):
                                kimchi = 0.2
        #                       print("znaki są dia")
                        #błędy ortograficzne
                        elif( czy_ortograficzny == 1):
                                kimchi = 0.5
        #                       print("znaki zawierają błąd ort")
                        # czeskie błędy
                        elif( czy_czeski ):
                                if(czy_czeski == 1):
                                        kimchi = 0.25
        #                               print("czeski błąd")
                                elif(czy_czeski == 0):
                                        kimchi = 0.7
        #                               print("czeski bł + dia")
                                elif(czy_czeski == 2):
                                        kimchi = 1
        #                               print("czeski + ort")
                        else:
                                kimchi = 1

                        macierz[j+1][i+1] = min(macierz[j+1][i]+1, macierz[j][i+1]+1, macierz[j][i] + kimchi)

        wynik = macierz[m][n]
#       print(macierz)
        return wynik

###############################################
def levenstein(w1,w2):
	return min(levensteinA(w1,w2),levensteinB(w1,w2))


