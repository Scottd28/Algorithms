import argparse

from bridges.bridges import *
from math import radians, cos, sin, asin, sqrt

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


    #figure what algorithm do you need to do
    if algorithm_type.lower() == "prims":
        path = prims()
        print(path)
        for s, e, w in path:
            city_graph.add_edge(s, e, w)
    elif algorithm_type.lower() == "kruskals":
        path = kruskals()
        print(path)
        for s, e, w in path:
            city_graph.add_edge(s, e, w)
    else:
        print("Invalid method. Choose 'Prims' or 'Kruskals'.")


  # visualizes map
    bridges.set_map(my_map)
    bridges.set_data_structure(city_graph)
    bridges.visualize()


#calculate distances between cities
#stack overflow code from Michael Dunn https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def prims():
    '''
    Select any vertex in G as the root of the MST.
    Choose the vertex v that is closest to the set of vertices already taken.
    Add v to the MST.
    Goto step 2 until all vertices in G are in the MST.
    :return the MST
    '''
    vertices = list(city_graph.vertices.keys())
    start = random.choice(vertices)
    visited = {start}
    mst = []

    while len(visited) < len(vertices): #while we haven't visited all vertices
        best_edge = None
        best_dist = float("inf")

        for c1 in visited:
            for c2 in vertices: #all possible edges

                if c2 in visited or c2 == c1:
                    continue

                #calculate data for the distance
                city1 = city_graph.get_visualizer(c1)  # use visualizer instead or vetices
                lat1, lon1 = city1.location_y, city1.location_x

                city2 = city_graph.get_visualizer(c2)
                lat2, lon2 = city2.location_y, city2.location_x

                dist = haversine( lon1, lat1, lon2, lat2)

                if dist < best_dist: #if we havent picked the smallest option yet
                    best_dist = dist
                    best_edge = (c1, c2, dist)

        if best_edge is None:
            print("No edge found")
            break

        mst.append(best_edge)
        visited.add(best_edge[1])

    return mst


def kruskals():
    '''
    The general strategy is to select edges in order of smallest weight
    and accept an edge if it does not form a cycle.
    returns: the MST
    '''
    mst = []
    edges = []
    vertices = list(city_graph.vertices.keys())

    # collect all edges
    for i, c1 in enumerate(vertices): # keep track of this position so you can skip it
        for c2 in vertices[i+1:]:
            city1 = city_graph.get_visualizer(c1)
            city2 = city_graph.get_visualizer(c2)

            #calculate distance
            lat1, lon1 = city1.location_y, city1.location_x
            lat2, lon2 = city2.location_y, city2.location_x
            distance = haversine(lon1, lat1, lon2, lat2)

            edges.append((c1, c2, distance))

    edges.sort(key=lambda e: e[2]) #sort by distance

    #bridges doesnt have an adj list
    adj = {key: [] for key in vertices}

    #CALCULATE IF IT HAS CYCLES, you have all edges now, just check if doing another edge would cause a cycle
    def dfsHasCycle(v1, v2):
        visited = set()

        def dfs(current, target):
            if current == target: #we've already reached the target, we dont have to again
                return True

            visited.add(current)
            for neighbor in adj[current]:
                if neighbor not in visited:
                    return dfs(neighbor, target)

            return False

        return dfs(v1, v2)

    # Build MST
    for edge in edges:
        city1, city2, dist = edge
        if dfsHasCycle(city1, city2): #if it has a cycle go to the next smallest vertice
            continue
        mst.append(edge)
        adj[city1].append(city2)
        adj[city2].append(city1)

    return mst



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
