import plotly.graph_objects as go
from plotly.subplots import make_subplots
fig = make_subplots(rows=2, cols=6)
# scores = [[0,15,15,30,40],[0,0,15,15,15],[0,0,0,15,15],[0,15,30,30,40]]
fig.add_trace(go.Line(y=[0,0,15,30,30,30,A,40,40,A],line_color = "crimson"),row=1,col=1)
fig.add_trace(go.Line(y=[0,15,30,30,30,40,40],line_color = "gray"),row=1,col=1)
fig.add_trace(go.Line(y=[0,0,0,15,15],line_color = "crimson"),row=1,col=2)
fig.add_trace(go.Line(y=[0,15,30,30,40],line_color = "gray"),row=1,col=2)
fig.add_trace(go.Line(y=[0,0,0,15,30,30,40,40],line_color = "crimson"),row=1,col=3)
fig.add_trace(go.Line(y=[0,15,30,30,30,40,40],line_color = "gray"),row=1,col=3)
# fig.add_trace(go.Line(y=[0,0,15,30,30,30,40,40,40,40],line_color = "crimson"),row=1,col=4)
# fig.add_trace(go.Line(y=[0,15,15,15,30,40,40,40,40,40],line_color = "gray"),row=1,col=4)
# fig.add_trace(go.Line(y=[0,0,0,15,30,30,40,40],line_color = "crimson"),row=1,col=5)
# fig.add_trace(go.Line(y=[0,15,30,30,30,40,40],line_color = "gray"),row=1,col=5)
# fig.add_trace(go.Line(y=[0,0,15,30,30,30,40,40,40,40],line_color = "crimson"),row=1,col=6)
# fig.add_trace(go.Line(y=[0,15,15,15,30,40,40,40,40,40],line_color = "gray"),row=1,col=6)
# fig.add_trace(go.Line(y=[0,1,2,2,3,4,5,6],line_color = "crimson"),row=2,col=1)
# fig.add_trace(go.Line(y=[0,0,0,1,1,1,1,1],line_color = "gray"),row=2,col=1)
fig.update_layout(height=600, width=1800, title_text="Tennis Scores")
# fig.show()
# j = 1
# def add_traces(i):
#     return fig.add_trace(go.Line(y= i),row=1,col=j)

# for i in scores:
#     add_traces(i)
#     j=j+1

# i=1
# fig.add_trace(go.Line(y = scores[0]),row=1,col=i)
# i = i+1
# fig.add_trace(go.Line(y = scores[1]),row=1,col=i)
# i = i+1
# fig.add_trace(go.Line(y = scores[2]),row=1,col=i)
# i = i+1
# fig.add_trace(go.Line(y = scores[3]),row=1,col=i)
# i = i+1
fig.show()

