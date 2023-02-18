from cs1lib import *
from city import City
from quicksort import *
from sort_cities import *


WIDTH = 720 #width of the screen
HEIGHT = 360 #height of the screen
cityPop = [] #empty list of the city Pop
cityPopFile = open('world_cities.txt', 'r') #read the sorted city population file


for line in cityPopFile: #for each line in the sorted city population file
    cities = line.split(',') #split the cities separated by ,
    for i in range(len(cities)): #for each index in the range of the separated cities list
        cities[i] = cities[i].strip() #strip the spaces of each spaces


    c = City(cities[0], cities[1], cities[2], cities[3], cities[4],  cities[5]) #call City class on each info

    cityPop.append(c) #append c to the city population list

sort(cityPop, compareCitiesPopulation) #sort the city list from most populous to least

img = load_image("world.png") #load the world map image
FRAMERATE = 1 #frame rate to 1 to show it slowly

x = 0 #x for long index
y = 0 #y for lat index

city_list = [] #empty list
def main(): #main func
    global x, y

    if len(city_list) < 49: #if the length of the city list (empty at first) is less than 49 cities
        city_list.append([cityPop[x].cityLong, cityPop[y].cityLat]) #append to the city the longitude of each city in City pop
                                                                 #result: a list of lists of long and lat of first 50 cities
        x += 1 #increment x to go through every city Long
        y += 1 #increment y to go through every city Lat

    draw_image(img, 0, 0) #draw the image
    disable_stroke() #disable stroke
    set_fill_color(1, 0, 0) #set color of circle to red
    for pair in range(0, len(city_list)): #for each pair of long and lat inside the list of lists of city list

        long_x = int(WIDTH/360.0) * (180+city_list[pair][0]) #access the longitude at city_list[pair][0], pair being the list inside the list
                                                             #and 0 being the longitude index
        lat_x = int(HEIGHT/180.0) * (90-city_list[pair][1])#access the longitude at city_list[pair][0], pair being the list inside the list
                                                           #and 1 being the lat index
        draw_circle(long_x, lat_x, 3) #draw the circle


cityPopFile.close() #close the file
start_graphics(main, width=WIDTH, height=HEIGHT, framerate=FRAMERATE) #start graphics