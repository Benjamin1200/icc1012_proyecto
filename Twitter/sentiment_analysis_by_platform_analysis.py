import matplotlib.pyplot as plt
archivo = open("sentiment_analysis_by_platform_summary.txt")
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
for i in archivo:
    line = i.translate(None, ''.join(chars_to_remove))
    line = line.split()
    if line[2] == "pos":
        pos.append([int(line[0]), int(line[1]), int(line[3])])
    elif line[2] == "neg":
        neg.append([int(line[0]), int(line[1]), int(line[3])])
    else:
        neu.append([int(line[0]), int(line[1]), int(line[3])])

x_neg = []
x_neg_name = []
y_neg = []
count = 0
for i in sorted(neg):
    x_neg.append(count)
    x_neg_name.append(str(i[0])+ " " + str(i[1]))
    y_neg.append(i[2])
    count += 1

plt.xticks(x_neg, x_neg_name)
#neg_plt = plt.plot(x_neg, y_neg, 'r',label='negatives')

x_neu = []
x_neu_name = []
y_neu = []
count = 0
for i in sorted(neu):
    x_neu.append(count)
    x_neu_name.append(str(i[0])+ " " + str(i[1]))
    y_neu.append(i[2])
    count += 1

plt.xticks(x_neu, x_neu_name)
#neu_plt = plt.plot(x_neu, y_neu, 'b',label='neutral')


x_pos = []
x_pos_name = []
y_pos = []
count = 0
for i in sorted(pos):
    x_pos.append(count)
    x_pos_name.append(str(i[0])+ " " + str(i[1]))
    y_pos.append(i[2])
    count += 1

plt.xticks(x_pos, x_pos_name)
#os_plt = plt.plot(x_pos, y_pos, 'g', label='positive')
plt.legend(loc=2)
#plt.show()

