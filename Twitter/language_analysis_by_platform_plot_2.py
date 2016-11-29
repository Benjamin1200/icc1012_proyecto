import matplotlib.pyplot as plt
import numpy as np
import random

archivo = open("languages_amount_by_platform_summary.txt")

########################################
###############Nintendo#################
########################################

archivo.readline()
archivo.readline()
languages = {}
chars_to_remove = [',', '[', ']', '"']
fechas = set()
suma_fechas = {}
width= 1
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] not in languages.keys():
		languages[line[2]] = []
	languages[line[2]].append([(int(line[0]), int(line[1])), int(line[3])])
	try:
		suma_fechas[(int(line[0]), int(line[1]))] += int(line[3])
	except:
		suma_fechas[(int(line[0]), int(line[1]))] = int(line[3])
	fechas.add((int(line[0]), int(line[1])))
fechas = sorted(fechas)
bottom = [0]*len(fechas)
ax = plt.subplot(111)
for i in languages.keys():
	color=(random.random(),random.random(),random.random())
	x = []
	x_name = []
	y = []
	count = 0
	inicio_len = 0
	leng = sorted(languages[i])
	n =len(leng)
	for j in xrange(len(fechas)):
		x.append(count)
		x_name.append(str(fechas[j][0])+ " " + str(fechas[j][1]))
		if inicio_len < n:
			if leng[inicio_len][0] == fechas[j]:
				y.append(leng[inicio_len][1]/float(suma_fechas[fechas[j]]))
				inicio_len += 1
				count += 1
			else:
				y.append(0)
				count += 1
		else:
			y.append(0)
			count += 1
	plt.xticks(x, x_name)
	plt.bar(x, y,width,label=i,bottom=bottom, edgecolor = "none", color=color)
	bottom += np.array(y)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
plt.title("Nintendo")
plt.xlabel('Week & Hour')
plt.ylabel('Ratio')
plt.show()

########################################
#############Playstation################
########################################

archivo.readline()
archivo.readline()
languages = {}
chars_to_remove = [',', '[', ']', '"']
fechas = set()
suma_fechas = {}
width= 1
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] not in languages.keys():
		languages[line[2]] = []
	languages[line[2]].append([(int(line[0]), int(line[1])), int(line[3])])
	try:
		suma_fechas[(int(line[0]), int(line[1]))] += int(line[3])
	except:
		suma_fechas[(int(line[0]), int(line[1]))] = int(line[3])
	fechas.add((int(line[0]), int(line[1])))
fechas = sorted(fechas)
bottom = [0]*len(fechas)
ax = plt.subplot(111)
for i in languages.keys():
	color=(random.random(),random.random(),random.random())
	x = []
	x_name = []
	y = []
	count = 0
	inicio_len = 0
	leng = sorted(languages[i])
	n =len(leng)
	for j in xrange(len(fechas)):
		x.append(count)
		x_name.append(str(fechas[j][0])+ " " + str(fechas[j][1]))
		if inicio_len < n:
			if leng[inicio_len][0] == fechas[j]:
				y.append(leng[inicio_len][1]/float(suma_fechas[fechas[j]]))
				inicio_len += 1
				count += 1
			else:
				y.append(0)
				count += 1
		else:
			y.append(0)
			count += 1
	plt.xticks(x, x_name)
	plt.bar(x, y,width,label=i,bottom=bottom, edgecolor = "none", color=color)
	bottom += np.array(y)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Playstation")
plt.xlabel('Week & Hour')
plt.ylabel('Ratio')
plt.show()