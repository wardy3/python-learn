from random import sample
from matplotlib import pyplot, ticker

num_total = 80
population = range(1, num_total + 1)
num_drawn = 20

# prize{selected}{matched} = $prize
prize = {
    1: {0: 0, 1: 3},
    2: {0: 0, 1: 0, 2: 12},
    3: {0: 0, 1: 0, 2: 1, 3: 44},
    4: {0: 0, 1: 0, 2: 1, 3: 4, 4: 120},
    5: {0: 0, 1: 0, 2: 0, 3: 2, 4: 14, 5: 640},

    6: {0: 0, 3: 1, 4: 5, 5: 80, 6: 1_800},
    7: {0: 0, 3: 1, 4: 3, 5: 12, 6: 125, 7: 5_000},
    8: {0: 0, 3: 0, 4: 2, 5: 7, 6: 60, 7: 675, 8: 25_000},
    9: {0: 0, 3: 0, 4: 1, 5: 5, 6: 20, 7: 210, 8: 2_500, 9: 100_000},
    10: {0: 0, 3: 0, 4: 1, 5: 2, 6: 6, 7: 50, 8: 580, 9: 10_000, 10: 250_000},

    15: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 2, 7: 4, 8: 20, 9: 50, 10: 250,
         11: 2_000, 12: 12_000, 13: 50_000, 14: 100_000, 15: 250_000},
    20: {0: 100, 1: 10, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 2, 9: 7, 10: 20,
         11: 100, 12: 450, 13: 1_200, 14: 5_000, 15: 10_000, 16: 15_000,
         17: 25_000, 18: 50_000, 19: 100_000, 20: 250_000},
    40: {0: 250_000, 1: 25_000, 2: 2_200, 3: 200, 4: 35, 5: 7, 6: 2, 7: 1,
         8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 1, 14: 2, 15: 7, 16: 35, 17: 200,
         18: 2_200, 19: 25_000, 20: 250_000}
}

jackpots = {
    7: 7_000,
    8: 38_000,
    9: 180_000,
    10: 750_000,
}


def prize_playing(num_selected):
    selected = sorted(sample(population, num_selected))
    drawn = sorted(sample(population, num_drawn))

    num_matched = 0
    for number in selected:
        if number in drawn:
            num_matched += 1

    win = prize[num_selected].get(num_matched, 0)

    return win


# Number of games per selected
n = 100_000  # _000

plot_x = []
plot_y = []

# For each type of game
for num_chosen in prize.keys():
    x_label = ''
    if num_chosen in jackpots:
        jackpot = jackpots[num_chosen] / 1000
        x_label += f"${jackpot:,.0f}k ??  "
    x_label += str(num_chosen)
    plot_x.append(x_label)

    average_win = sum(prize_playing(num_chosen) for i in range(n)) / n
    plot_y.append(average_win)

    print(f"Average win for picking {num_chosen:2d} numbers is "
          f"${average_win:4.2f}")


# Graph it
def plot_it(plot_x, plot_y):
    pyplot.bar(plot_x, plot_y)
    pyplot.xticks(rotation=90)
    y_tick = ticker.StrMethodFormatter(
        '${x:,.02f}')  # Format y axis as currency
    pyplot.gca().yaxis.set_major_formatter(y_tick)
    pyplot.xlabel('numbers chosen')
    pyplot.ylabel('average return for $1 bet')
    pyplot.title('Estimated Keno returns')
    pyplot.margins(0.2)
    pyplot.subplots_adjust(bottom=0.25)
    pyplot.show()


plot_it(plot_x, plot_y)
