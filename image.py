import plotly.graph_objects as go
import json

with open("../../data.json") as f:
    data = json.load(f)
    number_of_bees = data["traces"]["number_of_bees"]
    bx = [tick[0] for tick in number_of_bees]
    by = [tick[1] for tick in number_of_bees]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=bx, y=by,
            mode='lines',
            name='Bees',
            line=dict(color='rgb(255,255,0)')
        )
    )
    
    number_of_flowers = data["traces"]["number_of_flowers"]
    fx = [tick[0] for tick in number_of_flowers]
    fy = [tick[1] for tick in number_of_flowers]
    max_y = max(by) if max(by) > max(fy) else max(fy)
    fig.add_trace(
        go.Scatter(
            x=fx, y=fy,
            mode='lines',
            name='Flowers',
            line=dict(color="rgb(10, 251, 0)")
        )
    )
    fig.update_layout(
        title=dict(
            text="Plot Title"
        ),
        xaxis=dict(
            title=dict(
                text="Time"
            )
        ),
        yaxis=dict(
            title=dict(
                text="Number of:"
            )
        ),
        yaxis_range=[0,max_y]
    )

fig.show()
