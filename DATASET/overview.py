#obtained from https://github.com/gSasikala/ftp-himawari8-hsd/blob/main/examples/Processing_Satellite_Imagery.ipynb

import glob
from satpy import Scene
from datetime import datetime
import matplotlib.pyplot as plt

#files = glob.glob(r'HS_H08_20221118_0600_B03_FLDK_R05_S0110.DAT') 
files = glob.glob(r'*.DAT') 

#scn = Scene(filenames=files,  reader='ahi_hsd',filter_parameters={'start_time': datetime(2021,5,25,2,00), 'end_time': datetime(2021,5,25,2,10)})
scn = Scene(filenames=files,  reader='ahi_hsd')

scn.load(["B03"])
scn.save_dataset('B02', 'B02.png')

image = plt.imread('B03_1.png') 
plt.imshow(image)
cbar=plt.colorbar()
cbar.set_label("Kelvin")
plt.show()
