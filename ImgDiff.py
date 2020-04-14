import os, time, sys
from PIL import Image
import math, random
import numpy as np
from numpy import array
from helper import hlpr

def diff(imo,imc,row,col):
	img=np.zeros((row,col))
	for i in range(0,row):
		for j in range(0,col):
			img[i][j]=abs(imo[i][j]-imc[i][j])
			if img[i][j]!=0:
				print img[i][j]

	return img

imo = Image.open(os.getcwd() + '/encryptImgO.png')
col,row=imo.size
imc = imo = Image.open(os.getcwd() + '/encryptImg.png')
imo = hlpr.to_rgb_matrix(imo)
imc = hlpr.to_rgb_matrix(imc)

imgro = hlpr.get_two_dim_img_gray(row, col, imo[0])
imggo = hlpr.get_two_dim_img_gray(row, col, imo[1])
imgbo = hlpr.get_two_dim_img_gray(row, col, imo[2])
imgro = array(imgro)
imggo = array(imggo)
imgbo = array(imgbo)

imgrc = hlpr.get_two_dim_img_gray(row, col, imc[0])
imggc = hlpr.get_two_dim_img_gray(row, col, imc[1])
imgbc = hlpr.get_two_dim_img_gray(row, col, imc[2])
imgrc = array(imgrc)
imggc = array(imggc)
imgbc = array(imgbc)

imgr=diff(imgro,imgrc,row,col)
imgg=diff(imggo,imggc,row,col)
imgb=diff(imgbo,imgbc,row,col)

imgr=imgr.flatten()
imgg=imgg.flatten()
imgb=imgb.flatten()
img=np.row_stack((imgr,imgg,imgb))
img=hlpr.get_two_dim_img_rgb(row,col,img)
img.save(os.getcwd() + '/img.png')