import os

import matplotlib.pyplot as plt
import numpy as np

from skimage import io
from skimage import img_as_float
from skimage import color




path_to_training_retinal_ims = 'data/training/images/'
path_to_training_retinal_masks = 'data/training/masks/'
path_to_training_retinal_vessels = 'data/training/vessels/'
path_to_training_arteries = 'data/training/arteries/'
path_to_training_veins = 'data/training/veins/'
retinal_im_list = os.listdir(path_to_training_retinal_ims)

def compute_saturation(retinal_image):
    '''
    This function expects a retinal_image object
    1) retinal image 
    2) Field Of View mask 
    3) binary vessel map
    4) binary artery map
    5) binary vein map
    You may want to use (part of) them, or not
    '''
    return color.rgb2hsv(retinal_image.image)[:,:,1]

def compute_red_intensity(retinal_image):
    '''
    This function expects a retinal_image object.
    '''
    return retinal_image.image[:,:,0]


class retinal_image:   
    def __init__(self, name, train_or_test):
        self.name = name
        if train_or_test == 'train':
            path_im = path_to_training_retinal_ims
            path_mask = path_to_training_retinal_masks
            path_vessels = path_to_training_retinal_vessels
            path_arteries = path_to_training_arteries
            path_veins = path_to_training_veins
        elif train_or_test == 'test':
            path_im = path_to_training_retinal_ims
            path_mask = path_to_training_retinal_masks
            path_vessels = path_to_training_retinal_vessels
            path_arteries = path_to_training_arteries
            path_veins = path_to_training_veins
        else:
            print('Invalid mode')
            
        self.image = img_as_float(io.imread(path_im+name))
        self.mask = io.imread(path_mask+name[:-4]+'_mask.gif', dtype=bool)
        self.vessels = io.imread(path_vessels+name, dtype=bool) #[:-4]+'.png'
        self.arteries = io.imread(path_arteries+name, dtype=bool) #[:-4]+'.png'
        self.veins = io.imread(path_veins+name, dtype=bool) #[:-4]+'.png'
        
        # AVAILABLE FEATURES: These are place-holders for features that you may want to compute out of each image
        self.saturation = None
        self.red_intensity = None
        
    # The retinal_image object knows how to compute these features. 
    # It does that by calling to the functions defined in the previous cells    
    def load_saturation(self):
        # this calls an external function. If the attribute has not been initialized above, this will crash.
        self.saturation = compute_saturation(self)
    
    def load_red_intensity(self):
        self.red_intensity = compute_red_intensity(self)  
        
image = retinal_image(retinal_im_list[15], 'train')
io.imshow(image.vessels)
plt.show() 


from skimage.feature import hog
from skimage import data, color, exposure

from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

image=image.vessels
from skimage.morphology import disk

# perform skeletonization
skeleton = skeletonize(image)

