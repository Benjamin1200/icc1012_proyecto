import matplotlib.pyplot as plt
import numpy as np


archivo = open("languages_amount_by_platform_summary.txt")

archivo.readline()
archivo.readline()
languages_nintendo = {}
languages_total = {}
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	try:
		languages_total[line[2]] += int(line[3])
	except:
		languages_total[line[2]] = int(line[3])
	try:
		languages_nintendo[line[2]] += int(line[3])
	except:
		languages_nintendo[line[2]] = int(line[3])


archivo.readline()
archivo.readline()
languages_playstation = {}
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	try:
		languages_total[line[2]] += int(line[3])
	except:
		languages_total[line[2]] = int(line[3])	
	try:
		languages_playstation[line[2]] += int(line[3])
	except:
		languages_playstation[line[2]] = int(line[3])


archivo.readline()
archivo.readline()
languages_xbox = {}
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	try:
		languages_total[line[2]] += int(line[3])
	except:
		languages_total[line[2]] = int(line[3])	
	try:
		languages_xbox[line[2]] += int(line[3])
	except:
		languages_xbox[line[2]] = int(line[3])


archivo.readline()
archivo.readline()
languages_others = {}
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	try:
		languages_total[line[2]] += int(line[3])
	except:
		languages_total[line[2]] = int(line[3])	
	try:
		languages_others[line[2]] += int(line[3])
	except:
		languages_others[line[2]] = int(line[3])

nintendo_count = []
playstation_count = []
xbox_count = []
others_count = []

for i in languages_total.keys():
	try:
		nintendo_count.append(languages_nintendo[i]/float(languages_total[i]))
	except:
		nintendo_count.append(0)
	try:
		playstation_count.append(languages_playstation[i]/float(languages_total[i]))
	except:
		playstation_count.append(0)
	try:
		xbox_count.append(languages_xbox[i]/float(languages_total[i]))
	except:
		xbox_count.append(0)
	try:
		others_count.append(languages_others[i]/float(languages_total[i]))
	except:
		others_count.append(0)



width= 1
x_valus=languages_total.keys()
ind=np.arange(len(x_valus))
ax = plt.subplot(111)
bottom=[1]*len(x_valus)
plt.xticks(ind + 0.5, x_valus, rotation=70)
bottom -= np.array(nintendo_count)
plt.bar(ind , nintendo_count, width,label='Nintendo', color='red', bottom=bottom)
bottom -= np.array(playstation_count)
plt.bar(ind, playstation_count, width,label='Playstation', bottom=bottom)
bottom -= np.array(xbox_count)
plt.bar(ind, xbox_count, width,label='Xbox', bottom=bottom, color='green')
bottom -= np.array(others_count)
plt.bar(ind, others_count, width,label='Others', bottom=bottom, color='yellow')
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Language Compare by Plataform")
plt.xlabel('Language')
plt.ylabel('Ratio')
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,1))
plt.show()
