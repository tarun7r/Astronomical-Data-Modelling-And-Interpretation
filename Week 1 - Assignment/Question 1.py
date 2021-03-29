from matplotlib import pyplot as plot
import random as rn
import numpy as np

print("Enter the number of experiments you want to perform :")

n = int(input())

outcome_1=[]
outcome_2=[]

for i in range(0,n):
    outcome_1.append(rn.randint(1,6))
    outcome_2.append(rn.randint(1,6))
    
die1=np.array(outcome_1)
die2=np.array(outcome_2)

output=die1+die2

plot.style.use('ggplot')
plot.hist(output)
plot.show()