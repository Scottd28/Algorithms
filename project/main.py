from bridges.bridges import *
import math
from bridges.data_src_dependent import data_source
from bridges.graph_adj_list import GraphAdjList
from bridges.data_src_dependent import *
from bridges.dl_element import *
from bridges.us_map import *


#how to use the USCities Dataset
def main():

    # create the Bridges object, set credentials
    bridges = Bridges(306, "ScottR1" ,"1011084303546")
    # map info
    state_info = get_us_map_data()
    my_map = USMap(state_info)

    #city info
    all_cities = get_us_cities_data()
    major_cities = [ c for c in all_cities if c.population > 110400]
    print(len(major_cities))
    city_graph = GraphAdjList()


    #vertices
    for city in major_cities:

        city_graph.add_vertex(city.city, city.city + ", " + city.state + ", " + str(city.population) )
        node_in_map = city_graph.get_visualizer(city.city)
        #set longitude and latitude
        node_in_map.set_location(city.lon, city.lat)
        node_in_map.size = 5


  # visualizes map
    bridges.set_map(my_map)
    bridges.set_data_structure(city_graph)
    bridges.visualize()


#calculate distances between cities
def haversine(lat1, lon1, lat2, lon2):
    return None

def prims():
    #COMPLETE
    return None

def kruskals():
    #COMPLETE
    return None

if __name__ == "__main__":
    main()
