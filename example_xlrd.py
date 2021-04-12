import matplotlib.pyplot as plt
import xlrd
from pylab import *
from xlrd import open_workbook
x_data = []
y_data = []
x_volte=[]
temp=[]
wb = open_workbook('my_data.xlsx')

for s in wb.sheets():
    print('Sheets:', s.name)
    for row in range(s.nrows):
        print('the row is:', row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)
        x_data.append(values[0])
        y_data.append(values[1])

plt.plot(x_data, y_data, 'bo-', label='Phase curve', linewidth=1)
plt.title('TR14 phase detector')
plt.legend(loc='upper left')

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.xlabel('input-deg')
plt.ylabel('output-V')

plt.show()
print('over!')