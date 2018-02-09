import os
import urllib.request
from tkinter import *
import numpy as np

def show_entry_fields():
   print("Latitude: %s\Longitude: %s\Classname: %s" % (e1.get(), e2.get(), e3.get()))

master = Tk()
Label(master, text="Latitude ").grid(row=0)
Label(master, text="Longitude").grid(row=1)
Label(master, text="Classname").grid(row=2)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Done', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
mainloop()

lat = e1.get()
lon = e2.get()
cl = e3.get()
os.mkdir(cl)
api_key = 'AIzaSyD5i02-qQwL0nJU6NSQU1wyGU10LEkUE84'
w=640
h=480
heading = 151.78
#pitch = -0.76
pitch = np.arange(-1,1,0.1)
for i in range(1, 90,5):
	for j in range(1,10):
		url = 'https://maps.googleapis.com/maps/api/streetview?size=' + str(w)+'x'+str(h)+'&location='+str(lat)+','+str(lon)+'&heading='+str(i)+'&pitch='+str(pitch[j])+'&key='+api_key
		sname = str(cl) + '/'+'image'+ '%05d'%(i*j) +'.jpg'
		urllib.request.urlretrieve(url, sname)



