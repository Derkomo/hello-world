# !pip install pandas
# !pip install numpy
# !pip install matplotlib
# !pip install math
# !pip install scipy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from math import sqrt

print("hello")

ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
#Reading from the csv
ratings_df = pd.read_csv(ratings_url)

from scipy.stats import norm

# Plot between -4 and 4 with 0.1 steps.
x_axis = np.arange(-4, 4, 0.1)
# Mean = 0, SD = 1.
plt.plot(x_axis, norm.pdf(x_axis, 0, 0.1))
#plt.show()

eval_mean = round(ratings_df['eval'].mean(), 3)
eval_sd = round(ratings_df['eval'].std(), 3)
print("Moyenne des evaluations :", eval_mean ,"\nEcrat type des evaluations :" , eval_sd)

#Proba que l'evaluation soit plus petite que 4.5
prob0 = scipy.stats.norm.cdf((4.5 - eval_mean)/eval_sd)
#Proba que l'evaluation soit plus grande que 4.5 (c'est 1-Proba plus petite)
print("Proba que l'evaluation soit plus grande que 4.5:" , 1 - prob0)

#plus petite que 3.5
x1 = 3.5
prob1 = scipy.stats.norm.cdf((x1 - eval_mean)/eval_sd)
print(prob1)

#plus petite que 4.2
x2 = 4.2
prob2 = scipy.stats.norm.cdf((x2 - eval_mean)/eval_sd)
print(prob2)
#entre 4.2 et 3.5 pusique plus petit que 4.2 moins tout ce qui est plus petit que 3.5
print ("proba que l'evaluation soit entre 4.2 et 3.5:", round((prob2 - prob1)*100, 1))

#A professional basketball team wants to compare its performance with that of players in a regional league.
#The pros are known to have a historic mean of 12 points per game with a standard deviation of 5.5.
#A group of 36 regional players recorded on average 10.7 points per game.
#The pro coach would like to know whether his professional team scores on average are different from that of the regional players.

## because it is a two-tailed test we multiply by 2
xx=2*round(scipy.stats.norm.cdf((10.7 - 12)/(5.5/sqrt(36))), 3)
print(xx)

SleepingPP=np.array([116, 111, 101, 120, 99, 94, 106, 115, 107, 101, 110, 92])
SleepingPP_mean=np.mean(SleepingPP)
SleepingPP_std=np.std(SleepingPP)

Prob_inff100 = scipy.stats.norm.cdf((SleepingPP_mean - 100)/(SleepingPP_std/sqrt(12)))
Prob_supp100=1-Prob_inff100
print(Prob_supp100)

iq_mean = np.mean([116, 111, 101, 120, 99, 94, 106, 115, 107, 101, 110, 92])
iq_std = np.std([116, 111, 101, 120, 99, 94, 106, 115, 107, 101, 110, 92])
print(round(1-scipy.stats.norm.cdf((iq_mean - 100)/(iq_std/sqrt(12))), 3))