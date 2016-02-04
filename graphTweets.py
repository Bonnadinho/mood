import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go

# this class has 2 parameters, these parameters are from the readTweets class

class graphTweets():    

    def __init__(self, x, y):        
        plotly.offline.plot({
        "data": [
            go.Scatter(
                x = x,
                y = y
                )
        ],
        "layout": Layout(
            title="Graphical display of Goerge Bush"
        )
        })
        
        # Draw scattered graph
        trace = go.Scatter(
            x = x,
            y = y,
            mode = 'markers'
        )

        data = [trace]       
        plotly.offline.plot(data, filename = 'basic-scatter.html')
