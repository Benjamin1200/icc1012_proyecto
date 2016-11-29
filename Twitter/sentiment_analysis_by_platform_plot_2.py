import matplotlib.pyplot as plt
import numpy as np

archivo = open("sentiment_analysis_by_platform_summary.txt")

########################################
###############Nintendo#################
########################################

archivo.readline()
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] == "pos":
		pos.append([int(line[0]), int(line[1]), int(line[3])])
	elif line[2] == "neg":
		neg.append([int(line[0]), int(line[1]), int(line[3])])
	else:
		neu.append([int(line[0]), int(line[1]), int(line[3])])
neg.pop()
n= len(neg)
neg = sorted(neg)
neu = sorted(neu)
pos = sorted(pos)
for i in xrange(n):
	suma = float(neg[i][2]+neu[i][2]+pos[i][2])
	neu[i][2] = neu[i][2]/suma
	pos[i][2] = pos[i][2]/suma
	neg[i][2] = neg[i][2]/suma
width= 1
ind=np.arange(n)

x_neg_name = []
y_neg = []

ax = plt.subplot(111)
for i in sorted(neg):
	x_neg_name.append(str(i[0])+ " " + str(i[1]))
	y_neg.append(i[2])

plt.xticks(ind + width/2, x_neg_name)
neg_plt = plt.bar(0.6 + ind, y_neg,width, color="red",label='negatives', edgecolor = "none")

x_neu_name = []
y_neu = []

for i in sorted(neu):
	x_neu_name.append(str(i[0])+ " " + str(i[1]))
	y_neu.append(i[2])

plt.xticks(ind + width/2, x_neu_name)
neu_plt = plt.bar(0.6 + ind, y_neu, width,color="blue",label='neutral',bottom=y_neg, edgecolor = "none")



x_pos_name = []
y_pos = []

for i in sorted(pos):
	x_pos_name.append(str(i[0])+ " " + str(i[1]))
	y_pos.append(i[2])


plt.xticks(ind + width/2, x_pos_name)
pos_plt = plt.bar(0.6 + ind, y_pos, width,color="green", label='positive', bottom=np.array(y_neu)+np.array(y_neg), edgecolor = "none")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Nintendo")
plt.xlabel('Week & Hour')
plt.ylabel('Ratio')
plt.show()

########################################
#############Playstation################
########################################

archivo.readline()
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] == "pos":
		pos.append([int(line[0]), int(line[1]), int(line[3])])
	elif line[2] == "neg":
		neg.append([int(line[0]), int(line[1]), int(line[3])])
	else:
		neu.append([int(line[0]), int(line[1]), int(line[3])])
neg.pop()
n= len(neg)
neg = sorted(neg)
neu = sorted(neu)
pos = sorted(pos)

for i in xrange(n):
	suma = float(neg[i][2]+neu[i][2]+pos[i][2])
	neu[i][2] = neu[i][2]/suma
	pos[i][2] = pos[i][2]/suma
	neg[i][2] = neg[i][2]/suma

width= 1
ind=np.arange(n)

x_neg_name = []
y_neg = []

ax = plt.subplot(111)
for i in sorted(neg):
	x_neg_name.append(str(i[0])+ " " + str(i[1]))
	y_neg.append(i[2])
	
plt.xticks(ind + width/2, x_neg_name)
neg_plt = plt.bar(0.6 + ind, y_neg,width, color="red",label='negatives', edgecolor = "none")

x_neu_name = []
y_neu = []

for i in sorted(neu):
	x_neu_name.append(str(i[0])+ " " + str(i[1]))
	y_neu.append(i[2])
	
plt.xticks(ind + width/2, x_neu_name)
neu_plt = plt.bar(0.6 + ind, y_neu, width,color="blue",label='neutral',bottom=y_neg, edgecolor = "none")

x_pos_name = []
y_pos = []

for i in sorted(pos):
	x_pos_name.append(str(i[0])+ " " + str(i[1]))
	y_pos.append(i[2])

plt.xticks(ind + width/2, x_pos_name)
pos_plt = plt.bar(0.6 + ind, y_pos, width,color="green", label='positive', bottom=np.array(y_neu)+np.array(y_neg), edgecolor = "none")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Playstation")
plt.xlabel('Week & Hour')
plt.ylabel('Ratio')
plt.show()

