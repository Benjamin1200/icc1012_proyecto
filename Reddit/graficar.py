import matplotlib.pyplot as plt
y = [7962, 9521, 19322]
x = [0, 1, 2]
x_name = ['neg', 'neu', 'pos']
plt.xticks(x, x_name)
plt.plot(x, y, 'ro')
axes = plt.gca()
axes.set_xlim([-1,3])
plt.show()