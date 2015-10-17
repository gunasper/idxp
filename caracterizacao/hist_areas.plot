set auto x
set yrange [0:450]
set style data histogram
set style histogram cluster gap 1.5
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -90 scale 0
#set bmargin 10

set terminal 'png'
set output 'hist.png'
plot for [COL=2:2] 'hist_areas.dat' using 2:xticlabels(1) title columnheader
