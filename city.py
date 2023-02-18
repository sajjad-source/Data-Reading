#Author: Sajjad C Kareem
#Date: 10.31.2022
#Purpose: City class

class City:
    def __init__(self, cityCode, cityName, cityRegion, cityPopulation, cityLat, cityLong):
        self.cityCode = cityCode
        self.cityName = cityName
        self.cityRegion = cityRegion
        self.cityPopulation = int(cityPopulation)
        self.cityLat = float(cityLat)
        self.cityLong = float(cityLong)


    def __str__(self):
        strCityName = str(self.cityName)
        strCityPopulation = str(self.cityPopulation)
        strCityLat = str(self.cityLat)
        strCityLong = str(self.cityLong)

        return f'{strCityName}, {strCityPopulation}, {strCityLat}, {strCityLong}'
