from bridges.bridges import *
import math
from bridges.data_src_dependent import data_source
from bridges.graph_adj_list import GraphAdjList

#how to use the USCities Dataset
def main():

    # create the Bridges object, set credentials
    bridges = Bridges(306, "ScottR1" ,"1011084303546")
    g = GraphAdjList()

    map_data = data_source.get_us_cities_data()
    filtered_cities = [c for c in map_data if c.population >= 150000]

    #cities as vertices
    for city in filtered_cities:

        key = f"{city.city},{city.state}"
        g.add_vertex(key)
        g.get_vertex(key).data = city.city  # label the node with city name
        g.get_vertex(key).set_location(city.lat, city.lon)  # needed for map overlay



    for i in range(len(filtered_cities)):
        c1 = filtered_cities[i]
        dists = []

        for j in range(len(filtered_cities)):
            if i == j: continue
            c2 = filtered_cities[j]
            d = haversine(c1.lat, c1.lon, c2.lat, c2.lon)
            dists.append((d, c2))

        dists.sort(key=lambda x: x[0])

        # add edges to k nearest
        for d, c2 in dists[:4]:
            key1 = f"{c1.city},{c1.state}"
            key2 = f"{c2.city},{c2.state}"
            g.add_edge(key1, key2, d)

        # --- visualize in BRIDGES ---
    bridges.set_data_structure(g)

    # map view
    bridges.set_map_overlay(True)
    bridges.set_map("U.S")
    bridges.visualize()


#calculate distances between cities
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def prims():
    #COMPLETE
    return None

def kruskals():
    #COMPLETE
    return None

if __name__ == "__main__":
    main()
