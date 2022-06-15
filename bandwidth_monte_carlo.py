from random import random

def monte_carlo(people, SIMULATIONS, coverage):
    # Most time spent online
    total = max([sum(i) for i in people])

    # Mpbs of each activity (b_c, b_w, b_s, b_v, b_g)
    MBPS = [3, 1, 1, 5, 2, 0]

    values = []

    # Adds a column for no Internet usage
    for person in people:
        person.append(total - sum(person))

    # Monte Carlo simulation for bandwidth used at any point in time
    for i in range(SIMULATIONS):
        value = 0
        
        for person in people:
            # Cumulative probability
            cumulative = []
            for p in person:
                previous = 0 if len(cumulative) == 0 else cumulative[-1]
                cumulative.append(p/total + previous)

            # Randomly choses an activity based on proportion of time spent
            chance = random()
            index = 0
            while chance > cumulative[index]:
                index += 1

            # Adds the bandwidth used to the total
            value += MBPS[index]

        # Bandwidth used in that point of time
        values.append(value)

    # Count of how many times each bandwidth occurs
    counts = {}
    for i in values:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1

    # Count of how many times the bandwidth is less than or equal to each bandwidth value
    cumulative = []
    keys = sorted(counts)
    for key in keys:
        previous = 0 if len(cumulative) == 0 else cumulative[-1]
        cumulative.append(counts[key] + previous)

    # Calculates when the bandwidth is covered 90% and 99% of the time
    mbps = []
    for i in coverage:
        index = 0
        while cumulative[index] < SIMULATIONS * i/100:
            index += 1

        # Multiply by 100/65 because the bandwidth will be approximately 35% slower due to interferences
        mbps.append(round(keys[index] * (100/65), 1))

    return mbps

SIMULATIONS = 1000000

household1 = [[0, 11, 24.77, 11.7, 3.35],
              [12.5, 27.5, 6.74, 3.18, 0.91],
              [0, 0, 0, 18.73, 3.60]]

household2 = [[0, 0, 28.18, 5.77, 0.17],
              [5, 1.5, 1.95, 1.41, 0.52],
              [5, 1.5, 1.95, 1.41, 0.52]]

household3 = [[20, 25, 3.63, 1.71, 0.49],
              [20, 25, 3.63, 1.71, 0.49],
              [20, 25, 3.63, 1.71, 0.49]]

coverage = [90, 99]

print("Household 1:")
mbps = monte_carlo(household1, SIMULATIONS, coverage)
for i in range(2):
    print(str(coverage[i]) + "% coverage: ", mbps[i], "Mbps")

print("\nHousehold 2:")
mbps = monte_carlo(household2, SIMULATIONS, coverage)
for i in range(2):
    print(str(coverage[i]) + "% coverage: ", mbps[i], "Mbps")
    
print("\nHousehold 3:")
mbps = monte_carlo(household3, SIMULATIONS, coverage)
for i in range(2):
    print(str(coverage[i]) + "% coverage: ", mbps[i], "Mbps")
