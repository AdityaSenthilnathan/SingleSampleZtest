import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics
DataFrame = pd.read_csv("SingleSampleZtest.csv")
ls = DataFrame["reading_time"].tolist()
mean = statistics.mean(ls)

samplemeanList = []
for a in range(1, 100):
    sampleList = []

    for i in range(1,30):
        rnd = random.randint(1,6500)
        sampleList.append(ls[rnd])

    samplemean = statistics.mean(sampleList)
    samplemeanList.append(samplemean)

def plot_graph():
    newsamplemean = statistics.mean(samplemeanList)

    std_deviation = statistics.stdev(samplemeanList)

    first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
    second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)   
    third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
    
    fig = ff.create_distplot([samplemeanList], ["mean"])
    fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0,2.2], mode = "lines", name = "Standard Deviation 1"))
    fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,2.2], mode = "lines", name = "Standard Deviation 1"))
    fig.add_trace(go.Scatter(x = [ third_std_deviation_start, third_std_deviation_start], y = [0,2.2], mode = "lines", name = "Standard Deviation 1"))
    fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0,2.2], mode = "lines", name = "Standard Deviation 1"))
    fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,2.2], mode = "lines", name = "Standard Deviation 1"))
    fig.add_trace(go.Scatter(x = [ third_std_deviation_end, third_std_deviation_end], y = [0,2.2], mode = "lines", name = "Standard Deviation 1"))
    fig.add_trace(go.Scatter(x = [ newsamplemean, newsamplemean], y = [0,2.2], mode = "lines", name = "New Samplemean"))
    fig.add_trace(go.Scatter(x = [ mean, mean], y = [0,2.2], mode = "lines", name = " Samplemean"))

    fig.show()
    
    val = (newsamplemean - mean)/ std_deviation
    print(val)
plot_graph()