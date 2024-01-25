# from ahnaf
import matplotlib.pyplot as plt


def pure_pursuit(x_bomber, y_bomber, xf, yf, fighter_speed):
    x_fighter = []
    y_fighter = []
    time = 0
    escape_distance, caught_distance = 900, 10

    while True:
        x_fighter.append(xf)
        y_fighter.append(yf)

        plt.clf()
        plt.title("Simulation of a Pure Pursuit")
        plt.plot(x_fighter, y_fighter, marker="o", label="Fighter")
        plt.plot(
            x_bomber[0 : time + 1], y_bomber[0 : time + 1], marker="o", label="Bomber"
        )
        plt.xlim(-100, 200)
        plt.ylim(-100, 100)
        plt.legend()
        plt.grid()
        plt.pause(1)

        distance = ((xf - x_bomber[time]) ** 2 + (yf - y_bomber[time]) ** 2) ** 0.5
        if distance < caught_distance:
            print(f"Target caught at {time} second")
            plt.close()
            break
        if distance > escape_distance or time > len(x_bomber):
            print(f"Target escaped at {time} second")
            break

        sin = (y_bomber[time] - yf) / distance
        cos = (x_bomber[time] - xf) / distance
        time += 1
        xf += fighter_speed * cos
        yf += fighter_speed * sin

    plt.show()


def main():
    xb = [80, 90, 99, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180]
    yb = [0, -2, -5, -9, -15, -18, -23, -29, -28, -25, -21, -20, -17]
    xf, yf = 0, 50
    speed = 20
    pure_pursuit(xb, yb, xf, yf, speed)


if __name__ == "__main__":
    main()
