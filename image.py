import plotly.graph_objects as go
import json

with open("data.json") as f:
    data = json.load(f)
    number_of_bees = data["traces"]["number_of_bees"]
    x = [tick[0] for tick in number_of_bees]
    y = [tick[1] for tick in number_of_bees]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x, y=y,
            mode='lines',
            name='number_of_bees',
            line=dict(color='rgb(255,255,0)')
        )
    )
    
    number_of_flowers = data["traces"]["number_of_flowers"]
    x = [tick[0] for tick in number_of_flowers]
    y = [tick[1] for tick in number_of_flowers]
    fig.add_trace(
        go.Scatter(
            x=x, y=y,
            mode='lines',
            name='number_of_flowers',
            line=dict(color="rgb(10, 251, 0)")
        )
    )

fig.show()
