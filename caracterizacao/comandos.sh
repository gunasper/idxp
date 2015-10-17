#histograma dos valores presentes no dataset
cat treino | cut -f 2 -d ',' | sort | uniq -c | awk '{print $2"\t"$1}' > hist_areas.dat

#calculo de min, max, média e desvio padrão para área A001
cat treino | grep A001 | cut -f 3- -d ',' | sed 's/,,/,-100,/g' | python minMamx.py > estA001.dat
