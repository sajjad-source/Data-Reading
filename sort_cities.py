from cityConstructor import *
from quicksort import *

citiesAlpha = open('cities_alpha.txt', 'w') #alphabetically sorted file
citiesPopulation = open('cities_population.txt', 'w') #population size from most to least populous
citiesLatitude = open('cities_latitude.txt', 'w') #cities latitude from south to north

def compareCitiesName(a, b): #compare cities name func
    return a.cityName.lower() <= b.cityName.lower() #return True if city 1 name is <= city 2 name

def compareCitiesPopulation(a, b): #compare city population
    return b.cityPopulation <= a.cityPopulation #return True if city 2 population is <= city 1 population

def compareCitiesLatitude(a, b): #compare cities lat
    return a.cityLat <= b.cityLat #return true if city 1 lat is <= city 2 lat





sort(cities_list, compareCitiesName) #call the sort from quicksort on cities_list using compare city name func
for c in cities_list: #for cities in the alphabetically sorted cities list
    citiesAlpha.write(str(c)) #write it to cities_alpha.txt
    citiesAlpha.write('\n') #add space
citiesAlpha.close() #close the file


sort(cities_list, compareCitiesPopulation) #call the sort from quicksort on cities_list using compare city pop func
for c in cities_list: #for c in cities list sorted in most populous cities to least
    citiesPopulation.write(str(c)) #write the cities to 'cities_population.txt'
    citiesPopulation.write('\n') #add space
citiesPopulation.close() #close the file


sort(cities_list, compareCitiesLatitude) #call the sort from quicksort with cities sorted in south to north Lat
for c in cities_list: #for c in cities list sorted south to north Lat
    citiesLatitude.write(str(c)) #write out the cities to cities_latitude.txt
    citiesLatitude.write('\n') #add space
citiesLatitude.close() #close the file