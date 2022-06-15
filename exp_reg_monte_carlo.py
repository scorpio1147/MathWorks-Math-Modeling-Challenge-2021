import numpy as np
from sklearn.linear_model import LinearRegression

# Number of trials for the Monte-Carlo simulation
trials = 100000

# The mean bandwidth per month in the years 2015 to 2020, reverse chronological order; data for urban U.K. used
MbpsMeans = [97.44247228,
104.1279867,
90.35112135,
86.89859683,
53.61106073,
32.35380689]

# The standard deviation of bandwidth per month in the years 2015 to 2020, reverse chronological order; data for urban U.K. used
MbpsStdDev = [102.492798,
102.8019483,
95.61392489,
84.7818465,
45.03451962,
53.77606575
]

# Stores the randomly generated values for bandwidth per month, corresponding to the years 2020 to 2015, respectively
MbpsRandValues = [0, 0, 0, 0, 0, 0]

# Stores the natural log of the values in MbpsRandValues
Lny = [0, 0, 0, 0, 0, 0]

# Compounds the value returned for the base of the exponential regression in each trial
SumBase = 0
# Compounds the value returned for the coefficient of the exponential regression in each trial
SumCoef = 0

# Values of t corresponding to the years 2020 to 2015, respectively
years = [5,4,3,2,1,0]

# Loops Monte-Carlo simulation for number of selected trials
for j in range(0, trials):

  # Assigns randomly generated values according to the mean and standard deviation of each year
  for i in range(0,6):
    MbpsRandValues[i] = np.random.normal(MbpsMeans[i], MbpsStdDev[i])
    # The standard deviation allows for values of bandwidth that are less than 0; however, since the realistic minimum for bandwidth is 0.5 Mbps, all data below this value is replaced with 0.5 Mbps
    if (MbpsRandValues[i]<0.5):
      MbpsRandValues[i] = 0.5
    # We take the natural log of the randomly generated values, to transform the exponential regression model of coefficient 'a' and base 'b' to a linear regression model of intercept ln('a') and coefficient ln('b')
    Lny[i] = np.log(MbpsRandValues[i])
  
  # Defining lists to be used for the linear regression
  x = np.array(years).reshape((-1, 1))
  y = np.array(Lny)
  # Exponentiating the values of the intercept (ln('a')) and coefficient (ln('b')) returns the values of the coefficient of the exponential regression ('a') and the base ('b'), respectively
  SumBase += np.exp(LinearRegression().fit(x,y).coef_)
  SumCoef += np.exp(LinearRegression().fit(x,y).intercept_)

# Divides by the total number of trials to return the arithmetic mean
print(SumBase/trials)
print(SumCoef/trials)
