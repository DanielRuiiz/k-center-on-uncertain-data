# Plotly as Py and go to be able to create graph objs and plotting
import plotly.plotly as py 
import plotly.graph_objs as go
# Numpy for faster processes, and allowing 
# the random generation of starting and end points for the Data.
import numpy as np

# Base starting and end points from which we start at
start = 1
end = 7
# Array where we hold all the points and their informations
points = []
# arrLi, location
top_num = 20
# arrFi, probability
Fi = []
Li = []
Fi2 = []
Li2 = []
Fi3 = []
Li3 = []
data = []
# Create 3 Pi's
for i in range(0, 3):
    # This is for the moment to just have some points around eachother
    start += 3
    end +=start
    arrLi = np.random.choice(top_num, 5, replace=False)
    #arrLi = np.random.choice(range(start,end), 5, replace=False)
    # sort the array of locations
    np.sort(arrLi)
    arrLi.sort()
    #print(arrLi)
    # add probabilities, that add up to 1, rounded to 8 decimal places
    arrFi = np.around(np.random.dirichlet(np.ones(5), size=1),decimals=2)
    if i == 0:
        for j in range(0, 5):
            Fi.append(arrFi[0][j])
            Li.append(arrLi[j])
        Pi = [Li, Fi]
        points.append(Pi)
    elif i == 1:
        for j in range(0, 5):
            Fi2.append(arrFi[0][j])
            Li2.append(arrLi[j])
        Pi = [Li2, Fi2]
        points.append(Pi)
    else:
        for j in range(0, 5):
            Fi3.append(arrFi[0][j])
            Li3.append(arrLi[j])
        Pi = [Li3, Fi3]
        points.append(Pi)

    # add Pi to the points array
    
    print(points)

print(points)
print('\n')
'''
# Just to print out the points
for i in range(0, len(points)):
    # go through the length of each of the points
    for j in range(0, len(points[0][0])):
        # This selects the Li for the current Pi at j
        print(points[i][0][j])
        # This selects the Fi for the current Pi at j
        # Rather than scanning arrFi and copying into a different array
        # We dont so that, while it looks more complicated, its faster
        print(points[i][1][0][j])
'''

# C to store all the C's for each Pi
c = []
# D to store all the D's for each Pi
d = []
# Store all the intervals per point for use in Ed()
Ed = []
# Calculate all the points 
for i in range(0, len(points)):
    # temporary variable to store the values in
    temp = 0
    # add an array to the inside of c
    c.append([])
    # Calculate Ci0
    for xi in range(0, len(points[0][0])):
        temp+= points[i][1][xi]
    #print(temp)
    # store it in C
    c[i].append(round(temp, 8))
    #print(c)
    # reset the temp
    temp = 0
    # add an array to the inside of d
    d.append([])
    # Calculate Di0
    for fi in range(0, len(points[0][0])):
        temp += points[i][0][fi] * points[i][1][fi]
    # Store it in D
    d[i].append(round(temp, 8))
    #print(d)
    # Add an array inside the Ed()'s array
    Ed.append([])
    # Add the ci1 + di1, this took O(m)
    Ed[i].append(c[i][0] + d[i][0])
    # Calculate the remaining C's and D's, O(1)*m
    for ite in range(1, len(points[0][0])):
        c[i].append(round(c[i][ite-1] + (2* points[i][1][ite-1]), 8))
        d[i].append(round(d[i][ite-1] - (2* points[i][1][ite-1] * points[i][0][ite-1]), 8))
        # Add both sides of the interval to the total
        if not(ite >= len(points[0][0])):
            Ed[i].append(round(d[i][ite] + c[i][ite] * points[i][0][ite-1], 8))
            Ed[i].append(round(d[i][ite] + c[i][ite] * points[i][0][ite],8))
        if ite == len(points[0][0]):
            Ed[i].append(round(d[i][ite-1] + c[i][ite-1] * points[i][0][ite-1], 8))

    # At this point we should have all the functions with values for each of Pi
    # print them to see if they add up
    print(c[i])
    print(d[i])
    print()
    #print(Ed[i])
    #print()
# Print all the expected distances
'''
print('\n')
print(len(points))
Remove continous duplicates from the Ed()
from 
-16.38449536048509, -16.38449536048509, 
-60.357085034074885, -60.357085034074885,
 -103.3844850040478, -103.38448500404779, 
-124.51186418341577, -124.51186418341578, 
-145.61550463951494
go through all 
'''
# Super bad implementation :/ its 5am please forgive me
cleanEd = []
cleanEd.append([])
cleanEd.append([])
cleanEd.append([])
# It removes duplicates from the list of arrays
for i in range(0, len(Ed)):
    for j in range(0, len(Ed[0])):
        if Ed[i][j] not in cleanEd[i] and (round(Ed[i][j]) is not round(Ed[i][j]+1)) and (round(Ed[i][j]) is not round(Ed[i][j]-1)):
            cleanEd[i].append(Ed[i][j])

bleh = [top_num + 1]
m = np.array([])
for i in range(0, len(cleanEd)):
    print(cleanEd[i])
    print()
    print()    
    points[i][0] = np.append(points[i][0], bleh)
    #points[i][0] = np.insert(points[i][0], 0, -5)

#print(points)
# Should now have the 6 piece segments :D

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
        dtick=1,
        ticklen=8,
        tickwidth=4,
        tickcolor='#000'
    ),
    yaxis=dict(
        tickmode='linear',
        ticks='outside',
        tick0=0,
        dtick=1,
        ticklen=8,
        tickwidth=4,
        tickcolor='#000'
    )
)
figure = go.Figure(data=data, layout=layout)
py.plot(figure, filename='Try1')
