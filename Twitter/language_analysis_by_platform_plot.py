import matplotlib.pyplot as plt
from itertools import cycle
cycol = cycle('bgrcmk').next
archivo = open("languages_amount_by_platform_summary.txt")
archivo.readline()
archivo.readline()
languages = {}
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] not in languages.keys():
		languages[line[2]] = []
	languages[line[2]].append([int(line[0]), int(line[1]), int(line[3])])
ax = plt.subplot(111)
for i in languages.keys():
	x = []
	x_name = []
	y = []
	count = 0
	for j in sorted(languages[i]):
		x.append(count)
		x_name.append(str(j[0])+ " " + str(j[1]))
		y.append(j[2])
		count += 1

	plt.xticks(x, x_name)
	plt.plot(x, y,label=i)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

archivo.readline()
archivo.readline()
languages = {}
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] not in languages.keys():
		languages[line[2]] = []
	languages[line[2]].append([int(line[0]), int(line[1]), int(line[3])])
ax = plt.subplot(111)
for i in languages.keys():
	x = []
	x_name = []
	y = []
	count = 0
	for j in sorted(languages[i]):
		x.append(count)
		x_name.append(str(j[0])+ " " + str(j[1]))
		y.append(j[2])
		count += 1

	plt.xticks(x, x_name)
	plt.plot(x, y,label=i)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()