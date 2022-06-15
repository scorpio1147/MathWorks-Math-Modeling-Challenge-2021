#this simulation uses the monte_carlo() function from the bandwidh_monte_carlo.py file.

import numpy
from random import uniform

hours = [22.33, 36.35, 50.83, 51.90, 44.02, 34.12]
ratios = [[0, 0.839, 0.161],
          [0.501, 0.364, 0.135],
          [0.622, 0.294, 0.084],
          [0.715, 0.248, 0.037],
          [0.783, 0.205, 0.012],
          [0.826, 0.169, 0.005]]

# Distribution for each age group
region1 = [0.115, 0.141, 0.239, 0.206, 0.114, 0.185]
region2 = [0.1024, 0.1273, 0.1452, 0.2292, 0.1488, 0.2471]
region3 = [0.0852, 0.0861, 0.3339, 0.2713, 0.1032, 0.1203]

SIMULATIONS = 10000

def age_monte_carlo(region, SIMULATIONS):
    total = 0
    for i in range(SIMULATIONS):
        household = []
        for j in range(3):
            age = numpy.random.choice(numpy.arange(0, 6), p=region)
            time = hours[age]

            H_c, H_w = 0, 0
            if age == 1:
                H_c = uniform(0, 20)
                H_w = 20 - H_c
            if age in [2, 3, 4]:
                H_c = uniform(0, 40)
                H_w = 40 - H_c

            free = time - H_c - H_w
            H_s = free * ratios[age][0]
            H_v = free * ratios[age][1]
            H_g = free * ratios[age][2]

            household.append([H_c, H_w, H_s, H_v, H_g])

        total += monte_carlo(household, SIMULATIONS, [100])[0]

    print(total / SIMULATIONS)

print("Region 1:")
age_monte_carlo(region1, SIMULATIONS)

print("\nRegion 2:")
age_monte_carlo(region2, SIMULATIONS)

print("\nRegion 3:")
age_monte_carlo(region3, SIMULATIONS)
