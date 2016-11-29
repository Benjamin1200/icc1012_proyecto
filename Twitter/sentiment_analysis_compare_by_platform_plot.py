import matplotlib.pyplot as plt
import numpy as np

archivo = open("sentiment_analysis_by_platform_summary.txt")
archivo.readline()
archivo.readline()
pos_nintendo = 0
neg_nintendo = 0
neu_nintendo = 0
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] == "pos":
		pos_nintendo += int(line[3])
	elif line[2] == "neg":
		neg_nintendo += int(line[3])
	else:
		neu_nintendo += int(line[3])

########################################
#############Playstation################
########################################

archivo.readline()
archivo.readline()
pos_playstation = 0
neg_playstation = 0
neu_playstation = 0
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] == "pos":
		pos_playstation += int(line[3])
	elif line[2] == "neg":
		neg_playstation += int(line[3])
	else:
		neu_playstation += int(line[3])

########################################
#################Xbox###################
########################################

archivo.readline()
archivo.readline()
pos_xbox = 0
neg_xbox = 0
neu_xbox = 0
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] == "pos":
		pos_xbox += int(line[3])
	elif line[2] == "neg":
		neg_xbox += int(line[3])
	else:
		neu_xbox += int(line[3])

########################################
#################Others#################
########################################

archivo.readline()
archivo.readline()
pos_others = 0
neg_others = 0
neu_others = 0
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] == "pos":
		pos_others += int(line[3])
	elif line[2] == "neg":
		neg_others += int(line[3])
	else:
		neu_others += int(line[3])


total_pos = float(pos_nintendo + pos_xbox + pos_playstation + pos_others)
total_neg = float(neg_others + neg_xbox + neg_playstation + neg_nintendo)
total_neu = float(neu_others + neu_xbox + neu_playstation + neu_nintendo)

nintendo_plot = [float(pos_nintendo/total_pos), float(neg_nintendo/total_neg), float(neu_nintendo/total_neu)]
playstation_plot = [float(pos_playstation/total_pos), float(neg_playstation/total_neg), float(neu_playstation/total_neu)]
xbox_plot = [float(pos_xbox/total_pos), float(neg_xbox/total_neg), float(neu_xbox/total_neu)]
others_plot = [float(pos_others/total_pos), float(neg_others/total_neg), float(neu_others/total_neu)]
ind=np.arange(3)
width= 1
x_valus=['Positive', 'Negative', 'Neutral']
ax = plt.subplot(111)
bottom=[1]*3
plt.xticks(ind + 0.5, x_valus)
bottom -= np.array(nintendo_plot)
plt.bar(ind , nintendo_plot, width,label='Nintendo', color='red', bottom=bottom)
bottom -= np.array(playstation_plot)
plt.bar(ind, playstation_plot, width,label='Playstation', bottom=bottom)
bottom -= np.array(xbox_plot)
plt.bar(ind, xbox_plot, width,label='Xbox', bottom=bottom, color='green')
bottom -= np.array(others_plot)
plt.bar(ind, others_plot, width,label='Others', bottom=bottom, color='yellow')
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Sentiment Compare by Plataform")
plt.xlabel('Sentiment')
plt.ylabel('Ratio')
plt.axis([0, 3, 0, 1])
plt.show()