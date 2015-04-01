from skimage import color
from math import sqrt
import numpy as np
from scipy.cluster.vq import kmeans,vq,whiten
import itertools
from pylab import imshow,figure,show,subplot
from load import colors, multicam, multicam2, arid, tropic, alpine, night

class Picture:
    def __init__(self, image):
        self.im = io.imread(image)
        self.lab = color.rgb2lab(im)
        self.pixel = np.reshape(lab, (lab.shape[0] * lab.shape[1], 3))
        self.num_of_colors = -1

    def index_colors():
        #print("scheme", scheme.shape)
        # performing the clustering
        centroids,_ = kmeans(scheme[0], 6) # six colors will be found
        # quantization
        qnt,_ = vq(scheme[0], centroids)

        # reshaping the result of the quantization
        centers_idx = np.reshape(qnt,(scheme[1][0], scheme[1][1]))
        clustered = color.lab2rgb(centroids[centers_idx])

        #print(centroids)
        #for i in range(0, len(centroids)):
        #    name = "color" + str(i)
        #    scheme[name] = centroids[i]

        figure(1)
        subplot(211)
        imshow(color.lab2rgb(np.reshape(scheme[0], (scheme[1][0], scheme[1][1]))))
        subplot(212)
        imshow(color.lab2rgb(clustered))
        show()

index_colors(arid)
#index_colors("multicam_tropic.png", tropic)
#index_colors("multicam_alpine.png", alpine)
#index_colors("multicam_night.png", night)

def distance(a, b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

def shortest_color(scheme):
    shortest = 10000
    short_colors = ()
    for a, b in itertools.combinations(scheme, 2):
        dist = distance(scheme[a], scheme[b])
        if dist < shortest:
            shortest = dist
            short_colors = (a,b)
    #print(short_colors, shortest)

def consolidate_colors(scheme):
    threshold = 21.2
    colors = 12
    similar_colors = []
    for a, b in itertools.combinations(scheme, 2):
        dist = distance(scheme[a], scheme[b])
        if dist < threshold:
            #print (dist)
            if a not in similar_colors:
                similar_colors.append(a)
            if b not in similar_colors:
                similar_colors.append(b)
    #print(colors, similar_colors)

#shortest_color(arid)
#consolidate_colors(arid)

arid_colors = []
for i in arid:
    best = 10000000
    best_color = ""
    for j in colors:
        #print (i, j)
        temp = distance(arid[i], colors[j][0,0])
        if temp < best:
            best = temp
            best_color = j
    #print (i, best_color, best)
    if best_color not in arid_colors:
        arid_colors.append(best_color)

print (arid_colors)

target = distance(colors["CeramiteWhite"][0,0], colors["FlashGitzYellow"][0,0])
best = 1000000000
best_colors = ()
for a, b in itertools.combinations(colors, 2):
    if (a == "JokaeroOrange") or (a == "MephistonRed"):
        pass
    else:
        dist = distance(colors[a][0,0], colors[b][0,0])
        if abs(target-dist) < best:
            best = abs(target-dist)
            best_colors = (a,b)
best = 10000000
for i in colors:
    if i == "MootGreen":
        pass
    else:
        dist = distance(colors["MootGreen"][0,0], colors[i][0,0])
        if abs(target-dist) < best:
            best = abs(target-dist)
            best_colors = ("MootGreen", i)

print (best, best_colors)
print (distance(colors["AlaitocBlue"][0,0], colors["JokaeroOrange"][0,0]))

print (distance(colors["AlaitocBlue"][0,0], colors["MephistonRed"][0,0]))

print (distance(colors["ThunderhawkBlue"][0,0], colors["JokaeroOrange"][0,0]))

print (distance(colors["ThunderhawkBlue"][0,0], colors["MephistonRed"][0,0]))






