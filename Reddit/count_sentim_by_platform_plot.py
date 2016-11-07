import matplotlib.pyplot as plt
archivo = open("count_hour_by_platform_summary.txt")
archivo.readline()
pos = []
chars_to_remove = [',', '[', ']', '"']
for i in archivo:
	line = i.translate(None, ''.join(chars_to_remove))
	line = line.split()
	pos.append([int(line[0]), int(line[1]), int(line[2])])

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
pos_plt = plt.plot(x_pos, y_pos, 'g')
plt.show()