from skimage import io, color
import os
import numpy as np

colors = {}
multicam = {}	# Based of wiki values

# Load GW paint colors
for fileName in os.listdir("gwpaints"):
    if fileName.endswith(".png"):
        rgb = io.imread(os.path.join("gwpaints", fileName))
        #print(rgb.shape)
        lab = color.rgb2lab(rgb[30:32,30:32,:3])
        #print(lab)
        fn = fileName.split("_")
        colors[fn[0]] = lab

# Load Multicam wiki colors
for fileName in os.listdir("multicam"):
    if fileName.endswith(".png"):
        rgb = io.imread(os.path.join("multicam", fileName))
        lab = color.rgb2lab(rgb[30:32,30:32,:3])
        fn = fileName.split(".")
        multicam[fn[0]] = lab

im = io.imread("multicam.png")
lab = color.rgb2lab(im)
multicam2 = (np.reshape(lab, (lab.shape[0] * lab.shape[1], 3)), lab.shape)

im = io.imread("multicam_arid.png")
lab = color.rgb2lab(im)
arid = (np.reshape(lab, (lab.shape[0] * lab.shape[1], 3)), lab.shape)

im = io.imread("multicam_tropic.png")
lab = color.rgb2lab(im)
tropic = (np.reshape(lab, (lab.shape[0] * lab.shape[1], 3)), lab.shape)

im = io.imread("multicam_alpine.png")
lab = color.rgb2lab(im)
alpine = (np.reshape(lab, (lab.shape[0] * lab.shape[1], 3)), lab.shape)

im = io.imread("multicam_night.png")
lab = color.rgb2lab(im)
night = (np.reshape(lab, (lab.shape[0] * lab.shape[1], 3)), lab.shape)

