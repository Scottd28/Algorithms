import argparse

from bridges.bridges import *
import math

from bridges.data_src_dependent import *
import random
from bridges.us_map import *


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


    # create all vertices
    for city in major_cities:

        city_graph.add_vertex(city.city + "," + city.state , city.city + "," + city.state + "," + str(city.population) ) #key is CITY, STATE
        node_in_map = city_graph.get_visualizer(city.city + "," + city.state)
        #set longitude and latitude
        node_in_map.set_location(city.lon, city.lat)
        node_in_map.size = 5

    # create all edges
    for c1 in range(len(major_cities)):
        city1 = major_cities[c1]
        key1 = city1.city + ","  + city1.state

        for c2 in range(len(major_cities)):
            if c1 == c2: continue # dont connect the same cities
            city2 = major_cities[c2]
            distance = haversine(city1.lat, city1.lon, city2.lat, city2.lon) #calculate distance between cities
            key2 = city2.city + "," + city2.state
            city_graph.add_edge(key1, key2, distance)
            # city_graph.get_link_visualizer(key1, key2).thickness = 1.0  TODO: visualize only the mst




    #figure what algorithm do you need to do
    if algorithm_type.lower() == "prims":
        path = prims()
    elif algorithm_type.lower() == "kruskals":
        path = kruskals()
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

def prims():
    '''
    Select any vertex in G as the root of the MST.
    Choose the vertex v that is closest to the set of vertices already taken.
    Add v to the MST.
    Goto step 2 until all vertices in G are in the MST.
    '''
    mst = []
    visited = set()
    random_city = random.choice(list(city_graph.vertices.keys()))
    visited.add(random_city)
    while len(visited) < len(city_graph.vertices): #while we haven't visited all cities
         edges = []

         #add all possible edges we can pick from
         for v in visited:
            neighbor = city_graph.get_adjacency_list(v)
            for n in neighbor:
                 if n in visited: continue
                 edge = city_graph.get_edge(v,n)
                 edges.append((edge, n))

         edges.sort(key=lambda e: e[0].weight)#pick the closest
         edge, closest = edges.pop(0)
         visited.add(closest)
         mst.append(edge)
    return mst


def kruskals():
    #The general strategy is to select edges in order of smallest weight
    # and accept an edge if it does not form a cycle.
    mst = []
    edges = [] #collect all edges
    for city1 in city_graph.vertices:
        for city2 in city_graph.vertices:
            if city1 > city2: #dont count duplicates
                edges.append( city_graph.get_edge(city1, city2))
    edges.sort(key=lambda e: e.weight) # sort based on the distance

    while len(edges) > 0:
        edge = edges.pop(0)
        if dfsHasCycle(edge[0], edge[1]):  continue
        mst.append(edge)
    return mst

def dfsHasCycle(v1, v2):
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
    # python main.py -method prims
    main(args.algorithm_type)
