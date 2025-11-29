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

        city_graph.add_vertex(city.city + ", " + city.state , city.city + ", " + city.state + ", " + str(city.population) )
        node_in_map = city_graph.get_visualizer(city.city + ", " + city.state)
        #set longitude and latitude
        node_in_map.set_location(city.lon, city.lat)
        node_in_map.size = 5

    # edges
    n_of_neighbors = 5
    for c1 in range(len(major_cities)):
        city1 = major_cities[c1]
        key1 = f"{city1.city}, {city1.state}"  # Must match vertex_key above
        dists = []
        for c2 in range(len(major_cities)):
            if c1 == c2: continue # dont connect the same cities

            city2 = major_cities[c2]
            d = haversine(city1.lat, city1.lon, city2.lat, city2.lon)
            dists.append((d, city2))
        dists.sort(key=lambda x: x[0])
        for d, city2 in dists[:n_of_neighbors]:
            key2 = f"{city2.city}, {city2.state}"
            city_graph.add_edge(key1, key2,d)
            city_graph.get_link_visualizer(key1, key2).thickness = 1.0


  # visualizes map
    bridges.set_map(my_map)
    bridges.set_data_structure(city_graph)
    bridges.visualize()


#calculate distances between cities
def haversine(lat1, lon1, lat2, lon2):
    radius = 6371
    l1 = math.radians(lat1)
    l2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(l1) * math.cos(l2) * math.sin(dlambda / 2) ** 2
    return 2 * radius * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def prims():
    #COMPLETE
    return None

def kruskals():
    #COMPLETE
    return None

if __name__ == "__main__":
    main()
