from bridges.bridges import *
import sys
from bridges.data_src_dependent import data_source

#how to use the USCities Dataset
def main():

    # create the Bridges object, set credentials
    bridges = Bridges(306, "ScottR1" ,"1011084303546")

    # getting cities in North Carolina with populatino range or 200K-1M, limit to 25 cities
	# other parameters include elevation range, lat/long range
    map_data = data_source.get_us_cities_data()
    for m in map_data[:200]:
       print(m.city + ", " + m.state + ": population: " + str(m.population) + ", " + "elevation: " + str(m.elevation) + ", lat/long: " + str(m.lat) + "," + str(m.lon))


if __name__ == "__main__":
    main()
