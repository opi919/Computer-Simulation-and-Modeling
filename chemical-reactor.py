import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = [1.0]
b = [0.5]
c = [0.0]

k1, k2 = 0.5, 0.05

totalTime = 100
noOfSteps = 500
dt = totalTime / noOfSteps

fig, ax = plt.subplots()
ax.set_xlim(0, (totalTime / dt))
ax.set_ylim(0, 1)

# empty lines for a,b,c
(line_a,) = ax.plot([], [], label="a")
(line_b,) = ax.plot([], [], label="b")
(line_c,) = ax.plot([], [], label="c")

currentTime = 0

def animation(frame):
    global currentTime, totalTime
    if currentTime <= totalTime:
        a_new = a[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt
        b_new = b[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt
        c_new = c[-1] + (2 * k1 * a[-1] * b[-1] - 2 * k2 * c[-1]) * dt

        a.append(a_new)
        b.append(b_new)
        c.append(c_new)
        currentTime += dt

    line_a.set_data(range(len(a)), a)
    line_b.set_data(range(len(b)), b)
    line_c.set_data(range(len(c)), c)

    ax.legend()

animated = FuncAnimation(fig, animation, frames=noOfSteps, interval=1, repeat=False)

plt.xlabel("Time (s)")
plt.ylabel("Concentration (mole)")
plt.title("Concentration vs Time")
plt.grid()
plt.show()
