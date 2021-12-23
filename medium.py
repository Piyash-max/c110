from datetime import date
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("population mean:- ",population_mean)
print("standard deviation:- ",std_deviation)
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_mean=random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("mean of sampling distribution",mean)
setup()

population_mean=statistics.mean(data)
print("poplutaion mean:- ",population_mean)

def std_dev():
    mean_list=[]
    for i in range(0,100):
        set_of_mean=random_set_of_mean(30)
        mean_list.append(set_of_mean)
    std_devi=statistics.stdev(mean_list)
    print("standard deviation of sampling distribution",std_devi)
std_dev()