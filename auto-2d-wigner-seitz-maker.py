import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations, product
from collections import defaultdict
from matplotlib.widgets import Slider


#axis stuff
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

ax.set_aspect('equal')

ax.axhline(y=0,color='k',linewidth=0.5)
ax.axvline(x=0,color='k',linewidth=0.5)

a1 = float(input("basis vector a1: "))
a2 = float(input("basis vector a2: "))
b = float(input("angle between a1 and a2: "))

#lattice-point-generator-f(x)
#uses product to generate all combinations of the gencoords and makes the lattice points (pt)
gencoords = [0,1,2]
pt = []

for (n,m) in product(gencoords,repeat=2):
    x = n*a1 + m*a2*np.cos(np.radians(b))
    y = m*a2*np.sin(np.radians(b))
    pt.append((x,y))
#diag print(pt)
pt_matrix = np.array(pt)
ax.scatter(pt_matrix[:,0], pt_matrix[:,1], color='b')
origin = pt[4] #defines origin as (1a1,1a2)

#lookup-table 
#one of the inputs for c(x)
lp_coords = {
    'f(X)1': np.array(pt[2]),
    'f(X)2': np.array(pt[6]),
    'g(X)1': np.array(pt[7]),
    'g(X)2': np.array(pt[1]),
    'h(X)1': np.array(pt[0]),
    'h(X)2': np.array(pt[8]),
    'xV1': np.array(pt[3]),
    'xV2': np.array(pt[5])
    }

#eqs
fX = ((a1-a2*np.cos(np.radians(b)))/(a2*np.sin(np.radians(b)))) #grad(x+-1,y-+1)
gX = 1/(-np.tan(np.radians(b))) #grad(x,y+-1)
hX = (a1+a2*np.cos(np.radians(b)))/(a2*np.sin(np.radians(b))) #grad(x-+1,y-+1)

fXc1 = ((0.5*(a2**2) - 1.5*(a1**2)+a1*a2*np.cos(np.radians(b)))/(a2*np.sin(np.radians(b))))
fXc2 = ((1.5*(a2**2)-0.5*(a1**2)-a1*a2*np.cos(np.radians(b)))/(a2*np.sin(np.radians(b))))
gXc1 = ((1.5*a2+a1*np.cos(np.radians(b)))/np.sin(np.radians(b)))
gXc2 = ((0.5*a2+a1*np.cos(np.radians(b)))/np.sin(np.radians(b)))
hXc1 = ((0.5*(a2**2)+0.5*(a1**2)+ a1*a2*np.cos(np.radians(b)))/(a2*np.sin(np.radians(b))))
hXc2 = (((1.5*(a2**2))+1.5*(a1**2)+3*a1*a2*np.cos(np.radians(b)))/(a2*np.sin(np.radians(b))))
xv1 = 0.5*a1 + a2*np.cos(np.radians(b))
xv2 = 1.5*a1 + a2*np.cos(np.radians(b))

#linalg stuff
#generate all the pairs to feed into c(x)
pairs = [
    {"name": "f(X)1", "a": fX, "K": -1, "c": -fXc1},
    {"name": "f(X)2", "a": fX, "K": -1, "c": -fXc2},
    {"name": "g(X)1", "a": gX, "K": -1, "c": -gXc1},
    {"name": "g(X)2", "a": gX, "K": -1, "c": -gXc2},
    {"name": "h(X)1", "a": -hX, "K": -1, "c": -hXc1},
    {"name": "h(X)2", "a": -hX, "K": -1, "c": -hXc2},
    {"name": "xV1", "a": 1, "K": 0, "c": xv1},
    {"name": "xV2", "a": 1, "K": 0, "c": xv2}
    ]
intersections = defaultdict(list)

for li, lj in combinations(pairs,2):
    A =  np.array([[li["a"],li["K"]],
                    [lj["a"],lj["K"]]])
    d = np.array([li["c"],lj["c"]])
    try:
        x, y = np.linalg.solve(A, d)
    except np.linalg.LinAlgError:
        continue #noparallel

    intersections[li["name"]].append(((x,y),lj["name"]))
    intersections[lj["name"]].append(((x,y),li["name"]))
ints_list = [{'line': k, 'points': v} for k,v in intersections.items()]


#comparator-func-c(x)
#basically defines a valid point by comparing distances to the vertex AND ensures only the closest intersections are plotted
origin_array = np.array([origin])
dist_list = []
cXout = [] #output of c(x)
corr_param = 1e-6 #i literally dont know why THIS SPECIFIC VALUE works
for j in ints_list:
    for (x,y),name in j["points"]:
        dist_ip2o = np.linalg.norm(np.array([x,y])-origin_array) #compute a bunch of dists of intersection points -> (1a1,1a2)
        dist_list.append({"line": j["line"], "intersecting": name, "distance": dist_ip2o, "x": x, "y": y})

for l in dist_list:
    point = np.array([l["x"], l["y"]])
    valid = True
    for lp_name, lp in lp_coords.items():
        dist_ip2lp = np.linalg.norm(point-lp)
        if l["distance"] > dist_ip2lp+corr_param:
            valid = False
            break
    if valid: 
        cXout.append(l)

#limiter
#output of c(x) is used to define the bisector line startpoints and endpoints
line_lists = defaultdict(list)
for cX in cXout:
    line_lists[cX["line"]].append((cX["x"],cX["y"]))
for ln in line_lists:
    line_lists[ln].sort(key=lambda p: p[0])
for line_name, points in line_lists.items():
    x_min, y_min = points[0]
    x_max, y_max = points[-1]
    #print(f"{line_name} Minimum: ({x_min:.3f}, {y_min:.3f}) → Maxiumum: ({x_max:.3f}, {y_max:.3f})")
for line_name, points in line_lists.items():
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    plt.plot(x_vals, y_vals, 'b-')

plt.show()
