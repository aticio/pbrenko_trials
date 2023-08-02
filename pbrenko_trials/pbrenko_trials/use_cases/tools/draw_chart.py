import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import os


def draw_chart(bricks, percent, file_name):
    chart_path = os.getenv("CHART_PATH")
    min_val = bricks[0].close
    largest_brick_size = 0
    for b in bricks:
        brick_size = abs(b.close - b.open)
        if brick_size > largest_brick_size:
            largest_brick_size = brick_size

        if b.close < min_val:
            min_val = b.close

    brick_width = largest_brick_size / 2
    y_max = 0
    fig, ax = plt.subplots()

    count = 1
    for b in bricks:
        y = 0
        color = ""
        if b.type == "up":
            y = b.open
            color = "green"
        elif b.type == "down":
            y = b.close
            color = "red"
        else:
            color = "gray"
            y = b.close

        if y > y_max:
            y_max = y

        brick_size = (b.close * percent / 100)
        r = Rectangle((count * brick_width, y), brick_width, brick_size)
        r.set_color(color)

        ax.add_patch(r)
        count = count + 1

    ax.set_xlim(0, count * brick_width)
    ax.set_ylim(min_val - brick_width, y_max + (y_max * 0.02))
    ax.set_axisbelow(True)
    ax.get_xaxis().set_visible(False)

    ticks = np.arange(min_val - brick_width, y_max + (y_max * 0.02), brick_width * 2)
    plt.yticks(ticks)
    plt.grid(linestyle='--', color="#ccd8c0")
    file_name = file_name.replace(".", "-")
    plt.savefig(chart_path + "/" + file_name)
