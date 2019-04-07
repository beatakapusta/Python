slownik = open("odm.txt", "r")
import lab9
import re
sjp = list(slownik)

def linijka(line):
	words = re.split('[\W\d]+', line)
	napis=""
	for x in words:
		if len(x) > 2:
			napis = napis + " " + x
	return str(napis).lower()

def czy_w_slowniku(text):
	for j in sjp:
		if text in j:
			return True

text = input("Podaj tekst:\n")

x = linijka(text)
text = text.split()
#print("Po preprocesingu:", x)
podobienstwo = 10
x = x.split()
for i in range(len(x)):
	poprawne_slowo= ""
	if czy_w_slowniku(x[i]) != True: 
		for j in sjp:
			j = j.replace(","," ")
			z = j.split()
			for k in z:
				if len(k)<len(x[i])+3 and len(k)>len(x[i])-3:
			#	print(x[i],k)
					wynik = lab9.levenstein(x[i],k)
			#	print(wynik)
					if wynik < podobienstwo:
						podobienstwo = wynik
						poprawne_slowo = k
		print("%s -> %s" % (x[i], poprawne_slowo))
		for m in range(len(text)):
			if x[i] == text[m]:
				text[m] = poprawne_slowo
				podobienstwo = 10

#print(x)
print(' '.join(text))
