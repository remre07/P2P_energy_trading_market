import random

file = open("C:\\Users\\ramaz\\Desktop\\Bitirme_Projesi\\microgrid_matlab\\house1\\prosumerSellingPricesHourly.txt","w")
for i in range(24):
    file.write(str(random.randint(10, 28)) + "\n")

file.close
