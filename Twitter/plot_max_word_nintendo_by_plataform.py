import sys
import json
import operator
import numpy as np
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf8')

archivo = open("count_words_by_platform_summary.txt")

########################################
###############Nintendo#################
########################################

archivo.readline()
archivo.readline()
nintendo_count = {}
chars_to_remove = [',', '[', ']', '"']
fechas = set()
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	fechas.add((int(line[0]),int(line[1])))
	if line[2] == "nintendo":
		try:
			nintendo_count[(int(line[0]),int(line[1]))] += int(line[3])
		except:
			nintendo_count[(int(line[0]),int(line[1]))] = int(line[3])

########################################
###############Nintendo#################
########################################

archivo.readline()
archivo.readline()
playstation_count = {}
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	fechas.add((int(line[0]),int(line[1])))
	if line[2] == "nintendo":
		try:
			playstation_count[(int(line[0]),int(line[1]))] += int(line[3])
		except:
			playstation_count[(int(line[0]),int(line[1]))] = int(line[3])

########################################
###############Nintendo#################
########################################

archivo.readline()
archivo.readline()
xbox_count = {}
chars_to_remove = [',', '[', ']', '"']
fechas = set()
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	fechas.add((int(line[0]),int(line[1])))
	if line[2] == "nintendo":
		try:
			xbox_count[(int(line[0]),int(line[1]))] += int(line[3])
		except:
			xbox_count[(int(line[0]),int(line[1]))] = int(line[3])

########################################
###############Nintendo#################
########################################

archivo.readline()
archivo.readline()
other_count = {}
chars_to_remove = [',', '[', ']', '"']
fechas = set()
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	fechas.add((int(line[0]),int(line[1])))
	if line[2] == "nintendo":
		try:
			other_count[(int(line[0]),int(line[1]))] += int(line[3])
		except:
			other_count[(int(line[0]),int(line[1]))] = int(line[3])

nintendo_plt = []
playstation_plt = []
xbox_plt = []
other_plt = []

for i in fechas:
	try:
		nintendo_plt.append(nintendo_count[i])
	except:
		nintendo_plt.append(0)
	try:
		playstation_plt.append(playstation_count[i])
	except:
		playstation_plt.append(0)
	try:
		xbox_plt.append(xbox_count[i])
	except:
		xbox_plt.append(0)
	try:
		other_plt.append(other_count[i])
	except:
		other_plt.append(0)
width = 1
ind=np.arange(len(fechas))
ax = plt.subplot(111)
plt.xticks(ind, fechas)
nn_plt = plt.plot(ind, nintendo_plt,color="red", label='nintendo')
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Word: Nintendo")
plt.xlabel('Week & Hour')
plt.ylabel('Count')
plt.show()

width = 1
ind=np.arange(len(fechas))
ax = plt.subplot(111)
plt.xticks(ind, fechas)
ply_plt = plt.plot(ind, playstation_plt,color="blue", label='playstation')
plt.xticks(ind, fechas)
xbx_plt = plt.plot(ind, xbox_plt,color="green", label='xbox')
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Word: Nintendo")
plt.xlabel('Week & Hour')
plt.ylabel('Count')
plt.show()


