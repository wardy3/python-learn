from statistics import mean, stdev
from random import choices, shuffle
import sys

drug = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]
obs_diff = mean(drug) - mean(placebo)
comb = drug + placebo

nd = len(drug)

shuffle(comb)
print('comb last num drugs', comb[:nd])
shuffle(comb)
print('comb last num drugs', comb[:nd])

# If we reshuffle (permuting, relabeling) the participant
# Is the new mean diff the same or more extreme than we observed


def trial():
    shuffle(comb)
    drug = comb[:nd]
    placebo = comb[nd:]
    new_diff = mean(drug) - mean(placebo)
    return new_diff >= obs_diff


n = 10000
print(sum(trial() for i in range(n)) / n)
sys.exit()

print(f"Original:")
print('drug', mean(drug))
print(stdev(drug))
print('placebo', mean(placebo))
print(stdev(placebo))

# Build a 90% confidence interval


def bootstrap(data):
    return choices(data, k=len(data))


n = 10000
means = sorted(mean(bootstrap(drug)) for i in range(n))

print('bootstrapped mean', mean(means))
print('bootstrapped stdev', stdev(means))

print(
    f"Falls in a 90% confidence interval from "
    f"{means[500]:.1f} to {means[-500]:.1f}")

sys.exit(0)


print(f"samples:")

for i in range(10):
    sample = bootstrap(drug)
    print('mean', mean(sample))
    print('stdev', stdev(sample))
    print(sample)
    print()
