import plotly.figure_factory as ff
import plotly.graph_objects as go
import random 
import statistics
import pandas as pd

df  = pd.read_csv("StudentsPerformance.csv")

data = df["math score"].to_list()

mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
Sd = statistics.stdev(data)

print('mean is' ,mean)
print('mode is' ,mode)
print('median is' ,median)
print('std' ,Sd)

firstsdstart,firstsdend = mean - Sd,mean + Sd
secondsdstart,secondsdend = mean - (2*Sd),mean + (2*Sd)
thirdsdstart,thirdsdend = mean - (3*Sd),mean + (3*Sd)


list_of_data_within_1_std_deviation = [result for result in data if result > firstsdstart and result < firstsdend]
list_of_data_within_2_std_deviation = [result for result in data if result > secondsdstart and result < secondsdend]
list_of_data_within_3_std_deviation = [result for result in data if result > thirdsdstart and result < thirdsdend]


print(" percentage of data lies within one standard deviation",format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))

print(" percentage of data lies within second standard deviation",format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))

print(" percentage of data lies within second standard deviation",format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))





fig = ff.create_distplot([df["math score"].tolist()],["reading score"],["writing score"],show_hist=False)

fig.show()

