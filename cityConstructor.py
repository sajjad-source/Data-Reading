#Author: Sajjad C Kareem
#Date: 10.31.2022
#Purpose: City constructor

from city import City
from quicksort import *


worldCitiesFile = open("world_cities.txt", 'r') #reading world_cities file
out = open("cities_out.txt", "w")
cities_list = []

for line in worldCitiesFile:  # for each line in world_cities.txt
    info_list = line.split(',')  # split the info separated by commas

    for i in range(len(info_list)):
        info_list[i] = info_list[i].strip() #strip the space

    # 0 - cityCode, #1 - cityName, #2 - cityRegion, #3 - cityPopulation, #4 - cityLat, #5 - cityLong
    c = City(info_list[0], info_list[1], info_list[2], info_list[3], info_list[4], info_list[5])  # call City class on each info

    cities_list.append(c) #append the info to a list


for c in cities_list: #for each city in cities list
    out.write(str(c)) #write it to cities_out.txt
    out.write('\n') #add space


worldCitiesFile.close() #close file
out.close() #close file



