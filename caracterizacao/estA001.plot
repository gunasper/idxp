set title "Variação observada dos valores de RSS numa mesma área"
set auto x
set yrange [0:120]
set style data histogram

set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -90 scale 0
#set bmargin 10

# We need to set lw in order for error bars to actually appear.
set style histogram errorbars linewidth 1
# Make the bars semi-transparent so that the errorbars are easier to see.
set style fill solid 0.3
set bars front

set terminal 'png'
set output 'estA001.png'
plot 'estA001' using 4:2:3:xticlabels(1) title "Valor médio dos RSS observados"
