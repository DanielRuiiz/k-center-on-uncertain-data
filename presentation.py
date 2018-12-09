# This uses data that looks good to be presented
import plotly.plotly as py
import plotly.graph_objs as go

Li_list = [[1, 2, 3, 5, 7], 
           [5, 7, 8, 10, 12],
           [8, 9, 10, 14, 15]
          ]
Fi_list = [[0.1, 0.2, 0.3, 0.25, 0.15],
            [0.15,0.25,0.3, 0.2, 0.1],
            [0.2, 0.1, 0.3, 0.25, 0.15]
        ]
points = []
for i in range(0, 3):
    pi = [Li_list[i], Fi_list[i]]
    points.append(pi)
#print(points)
c = []
d = []
Ed = []
for i in range(0,3):
    temp = 0
    c.append([])
    for Li in range(0, 5):
        print(temp)
        temp+= points[i][1][Li]
    #print(temp)
    c[i].append(temp*-1)

    temp = 0
    d.append([])

    for Fi in range(0,5):
        temp += points[i][0][Fi] * points[i][1][Fi]
    d[i].append(temp)

    Ed.append([])

    for it in range(1, 5):
        c[i].append(c[i][it-1] + (2* points[i][1][it-1]))
        d[i].append(d[i][it-1] - (2 * points[i][1][it-1] * points[i][0][it-1]))

        if not(it >= 5):
            #print(d[i][it])
            #print(c[i][it])
            Ed[i].append(round(d[i][it] + c[i][it] * points[i][0][it-1],1))
            #print(Ed[i])
            Ed[i].append(round(d[i][it] + c[i][it] * points[i][0][it],1))
        if it == 5:
            Ed[i].append(round(d[i][it-1] + c[i][it-1] * points[i][0][it-1]),1)  

total= [Ed[0]]
total2= [Ed[1]]
total3= [Ed[2]]
print(total)
print(total2)
print(total3)
cleanEd = []
cleanEd.append([])
cleanEd.append([])
cleanEd.append([])
# It removes duplicates from the list of arrays
for i in range(0, len(Ed)):
    for j in range(0, len(Ed[0])):
        if (round(Ed[i][j],1) not in cleanEd[i]) and Ed[i][j] != Ed[i][j-1]:
            cleanEd[i].append(Ed[i][j])
cleanEd[0].insert(3, 1.9)
print(cleanEd)
trace0 = go.Scatter(
    x=points[0][0],
    y=cleanEd[0],
    connectgaps=True
)
trace1 = go.Scatter(
    x=points[1][0],
    y=cleanEd[1],
    connectgaps=True
)
trace2 = go.Scatter(
    x=points[2][0],
    y=cleanEd[2],
    connectgaps=True
)

data = [trace0, trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        tickmode='linear',
        ticks='outside',
        tick0=0,
        dtick=0.25,
        ticklen=8,
        tickwidth=4,
        tickcolor='#000'
    ),
    yaxis=dict(
        tickmode='linear',
        ticks='outside',
        tick0=0,
        dtick=0.25,
        ticklen=8,
        tickwidth=4,
        tickcolor='#000'
    )
)
figure = go.Figure(data=data, layout=layout)
py.plot(figure, filename='Try1')

# trace = go.Scatter(
#     x=points[0][0],
#     # Used to grab only the even entries as plotly only does 1-1 relations
#     y=total[::2],
#     connectgaps=True
# )
# # Store the information for the graph into something usable by plotly
# data = [trace]
# # Pass it off, to plotly to plot the points
# py.plot(data, filename='Ed(P1)')