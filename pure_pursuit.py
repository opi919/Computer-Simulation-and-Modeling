import numpy as np
import matplotlib.pyplot as plt


def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def simulate_pure_pursuit(v_fighter, v_bomber, duration):
    timesteps = np.arange(0, duration + 1, 1)

    # Initial positions of fighter and bomber
    xf, yf = np.random.randint(1, 1001), np.random.randint(1, 1001)
    xb, yb = np.random.randint(1, 1001), np.random.randint(1, 1001)

    fig, ax = plt.subplots()

    for t in timesteps:
        # Calculate distance between fighter and bomber
        distance = calculate_distance(xf, yf, xb, yb)

        # Plot current positions
        ax.plot([xf], [yf], marker="o", color="red", label="Fighter" if t == 0 else "")
        ax.plot([xb], [yb], marker="o", color="blue", label="Bomber" if t == 0 else "")

        ax.set_xlabel("X Coordinate")
        ax.set_ylabel("Y Coordinate")
        ax.set_title(f"Fighter and Bomber Paths at t={t}s")
        plt.pause(0.1)

        # Check if bomber is shot down or escaped
        if 100 < distance < 900:
            # Update positions based on pursuit logic
            angle = np.arctan2(yb - yf, xb - xf)
            xf += v_fighter * np.cos(angle)
            yf += v_fighter * np.sin(angle)

            xb += v_bomber * np.cos(np.random.uniform(0, 2 * np.pi))
            yb += v_bomber * np.sin(np.random.uniform(0, 2 * np.pi))
        elif distance <= 100:
            ax.text(
                xf,
                yf,
                f"Destroyed Bomber at {t} s",
                color="black",
                fontsize=10,
                ha="right",
                va="bottom",
            )
            break

    if distance > 900 or t == duration:
        ax.text(
            xf,
            yf,
            f"The bomber escaped from sight after {duration} seconds.",
            color="black",
            fontsize=10,
        )

    ax.legend()
    plt.show()


# Example usage
simulate_pure_pursuit(v_fighter=20, v_bomber=20, duration=50)
