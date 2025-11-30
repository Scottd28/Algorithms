import argparse

from bridges.bridges import *
import math
from bridges.data_src_dependent import data_source
from bridges.graph_adj_list import GraphAdjList
from bridges.data_src_dependent import *
from bridges.dl_element import *
from bridges.us_map import *
from nbformat.sign import algorithms
from networkx.classes import neighbors

city_graph = GraphAdjList()
path = []
#how to use the USCities Dataset
def main(algorithm_type):

    # create the Bridges object, set credentials
    bridges = Bridges(306, "ScottR1" ,"1011084303546")


    # map info
    state_info = get_us_map_data()
    my_map = USMap(state_info)

    #city info
    all_cities = get_us_cities_data()
    major_cities = [ c for c in all_cities if c.population > 110400]
    print(len(major_cities))


    #vertices
    for city in major_cities:

        city_graph.add_vertex(city.city + ", " + city.state , city.city + ", " + city.state + ", " + str(city.population) ) #key is CITY, STATE
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
            distance = haversine(city1.lat, city1.lon, city2.lat, city2.lon)
            dists.append((distance, city2))
        dists.sort()
        for distance, city2 in dists[:n_of_neighbors]:
            key2 = f"{city2.city}, {city2.state}"
            city_graph.add_edge(key1, key2,distance)
            city_graph.get_link_visualizer(key1, key2).thickness = 1.0


    #figure what algorithm do you need to do
    if algorithm_type.lower() == "prims":
        #prims()  TODO:FIX
        exit()
    elif algorithm_type.lower() == "kruskals":
        #kruskals()
        exit()
    else:
        print("Invalid method. Choose 'Prims' or 'Kruskals'.")


  # visualizes map
    bridges.set_map(my_map)
    bridges.set_data_structure(city_graph)
    bridges.visualize()


#calculate distances between cities
def haversine(lat1, lon1, lat2, lon2):
    radius = 6371 #radius around the earth in km
    l1 = math.radians(lat1)
    l2 = math.radians(lat2)
    dlatitude = math.radians(lat2 - lat1)
    dlongitude = math.radians(lon2 - lon1)

    a = math.sin(dlatitude / 2) ** 2 + math.cos(l1) * math.cos(l2) * math.sin(dlongitude / 2) ** 2
    return 2 * radius * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def prims(start):
    #COMPLETE
    '''
    Select any vertex in G as the root of the MST.
    Choose the vertex v that is closest to the set of vertices already taken.
    Add v to the MST.
    Goto step 2 until all vertices in G are in the MST.
    '''
    visited = set() #list of all the city objects visited
    visited.add(start)
    while len(visited) < len(city_graph.vertices):
        allEdges = {}
        for v in visited:
            neighbors = v.get_adjacency_list()
            for n in neighbors:
                if n not in visited:
                    edge = city_graph.get_edge(v,n)
                    allEdges[n] = edge.get_weight()
            closest = min(allEdges, key=allEdges.get)
            visited.add(closest)
            path.append(closest)

    return path

def kruskals():
    #COMPLETE
    '''
    The general strategy is to select edges in order of smallest weight
    and accept an edge if it does not form a cycle.
    '''
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MST Major Cities In America')

    parser.add_argument(
        '-method',
        dest='algorithm_type',
        required=True,
        type=str,
        help='Kruskals, Prims'
    )
    args = parser.parse_args()

    main(args.algorithm_type)
