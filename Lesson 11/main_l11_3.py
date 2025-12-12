
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def bubble_sort_visualization(data):
    """
    Візуалізація сортування бульбашкою.

    :param data: Початкові дані для сортування та візуалізації.
    """
    n = len(data)

    fig, ax = plt.subplots()
    bars = ax.bar(range(n), data, align='edge')

    def update(frame):
        for i in range(n - frame - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

        for bar, h in zip(bars, data):
            bar.set_height(h)

    ani = animation.FuncAnimation(fig, update, frames=n - 1, repeat=False)
    plt.show()


# Приклад використання
initial_data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_visualization(initial_data)