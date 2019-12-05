from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = go.Figure()

fig = make_subplots(rows=2, cols=3)

fig.add_trace(
    go.Line(
        x=[1,2,3,4,5,6,7,8,9,10],
        y=[0, 15, 30, 30, 40, 40,40,40,40,50],
        text=["0-0", "15-0", "30-0","30-15","40-15[BP]","40-30[BP]","40-40","40-A","40-40","A-40[BP]"],
        textposition="bottom center",
        line_color='grey'
        
    ),
    row=1, col=1
)


fig.add_trace(
    go.Line(
        x=[1,2,3,4,5,6,7,8,9,10],
        y=[0, 0, 0, 15, 15, 30, 40, 50, 40, 40],
        text=["0-0", "15-0", "30-0","30-15","40-15[BP]","40-30[BP]","40-40","40-A","40-40","A-40[BP]"],
        textposition="bottom center",
        line_color = "crimson"
    ),
    row=1, col=1
)

fig.update_xaxes(title_text="Serve1", row=1, col=1)
fig.update_yaxes(title_text="Set1", row=1, col=1)


fig.add_trace(
    go.Line(
        x=[1,2,3,4,5,6,7,8,9,10],
        y=[0, 15, 30, 30, 40, 40,40,40,40,50],
        text=["0-0", "15-0", "30-0","30-15","40-15[BP]","40-30[BP]","40-40","40-A","40-40","A-40[BP]"],
        textposition="bottom center",
        line_color='grey'
        
    ),
    row=1, col=2
)


fig.add_trace(
    go.Line(
        x=[1,2,3,4,5,6,7,8,9,10],
        y=[0, 0, 0, 15, 15, 30, 40, 50, 40, 40],
        text=["0-0", "15-0", "30-0","30-15","40-15[BP]","40-30[BP]","40-40","40-A","40-40","A-40[BP]"],
        textposition="bottom center",
        line_color = "crimson"
    ),
    row=1, col=2
)

fig.update_xaxes(title_text="Serve2", row=1, col=2)

fig.add_trace(
    go.Line(
        x=[1,2,3,4,5,6,7,8,9,10],
        y=[0, 15, 30, 30, 40, 40,40,40,40,50],
        text=["0-0", "15-0", "30-0","30-15","40-15[BP]","40-30[BP]","40-40","40-A","40-40","A-40[BP]"],
        textposition="bottom center",
        line_color='grey'
        
    ),
    row=2, col=1
)


fig.add_trace(
    go.Line(
        x=[1,2,3,4,5,6,7,8,9,10],
        y=[0, 0, 0, 15, 15, 30, 40, 50, 40, 40],
        text=["0-0", "15-0", "30-0","30-15","40-15[BP]","40-30[BP]","40-40","40-A","40-40","A-40[BP]"],
        textposition="bottom center",
        line_color = "crimson"
    ),
    row=2, col=1
)
fig.update_xaxes(title_text="Serve1", row=2, col=1)
fig.update_yaxes(title_text="Set2", row=2, col=1)

fig.add_trace(
    go.Line(
        x=[1,2,3,4,5,6,7,8,9,10],
        y=[0, 15, 30, 30, 40, 40,40,40,40,50],
        text=["0-0", "15-0", "30-0","30-15","40-15[BP]","40-30[BP]","40-40","40-A","40-40","A-40[BP]"],
        textposition="bottom center",
        line_color='grey'
        
    ),
    row=2, col=2
)


fig.add_trace(
    go.Line(
        x=[1,2,3,4,5,6,7,8,9,10],
        y=[0, 0, 0, 15, 15, 30, 40, 50, 40, 40],
        text=["0-0", "15-0", "30-0","30-15","40-15[BP]","40-30[BP]","40-40","40-A","40-40","A-40[BP]"],
        textposition="bottom center",
        line_color = "crimson"
    ),
    row=2, col=2
)
fig.update_xaxes(title_text="Serve2", row=2, col=2)

fig.update_layout(height=600, width=800, title_text="Annotations and subplots")

fig.show()