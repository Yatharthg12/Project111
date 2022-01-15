import csv
import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff 
import statistics
import random
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df["title"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

#random set of 30 samples data
def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)
    
mean_list = []
for i in range(0,100):
    setofmean = randomsetofmean(30)
    mean_list.append(setofmean)

mean = statistics.mean(mean_list)
std = statistics.stdev(mean_list)
print(mean, std)

fstds,fstde = mean-std, mean+std 
sstds,sstde = mean-(2*std),mean+(2*std)
tstds,tstde = mean-(3*std),mean+(3*std)
print("std1", fstds,fstde)
print("std2", sstds,sstde)
print("std3", tstds,tstde)

#plotting graph with trace
fig = ff.create_displot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [fstds,fstds], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [fstde,fstde], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [sstds,sstds], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [sstde,sstde], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [tstds,tstds], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [tstde,tstde], y = [0,0.17], mode = "lines", name = "mean"))
fig.show()

#def show_fig(mean_list):
    #df = mean_list
    #fig = ff.create([df], ["temp"], show_hist = False)
    #fig.show()