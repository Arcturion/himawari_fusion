#obtained from https://github.com/gSasikala/ftp-himawari8-hsd/blob/main/examples/Processing_Satellite_Imagery.ipynb
#and https://github.com/ZPYin/Himawari-8_Visualizer/tree/master/notebook

#install package satpy pake conda di environment baru conda create -c conda-forge -n my_satpy_env python satpy
#install cartopy sebelumnya install dulu pyproj dan shapely lewat pipwin


import glob
from satpy import Scene
from datetime import datetime
import matplotlib.pyplot as plt

#files = glob.glob(r'HS_H08_20221118_0600_B03_FLDK_R05_S0110.DAT') 
files = glob.glob(r'*.DAT') 

#scn = Scene(filenames=files,  reader='ahi_hsd',filter_parameters={'start_time': datetime(2021,5,25,2,00), 'end_time': datetime(2021,5,25,2,10)})
scn = Scene(filenames=files,  reader='ahi_hsd')

#https://github.com/JeanPaulKoole/Satelliet/blob/135843d9f566398b926ffe75897d7dac01569f6f/Satelliet-2.ipynb
scn.show("B03")
scn['B03'].plot.imshow()

scn.load(["B03"])
scn.save_dataset('B03', 'B03.png')

image = plt.imread('B03.png') 
plt.imshow(image)
cbar=plt.colorbar()
cbar.set_label("Kelvin")
plt.show()


import cartopy.crs as ccrs
import cartopy.feature as cfeature

country_borders = cfeature.NaturalEarthFeature(
    category='cultural',
    name='‘admin_0_boundary_lines_land',
    scale='50m',
    facecolor='none')
