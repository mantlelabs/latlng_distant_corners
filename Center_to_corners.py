# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:25:21 2018

@author: Kushal
"""

#python -u <side of square> <latitude of center> <longitude of center>

import math
import sys

count = 1

d = 0 #Distance in m is the first argument 
lat1 = 0 #Current lat point converted to radians
lon1 = 0 #Current long point converted to radians

try:
    d = float(sys.argv[1]) #Distance in m is the first argument 
    lat1 = float(sys.argv[2]) #Current lat point converted to radians
    lon1 = float(sys.argv[3]) #Current long point converted to radians

except IndexError:	#Exception in number of arguments.
	print("Number of arguments are less:", sys.exc_info()[0])
	#raise	#use this if you want to throw error to caller. Check python coding for more details.
	sys.exit(118)
                    
print "lat1: ",lat1
print "lon1: ",lon1 

count=1

if ((lat1 >= -90) and (lat1 <= 90)):
     count = 0
        
if ((lon1 >= -180) and (lon1 <= 180)):
     count = 0
        
if count != 0 :
    print("The Latitude Longitude is not correct", sys.exc_info()[0])
    sys.exit(118)



lat1 = math.radians(lat1) #Current lat point converted to radians
lon1 = math.radians(lon1) #Current long point converted to radians
                    
R = 6378100.00 #Radius of the Earth
d = (d*1.414)/2 #converted to diagnol for the specific program purpose 

angl = 0.785398 #Bearing is 45 degrees converted to radians.

lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
     math.cos(lat1)*math.sin(d/R)*math.cos(angl))

lon2 = lon1 + math.atan2(math.sin(angl)*math.sin(d/R)*math.cos(lat1),
             math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

lat2 = math.degrees(lat2)
lon2 = math.degrees(lon2)




angl = 2.35619 #Bearing is 135 degrees converted to radians.

lat3 = math.asin( math.sin(lat1)*math.cos(d/R) +
     math.cos(lat1)*math.sin(d/R)*math.cos(angl))

lon3 = lon1 + math.atan2(math.sin(angl)*math.sin(d/R)*math.cos(lat1),
             math.cos(d/R)-math.sin(lat1)*math.sin(lat3))

lat3 = math.degrees(lat3)
lon3 = math.degrees(lon3)


angl = 3.927 #Bearing is 225 degrees converted to radians.

lat4 = math.asin( math.sin(lat1)*math.cos(d/R) +
     math.cos(lat1)*math.sin(d/R)*math.cos(angl))

lon4 = lon1 + math.atan2(math.sin(angl)*math.sin(d/R)*math.cos(lat1),
             math.cos(d/R)-math.sin(lat1)*math.sin(lat4))

lat4 = math.degrees(lat4)
lon4 = math.degrees(lon4)

angl = 5.49779 #Bearing is 315 degrees converted to radians.

lat5 = math.asin( math.sin(lat1)*math.cos(d/R) +
     math.cos(lat1)*math.sin(d/R)*math.cos(angl))

lon5 = lon1 + math.atan2(math.sin(angl)*math.sin(d/R)*math.cos(lat1),
             math.cos(d/R)-math.sin(lat1)*math.sin(lat5))

lat5 = math.degrees(lat5)
lon5 = math.degrees(lon5)

print("lat1",lat2)
print("lon1",lon2)
print("lat2",lat3)
print("lon2",lon3)
print("lat3",lat4)
print("lon3",lon4)
print("lat4",lat5)
print("lon4",lon5)