##TODO - MOSTRAR SKELETON EM CIMA DA IMAGEM ORIGINAL 
    
    
# display results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                         sharex=True, sharey=True,
                         subplot_kw={'adjustable': 'box-forced'})

ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('original', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()

from scipy.ndimage import binary_hit_or_miss


B1 = np.array([[0, 1, 0], 
                   [1, 1, 1], 
                   [0, 1, 0]])
B2 = np.array([[1, 0, 1], 
                   [0, 1, 0], 
                   [1, 0, 1]])
B3=np.array([[0, 1, 0], 
                 [1, 1, 1], 
                 [0, 0, 0]])

B4=np.array([[1, 0, 1], 
                 [0, 1, 0],
                 [1, 0, 0]])  

B5=np.array([[0, 1, 0], 
                 [1, 1, 0],
                 [0, 1, 0]])

B6=np.array([[1, 0, 0],
                 [0, 1, 0],
                 [1, 0, 1]])

B7=np.array([[0, 0, 0],
                 [1, 1, 1],
                 [0, 1, 0]])

B8=np.array([[0, 0, 1], 
                 [0, 1, 0],
                 [1, 0, 1]])

B9=np.array([[0, 1, 0],
                [0, 1, 1],
                 [0, 1, 0]])

B10=np.array([[1, 0, 1],
                 [0, 1, 0],
                 [0, 0, 1]])
B11=np.array([[1, 0, 1], 
                 [0, 1, 0], 
                 [0, 1, 0]])

B12=np.array([[0, 1, 0], 
                 [1, 1, 0], 
                 [0, 0, 1]])

B13=np.array([[1, 0, 0], 
                 [0, 1, 1], 
                 [1, 0, 0]])

B14=np.array([[0, 0, 1], 
                 [1, 1, 0], 
                 [0, 1, 0]])

B15=np.array([[0, 1, 0], 
                 [0, 1, 0], 
                 [1, 0, 1]])
B16=np.rot90(B14)
B17 = np.rot90(B15)
B18 = np.rot90(B16)

IMhit_mis=(binary_hit_or_miss(skeleton,B1)+binary_hit_or_miss(skeleton,B2)+binary_hit_or_miss(skeleton,B3)+binary_hit_or_miss(skeleton,B4)+binary_hit_or_miss(skeleton,B5)+binary_hit_or_miss(skeleton,B6)+binary_hit_or_miss(skeleton,B7)+binary_hit_or_miss(skeleton,B8)+binary_hit_or_miss(skeleton,B9)+binary_hit_or_miss(skeleton,B10)+binary_hit_or_miss(skeleton,B11)+binary_hit_or_miss(skeleton,B12)+binary_hit_or_miss(skeleton,B13)+binary_hit_or_miss(skeleton,B14)+binary_hit_or_miss(skeleton,B15)+binary_hit_or_miss(skeleton,B16)+binary_hit_or_miss(skeleton,B17)+binary_hit_or_miss(skeleton,B18))

IMhit_mis_bin=IMhit_mis.astype(np.int); 
coordinates=np.nonzero(IMhit_mis_bin)

coordinates=np.nonzero(IMhit_mis_bin)

plt.figure(3)

plt.imshow(skeleton)
plt.scatter(x=coordinates[1],y=coordinates[0],c='r',s=20,marker='x')
plt.show() 
####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
# Applie Homomorphic Filtering  to the image

import cv2 

img1 = retinal_image(retinal_im_list[2], 'train')

img= img1.image
plt.figure(4)
plt.imshow(img)
plt.show()

img = np.float32(img)

rows,cols,dim = img.shape

rh, rl, cutoff = 0.95,0.25,0.01 #possivelmente será necessário modificar os parametros 

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
H,S,V = cv2.split(imgHSV)
indices=(img1.mask==0)
indices=indices.astype(np.int)
H[indices==1]=0
S[indices==1]=0
V[indices==1]=0

cv2.imshow('H', H)

cv2.imshow('S', S)

cv2.imshow('V', V)


V_log = np.log(V+0.01)
#H_log = np.log(H+0.01)
#S_log = np.log(S+0.01)
V_fft = np.fft.fft2(V_log)
#H_fft = np.fft.fft2(H_log)
#S_fft = np.fft.fft2(S_log)
V_fft_shift = np.fft.fftshift(V_fft)
#H_fft_shift = np.fft.fftshift(H_fft)
#S_fft_shift = np.fft.fftshift(S_fft)
 

DX = cols/cutoff
G = np.ones((rows,cols))
for i in range(rows):
    for j in range(cols):
        G[i][j]=((rh-rl)*(1-np.exp(-((i-rows/2)**2+(j-cols/2)**2)/(2*DX**2))))+rl

result_filter_V = G * V_fft_shift
#result_filter_H = G * H_fft_shift
#result_filter_S = G * S_fft_shift
result_interm_V = np.real(np.fft.ifft2(np.fft.ifftshift(result_filter_V)))
#result_interm_H = np.real(np.fft.ifft2(np.fft.ifftshift(result_filter_H)))
#result_interm_S = np.real(np.fft.ifft2(np.fft.ifftshift(result_filter_S)))

result_V = np.exp(result_interm_V)
#result_H = np.exp(result_interm_H)
#result_S = np.exp(result_interm_S)



result1 = np.dstack((H,S,result_V))
result1 = np.float32(result1)
imgRGB = cv2.cvtColor(result1, cv2.COLOR_HSV2RGB)
#imgRGB = cv2.cvtColor(result1, cv2.COLOR_YCrCb2RGB)

cv2.imshow('Homomorphic Filtered Result', result_V)

cv2.imshow('Homomorphic Filtered RGB Image', imgRGB)




###############################
#center disk

#from skimage.color import rgb2gray

img_gray= cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)

from skimage.feature import blob_dog
from skimage.filters import gaussian 
img_gray=gaussian(img_gray,sigma=5)

blobs_dog = blob_dog(img_gray, max_sigma=30, threshold=.7)

blobs = [blobs_dog]
colors = ['red']
titles = ['Difference of Gaussian']
sequence = zip(blobs, colors, titles)

from skimage.filters import gaussian
meancolorintensity=[]; 
for blobs, cor, title in sequence:
    fig, ax = plt.subplots(1, 1)
    ax.set_title(title)
    ax.imshow(image, interpolation='nearest',cmap='gray')
    for blob in blobs:
        y, x, r = blob
        print("y",y,"x",x,"r",r)
        c = plt.Circle((x, y), r, color=cor, linewidth=1, fill=False)
        ax.add_patch(c)
        area=np.mean(img_gray[int(y-round(r)):int(y+round(r)),int(x-round(r)):int(x+round(r))]) #ver se estao trocados
        print(area)
        meancolorintensity.append(area)
print(meancolorintensity)
plt.imshow(img_gray,cmap='gray')
maxIndex=np.argmax(meancolorintensity); 

plt.scatter(x=blobs[maxIndex,1],y=blobs[maxIndex,0],c='r',s=20,marker='x')
plt.imshow(img_gray,cmap='gray')

plt.show()






















####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################3
#ipainting

#import scipy

# Read in image
#img1 = retinal_image(retinal_im_list[15], 'train')
#
#img= img1.image
#
#plt.figure(4)
#plt.imshow(img)
#plt.show() 
#
#plt.figure(5)
#plt.scatter(x=coordinates[1],y=coordinates[0],c='r',s=20,marker='x')
#plt.show()
#plt.imshow(img)
#plt.show()
#
#import numpy as np
#import matplotlib.pyplot as plt
#from skimage.restoration import inpaint
#from scipy.ndimage import binary_dilation, generate_binary_structure


#mask = img1.vessels



#struct1 = generate_binary_structure(2, 2)
#mask1 = binary_dilation(mask, structure=struct1).astype(np.float)
#img_gray = color.rgb2gray(img)
# Defect image over the same region in each color channel

#image_result = inpaint.inpaint_biharmonic(img, mask, multichannel=True)

#fig, axes = plt.subplots(ncols=2, nrows=2)
#ax = axes.ravel()

#ax[0].set_title('Original image')
#ax[0].imshow(img)
#
#ax[1].set_title('Mask')
#ax[1].imshow(mask, cmap=plt.cm.gray)
#
#ax[2].set_title('Defected image')
#ax[2].imshow(img_gray)
#
#ax[3].set_title('Inpainted image')
#ax[3].imshow(image_result)
#
#for a in ax:
#    a.axis('off')
#
#
#fig.tight_layout()
#plt.show()




