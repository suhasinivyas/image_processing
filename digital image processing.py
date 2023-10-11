import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np
from skimage.transform import rescale, resize
from skimage import color, filters, exposure, util, restoration
import tkinter as tk
from tkinter import filedialog
import cv2
import pandas as pd
from color_detection import *

root = tk.Tk("DIP")
root.geometry('650x800')
root.config(bg="gray36")
path = filedialog.askopenfilename()


def flipping():
    o = image.imread(path)
    image1 = plt.subplot(221)
    _ = image1.imshow(o)
    _ = plt.title('Original')
    image1.axis("off")

    image2 = plt.subplot(222)
    gray = np.flipud(o)
    _ = image2.imshow(gray)
    _ = plt.title('Flipped Image')
    image2.axis("off")
    plt.show()


def noise_IMG():
    o = image.imread(path)
    image1 = plt.subplot(221)
    _ = image1.imshow(o)
    _ = plt.title('Original')
    image1.axis("off")
    image2 = plt.subplot(222)
    random_image = util.random_noise(o)
    _ = image2.imshow(random_image)
    _ = plt.title('Random Noise Image')
    image2.axis("off")
    image3 = plt.subplot(223)
    un_noise = restoration.denoise_tv_chambolle(random_image, weight=0.1, multichannel=True)
    _ = image3.imshow(un_noise)
    _ = plt.title('De-noised Image')
    image3.axis("off")
    plt.show()


def scaled():
    o = image.imread(path)
    image1 = plt.subplot(121)
    _ = image1.imshow(o)
    _ = plt.title('Original')
    image1.axis("on")
    image2 = plt.subplot(122)
    scaling = rescale(o, 1 / 4, anti_aliasing=True, multichannel=True)
    _ = image2.imshow(scaling)
    _ = plt.title('Rescaled')
    image2.axis("on")
    plt.show()


def resized():
    o = image.imread(path)
    h = int(input("enter the height"))
    w = int(input("enter the width"))
    image1 = plt.subplot(121)
    _ = image1.imshow(o)
    _ = plt.title('Original')
    image1.axis("on")
    image2 = plt.subplot(122)
    image_resize = resize(o, (h, w), anti_aliasing=True)
    _ = image2.imshow(image_resize)
    _ = plt.title('Resized Image')
    image2.axis("on")
    plt.show()


def GRAY_scale():
    o = image.imread(path)
    image1 = plt.subplot(121)
    _ = image1.imshow(o)
    _ = plt.title('Original')
    image1.axis("off")
    image2 = plt.subplot(122)
    gray = color.rgb2gray(o)
    _ = image2.imshow(gray, cmap=plt.cm.gray)
    _ = plt.title('Grayscale Image')
    image2.axis("off")
    plt.show()


def edges():
    o = image.imread(path)
    image1 = plt.subplot(121)
    _ = image1.imshow(o)
    _ = plt.title('Original')
    image1.axis("off")
    image2 = plt.subplot(122)
    edge_sobel = filters.sobel(o)
    _ = image2.imshow(edge_sobel)
    _ = plt.title('Edged Image')
    image2.axis("off")
    plt.show()


def gaussian():
    o = image.imread(path)
    image1 = plt.subplot(121)
    _ = image1.imshow(o)
    _ = plt.title('Original')
    image1.axis("off")
    image2 = plt.subplot(122)
    gaussian_img = filters.gaussian(o, multichannel=True)
    _ = image2.imshow(gaussian_img)
    _ = plt.title('Gaussian Filter')
    image2.axis("off")
    plt.show()


def expo():
    o = image.imread(path)
    image1 = plt.subplot(221)
    _ = image1.imshow(o)
    image1.axis("off")
    _ = plt.title('original')
    expo_img = exposure.equalize_hist(o)
    image2 = plt.subplot(222)
    _ = image2.imshow(expo_img)
    image2.axis("off")
    _ = plt.title('histogram')
    expo_img1 = exposure.equalize_adapthist(o, clip_limit=0.03)
    image3 = plt.subplot(223)
    _ = image3.imshow(expo_img1)
    _ = plt.title('adaptive_histogram')
    image3.axis("off")
    plt.show()


def colour():
    takeinput(path)
   #yaha wo program dalna tha but its not working to separate file hi rakhi h but wo bhi kaam nahi kr raha ek baar dekh le


l1 = tk.Label(root, text="Welcome! Choose your image processing option", font=("Times", 20), fg="misty rose", bg='gray36')
l1.pack()

f = tk.Button(root, text="1. Flip the image", font=("Times", 15), fg="Red", bg='gold', command=flipping)
f.pack(expand=True)
f1 = tk.Button(root, text="2. Noisy image", font=("Times", 15), fg="Red", bg='gold', command=noise_IMG)
f1.pack(expand=True)
f2 = tk.Button(root, text="3. Scaled image", font=("Times", 15), fg="red", bg='gold', command=scaled)
f2.pack(expand=True)
f3 = tk.Button(root, text="4. Resized image", font=("Times", 15), fg="red", bg='gold', command=resized)
f3.pack(expand=True)
f4 = tk.Button(root, text="5. Grayscale image", font=("Times", 15), fg="red", bg='gold', command=GRAY_scale)
f4.pack(expand=True)
f5 = tk.Button(root, text="6. Edged image", font=("Times", 15), fg="red", bg='gold', command=edges)
f5.pack(expand=True)
f6 = tk.Button(root, text="7. Gaussian filter on an image", font=("Times", 15), fg="red", bg='gold', command=gaussian)
f6.pack(expand=True)
f7 = tk.Button(root, text="8. Histogram of an image", font=("Times", 15), fg="red", bg='gold', command=expo)
f7.pack(expand=True)
f7 = tk.Button(root, text="9. color Detection", font=("Times", 15), fg="red", bg='gold', command=colour)
f7.pack(expand=True)


root.mainloop()