########################################
#################Xbox###################
########################################

archivo.readline()
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] == "pos":
		pos.append([int(line[0]), int(line[1]), int(line[3])])
	elif line[2] == "neg":
		neg.append([int(line[0]), int(line[1]), int(line[3])])
	else:
		neu.append([int(line[0]), int(line[1]), int(line[3])])
n= len(neg)
neg = sorted(neg)
neu = sorted(neu)
pos = sorted(pos)

for i in xrange(n):
	suma = float(neg[i][2]+neu[i][2]+pos[i][2])
	neu[i][2] = neu[i][2]/suma
	pos[i][2] = pos[i][2]/suma
	neg[i][2] = neg[i][2]/suma

width= 1
ind=np.arange(n)

x_neg_name = []
y_neg = []

ax = plt.subplot(111)
for i in sorted(neg):
	x_neg_name.append(str(i[0])+ " " + str(i[1]))
	y_neg.append(i[2])

plt.xticks(ind + width/2, x_neg_name)
neg_plt = plt.bar(0.6 + ind, y_neg,width, color="red",label='negatives', edgecolor = "none")

x_neu_name = []
y_neu = []

for i in sorted(neu):
	x_neu_name.append(str(i[0])+ " " + str(i[1]))
	y_neu.append(i[2])
	
plt.xticks(ind + width/2, x_neu_name)
neu_plt = plt.bar(0.6 + ind, y_neu, width,color="blue",label='neutral',bottom=y_neg, edgecolor = "none")

x_pos_name = []
y_pos = []

for i in sorted(pos):
	x_pos_name.append(str(i[0])+ " " + str(i[1]))
	y_pos.append(i[2])
	

plt.xticks(ind + width/2, x_pos_name)
pos_plt = plt.bar(0.6 + ind, y_pos, width,color="green", label='positive', bottom=np.array(y_neu)+np.array(y_neg), edgecolor = "none")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Xbox")
plt.xlabel('Week & Hour')
plt.ylabel('Ratio')
plt.show()

########################################
#################Others#################
########################################

archivo.readline()
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
while True:
	i = archivo.readline()
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	if len(line) == 0:
		break
	if line[2] == "pos":
		pos.append([int(line[0]), int(line[1]), int(line[3])])
	elif line[2] == "neg":
		neg.append([int(line[0]), int(line[1]), int(line[3])])
	else:
		neu.append([int(line[0]), int(line[1]), int(line[3])])
neu.pop()
n= len(neu)
neg = sorted(neg)
neu = sorted(neu)
pos = sorted(pos)

for i in xrange(n):
	suma = float(neg[i][2]+neu[i][2]+pos[i][2])
	neu[i][2] = neu[i][2]/suma
	pos[i][2] = pos[i][2]/suma
	neg[i][2] = neg[i][2]/suma

width= 1
ind=np.arange(n)

x_neg_name = []
y_neg = []

ax = plt.subplot(111)
for i in sorted(neg):
	x_neg_name.append(str(i[0])+ " " + str(i[1]))
	y_neg.append(i[2])

plt.xticks(ind + width/2, x_neg_name)
neg_plt = plt.bar(0.6 + ind, y_neg,width, color="red",label='negatives', edgecolor = "none")


x_neu_name = []
y_neu = []

for i in sorted(neu):
	x_neu_name.append(str(i[0])+ " " + str(i[1]))
	y_neu.append(i[2])

plt.xticks(ind + width/2, x_neu_name)
neu_plt = plt.bar(0.6 + ind, y_neu, width,color="blue",label='neutral',bottom=y_neg, edgecolor = "none")

x_pos_name = []
y_pos = []

for i in sorted(pos):
	x_pos_name.append(str(i[0])+ " " + str(i[1]))
	y_pos.append(i[2])

plt.xticks(ind + width/2, x_pos_name)
pos_plt = plt.bar(0.6 + ind, y_pos, width,color="green", label='positive', bottom=np.array(y_neu)+np.array(y_neg), edgecolor = "none")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Others")
plt.xlabel('Week & Hour')
plt.ylabel('Ratio')
plt.show()

