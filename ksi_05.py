import numpy as np
import matplotlib.pyplot as plt

# стационарные значения
stat = [[3, 10],
		[3.5, 10], [3.5, 10.5], [3.5, 11], [3.5, 11.5], [3.5, 12], [3.5, 12.5],
		[4, 9], [4, 9.5],
		[4.5, 8.5], [4.5, 9],
		[5, 6.5], [5, 7], [5, 7.5], [5, 8], [5, 8.5],
		[5.5, 7.5], [5.5, 8],
		[6, 7], [6, 7.5],
		[6.5, 6.5], [6.5, 7],
		[7, 6.5],
		[7.5, 6.5],
		[8, 6],
		[8.5, 5.5],
		[9, 5],
		[9.5, 5],
		[10, 4.5],
		[10.5, 4],
		[11, 4]
		]
# нестационарные значения
nonstat = [ [4, 10], [4, 10.5], [4, 11],
			[4.5, 9.5],
			[5, 9],
			[5.5, 8.5],
			[6, 8],
			[6.5, 7.5],
			[7, 7],
			[7.5, 7],
			[8, 6.5], [8, 7],
			[8.5, 6], [8.5, 6.5],
			[9, 5.5], [9, 6], [9, 6.5],
			[9.5, 5.5],
			[10, 5],
			[10.5, 4.5], [10.5, 5],
			[11, 4.5],
			[11.5, 4], [11.5, 4.5]
		]
# значения, которые сейчас считаются
temp = [[3.5, 13], 
		[11.5, 3.5]]

# вынимаем из массива stat все x и y
# рисуем стационарные значения
x = []
y = []
for row in stat:
	x.append(row[0])
	y.append(row[1])

fig, ax = plt.subplots()
ax.plot(x, y, 'ko')

x.clear()
y.clear()

# рисуем нестационарные значения
for row in nonstat:
	x.append(row[0])
	y.append(row[1])

ax.plot(x, y, 'ro')

x.clear()
y.clear()

# рисуем временные значения
for row in temp:
	x.append(row[0])
	y.append(row[1])
ax.plot(x, y, 'bx')



# рисуем сетку
ticks = np.arange(0, 15, 0.5)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.grid(which='both')

# plt.savefig(folder + 'T_t='+str(int(time[0]))+'-'+str(int(time[-1]))+'.jpg', format='jpg', dpi=1000)

plt.show()