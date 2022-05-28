import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics as st 
import pandas as pd 
import csv
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time']

mean = st.mean(data)
std = st.stdev(data)

print('mean of population -->', mean)
print('Standard deviation of populaton -->', std)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean


mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)


std1 = st.stdev(mean_list)
mean1 = st.mean(mean_list)

print('mean of sampling distribution -->', mean)
print('Srandard deviation of sampling distribution --? ', std1) 

fig = ff.create_distplot([mean_list], ['reading time'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y =[ 0, 0.20], mode = 'lines', name = 'MEAN'))



stdev1Start = mean1 - std1
stdev1End = mean1 + std1

stdev2Start = mean1 - std1 * 2
stdev2End = mean1 + std * 2

stdev3Start = mean1 - std * 3
stdev3End = mean1 + std * 3


fig.add_trace(go.Scatter(x = [stdev1Start, stdev1Start], y = [0,2], mode = 'lines', name  = '1st start'))
fig.add_trace(go.Scatter(x = [stdev1End, stdev1End], y = [0,2], mode = 'lines', name  = '1st end'))

fig.add_trace(go.Scatter(x = [stdev2Start, stdev2Start], y = [0,2], mode = 'lines', name  = '2st start'))
fig.add_trace(go.Scatter(x = [stdev2End, stdev2End], y = [0,2], mode = 'lines', name  = '2st end'))

fig.add_trace(go.Scatter(x = [stdev3Start, stdev3Start], y = [0,2], mode = 'lines', name  = '3st start'))
fig.add_trace(go.Scatter(x = [stdev3End, stdev3End], y = [0,2], mode = 'lines', name  = '3st end'))

fig.show()