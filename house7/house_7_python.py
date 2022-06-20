import numpy as np
from numpy.core.fromnumeric import size

array_from_file = np.loadtxt("house_7_produces_solarEnergy.txt",dtype=str)
row_number = np.size(array_from_file,0)
column_number = np.size(array_from_file,1)
for i in range(row_number):
    for j in range(1,column_number):
        array_from_file[i][j] = np.char.replace(array_from_file[i][j],',','.')

array_from_file = np.delete(array_from_file,0,1)
array_from_file = np.delete(array_from_file,1,1)
#print(array_from_file[310])
sav = np.savetxt("house_7_produces_solarEnergy_1.txt",array_from_file,fmt='%s')
