#!/usr/bin/gnuplot

set terminal pngcario size 1024,768
set putput 'cos.png'
#unset key

set xrange[1:61259]
set yrange[1:20000]

set logscale x 
set logscale y

maks = 19763
set datafile separator ","
plot \
	'kimchi.csv' using 1:3 pt 7 ps 1 title 'csv', \
	maks/x, \
	maks/x**2, \
	maks/
