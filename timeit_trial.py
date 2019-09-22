import matplotlib.pyplot as plt
import timeit



main_str = """\
x = [1,2,4,7,3,7,8,4,4,9]
previous_value = None
new_lst = []

for elem in x:
   if elem != previous_value:
       new_lst.append(elem)
       previous_value = elem

"""

time1 = timeit.timeit(stmt=main_str, number=100000)
print(time1)
#===============================

x = [1,2,4,7,3,7,8,4,4,9]

main_str_2 = """\
x = [1,2,4,7,3,7,8,4,4,9]
result = [v for i, v in enumerate(x) if i == 0 or v != x[i-1]]"""

time2 = timeit.timeit(stmt=main_str_2, number=100000)
print(time2)
#=====================================




main_str_3 = """\
from itertools import groupby
x = [1,2,4,7,3,7,8,4,4,9]
result = [i[0] for i in groupby(x)]"""
time3 = timeit.timeit(stmt=main_str_3, number=100000)
print(time3)


plot_x = ["using For loops", "Using Enumerate", "Using itertools"]
plot_y = [time1, time2, time3]

bar = plt.bar(plot_x, plot_y)
bar[0].set_color('r')
bar[1].set_color('b')
bar[2].set_color('g')
plt.ylabel("Time")
plt.title("Time taken by each method")
plt.show()
