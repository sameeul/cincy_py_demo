import numpy as np 
from skimage import color, data
import time
from scipy import ndimage

import libtest

def convolve_2D(image, kernel):
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]

    output = np.zeros((image.shape))
    imagePadded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        for x in range(image.shape[0]):
            # Go to next row once kernel is out of bounds
            if x > image.shape[0] - xKernShape:
                break
            try:
                # Only Convolve if x has moved by the specified Strides
                output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
            except:
                break

    return output


def detect_edges(image,masks):
    edges=np.zeros(image.shape)
    for mask in masks:
        # using Python Implementation
        #edges=np.maximum(convolve_2D(image,mask), edges)
        
        #using our C++ implementation
        edges=np.maximum(libtest.convolution_2d(image,mask), edges)
        
        #using SciPy Convolution
        #edges=np.maximum(ndimage.convolve(image,mask), edges)
        
    return edges


def test_edge_detedtion():
    image=color.rgb2gray(data.astronaut())
    kernels= [ np.array([[-1,0,1],[-1,0,1],[-1,0,1]]), 
            np.array([[1,1,1],[0,0,0],[-1,-1,-1]]),
            np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]),
            np.array([[0,1,0],[-1,0,1],[0,-1,0]]) 
        ] 
    
    edges=detect_edges(image, kernels)

if __name__ == "__main__":
    start_time = time.time()
    test_edge_detedtion()
    end_time = time.time()
    print(f"elapsed time = {1000*(end_time-start_time)} ms")