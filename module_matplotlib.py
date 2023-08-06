from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

import random
style.use("ggplot")


# Graphs ...

X = [i for i in range(1, 10, 1)]
Y = [random.randint(1, 10) for _ in range(9)]
Y1 = [random.randint(1, 10) for _ in range(9)]
Y2 = [random.randint(1, 10) for _ in range(9)]

plt.plot(X, Y)  # plot(x_axis, y_axis)
plt.plot(X, Y1, "c", label = "Line one" , linewidth = 5)
plt.plot(X, Y2, "g", label = "Line two" , linewidth = 5)

plt.title("Info")
plt.xlabel("X - Axis")
plt.ylabel("Y - axis")

plt.legend()

plt.grid(True , color = "y")
plt.show()

# Bars ...

plt.figure(2)
X1 = [2 *i for i in range(5)]
X2 = [2 *i - 1 for i in range(5)]
Y1 = [random.randint(1, 10) for _ in range(5)]
Y2 = [random.randint(1, 10) for _ in range(5)]
plt.bar(X1, Y1, label = "DATA_SET_1", color = "b")
plt.bar(X2, Y2, label = "DATA_SET_2", color = "y")
plt.legend()
plt.xlabel("Frequency")
plt.ylabel("no_of_students")
plt.title("Info")
plt.show()

# Histograms ..

plt.figure(3)
data = [random.randint(1, 10) for _ in range(100)]

plt.hist(data, X, histtype = "bar", rwidth = 0.5)
plt.xlabel("X")
plt.ylabel("Data")
plt.title("Histograms")
plt.show()

# Scatters..
 
plt.figure(4)

plt.scatter(X1, Y1, label = "skitskat", color = "k", marker = "s", s = 25  )
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatters")
plt.legend()
plt.show()

# stack plot ..

plt.figure(5)
Y = [1, 5, 3, 2, 5, 4 ,7, 6, 7]
Y1 = [9 , 8, 6, 5, 6, 4, 5, 3, 4]
Y2 = [4, 1, 5, 7, 3,  6, 2, 5, 3]
plt.plot([],[], color = "k", label = "Y", linewidth = 3)
plt.plot([],[], color = "m", label = "Y1", linewidth = 3)
plt.plot([],[], color = "c", label = "Y2", linewidth = 3)

plt.stackplot(X, Y, Y1, Y2, colors = ["k", "m", "c"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("stack plot")
plt.legend()
plt.show()

# pie chart ...

plt.figure(6)
Y  = [random.randint(1, 15)  for _ in range(5)]
act = ["A", "B", "C", "D", "E"]
col = ["m", "b", "y", "c", "g"]
plt.pie(Y, labels = act, colors = col, startangle = 90, explode = (0.1, 0.1, 0.1, 0.1, 0.1), shadow = True, autopct = "%0.2f%%")
plt.title("Pie chart")
plt.show()



# Subplots ...
plt.figure(7)
def fun(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


T1 = np.arange(0.0, 5, 0.1)
T2 = np.arange(0.0, 5, 0.05)

plt.subplot(211)
plt.plot(T1, fun(T1), "bo", T2, fun(T2))

plt.subplot(212)
plt.scatter(T2, np.cos(2 * np.pi * T2), color = "r", marker = "s", s = 5)
plt.show()