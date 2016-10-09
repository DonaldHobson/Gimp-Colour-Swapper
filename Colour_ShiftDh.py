#!/usr/bin/env python
MaxCols=4

from gimpfu import *
import numpy as np
from scipy.interpolate import Rbf
#relies on standard libraries



Modes=('multiquadric','inverse','gaussian','linear','cubic','quintic','thin_plate')
def colourSwap(img, layer, count,mode, *colss) :
        gimp.progress_init("Testing layer...")

        cols=np.zeros((count,2,3),dtype=np.uint8)#create array to store RGB values from colour pickers 

        for pos in range(int(count*2+0.5)):
                i=colss[pos]
                colour=[int(255*float(j)+0.5) for j in str(i)[5:-1].split(",")[:3]]#turns colour object into rgb array
                for j in range(3):
                        cols[pos//2,pos%2,j]=colour[j]#arranges the colour data into several pairs of rgb values
                        pass


        
        layername = layer.name+" Colour shift "+Modes[mode]
        
        
                        
        gimp.progress_update(0.1)
  
        
        pdb.gimp_image_undo_group_start(img)

        #Create New Layer
        destDrawable = gimp.Layer(img, layername, layer.width, layer.height,
                                  layer.type, layer.opacity, layer.mode)
        img.add_layer(destDrawable, 0)
        
        

        # No need to clear the layer here --
        # we'll initialize it to zero when we create the pixel array.

        srcWidth, srcHeight = layer.width, layer.height
        srcRgn = layer.get_pixel_rgn(0, 0, srcWidth, srcHeight,False, False)
        
        
        src_pixels_A = np.fromstring(srcRgn[0:srcWidth, 0:srcHeight], dtype=np.uint8).reshape(layer.height,layer.width,-1)#source pixels as numpy array. Possabilly containing alpha
        src_pixels=src_pixels_A[...,:3]#numpy array not containing alpha values
        dstRgn = destDrawable.get_pixel_rgn(0, 0,layer.width, layer.height,True, True)

        
        dest_pixels = np.zeros((layer.height,layer.width,3),dtype=np.uint8)#numpy array of zeros. To fill with result



        
        points = cols[:,0,:]
        for i in range(3):
                
                func=Rbf(points[:,0],points[:,1],points[:,2],cols[:,1,i],function=Modes[mode])#interpolate

                
                dest_pixels[...,i]=np.clip(func(src_pixels[:,:,0],src_pixels[:,:,1],src_pixels[:,:,2]),0,255)#fit to range 0 to 255 to prevent overflow
                
                

                gimp.progress_update(i*.30+0.35)#progress bar update




        src_pixels_A[...,:3]=dest_pixels#combine the new pixels with the alpha
        dstRgn[0:layer.width, 0:layer.height] = src_pixels_A.tobytes(order="C") #send data to image


        #cleanup
        destDrawable.flush()
        destDrawable.merge_shadow(True)
        destDrawable.update(0, 0, layer.width, layer.height)
        pdb.gimp_image_undo_group_end(img)

register(
        "python_fu_colour_swapper",
        "Recolour the image",
        "Replace the colours with other colours",
        "Donald Hobson",
        "Donald Hobson",
        "2016",
        "<Image>/Colors/Colour-Swap",
        "*",
        [
                (PF_SLIDER, "ColourSwaps",  "ColourSwaps", MaxCols, (2, MaxCols, 1)),(PF_OPTION, "mode", "Mode", 0, Modes)]+[
                (PF_COLOR, "From", "From", (1.0, 1.0, 1.0)),(PF_COLOR, "To", "To", (1.0, 1.0, 1.0))

        ]*MaxCols,
        [],
        colourSwap)

main()
