import cv2
import numpy as np

def maskCalcurate(image,mask,color,value):
    m = np.where(image<value,0,1)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if m[i][j]==1:
                mask[i][j]=color

    return mask
    



def generate(image,threshold):
    class_num,height,width =image.shape

    rng = np.random.default_rng(0)
    colors = np.random.randint(low=0,high=255,size=(class_num,3))


    mask = np.zeros((height,width,3))
    for i,c in enumerate(colors):
        mask = maskCalcurate(image[i],mask,c,threshold)

    return mask

    


    


