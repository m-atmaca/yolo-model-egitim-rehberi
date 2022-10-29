import os
import cv2
from glob import glob

klasorPath = "klasör yolu\\*.png"

png = glob(klasorPath)

for j in png:
    print(j)
    img = cv2.imread(j)
    cv2.imwrite(j[:-3]+"jpg",img) #okunan resimlerdeki son 3 karakteri(png) alarak jpg ile değiştirildi
    os.remove(j) #bununla da okuyup jpg olarak yazdığım png görsellerinin png hallerini siliyoruz
    
    
