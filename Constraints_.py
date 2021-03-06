import networkx as nx
from networkx.algorithms import approximation
import numpy as np
from datetime import date
import csv
import pandas as pd
import math
from math import sqrt
import sys
from scipy.spatial import distance
import webbrowser

with open('PODlist2.csv', 'r+') as in_file:
    OurPOD = csv.reader(in_file)

    PODList = list(OurPOD)
    reader = csv.DictReader(in_file)
    long =[]
    lat =[]
    dict_list = []
    popn = []
    for line in reader:
        dict_list.append(line)
    print(dict_list)

    for row in OurPOD:
        long.append(row[3])
        lat.append(row[4])

    for row in reader:

        print(dict(row))
        PODdict = dict(row)


    #PODdict2 = {rows[0]: rows[1][2][3][4] for rows in OurPOD}
    #print(PODdict)
    #print (PODList)


def two_phase():
    # with open('Routes_new.csv', 'w+') as outfile:
    #  writer = csv.writer(outfile)
    #  routes = {rows[0]: rows[1] for rows in reader}
    cum_dist = 0
    firstcluster = []
    secondcluster = []
    routes = set()
    opt_weight = 1
    reduction_factor = range(0, 1)
    firstpod = 1
    route1 = []
    route2 = []
    G = nx.path_graph(5)
    print(nx.dijkstra_path_length(G, 0, 4))


    maxDistance = int(input("Enter maximum Distance for this cluster:  "))

    cum_dist= dist_cumu()
    for PodID in PODList:
        if cum_dist< maxDistance:
            #a = np.reshape(np.random.random_integers(0, 1, size=100), (10, 10))
            #D = nx.DiGraph(a)
            #g = nx.DiGraph(PODdict)
            #g = nx.path_graph(PODList)
            #length = nx.all_pairs_dijkstra_path_length(g)
            #print(length)

            firstcluster.append(PodID)
            cum_dist += cum_dist
        #print (firstcluster)

    for PodID in PODList:
        if PodID not in firstcluster:
            secondcluster.append(PodID)
    print("First Cluster:---")
    for item in firstcluster:
        print(item)

    print("Second Cluster:---")
    for item in secondcluster:
        print(item)

        def myDFS(graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            paths = []
            for node in graph.childrenOf(start):
                if node not in path:
                    paths.extend(myDFS(graph, node, end, path))
            return paths
    """
    #assume items in secondcluster are not yet time compliant
    # Create another route for items in second cluster and increase time constraint
    graph2 = List2Graph(PODList)
    time2 = input( "Enter Maximum time for second cluster items: ")
    g = nx.path_graph(graph2)

    length = nx.all_pairs_dijkstra_path_length(g)
    #print(length)
    print(dijsktra(g, 1))

    """

    #Prunning Route
    route3 =[]
    route4 =[]
    prunnedroute =[]

    Cum_cap = int(capacity())
    maxCapacity = int(input("Enter maximum capacity of a truck:  "))
    with open('PODlist2.csv', 'r+') as in_file:
        OurPOD = csv.reader(in_file)
        has_header = csv.Sniffer().has_header(in_file.read(1024))
        in_file.seek(0)  # Rewind.
        if has_header:
            next(OurPOD)  # Skip header row.

        for row in OurPOD:
            popn.append(row[2])

       # i=0
        #i+=i
        #capacity = popn[i]
        for item in firstcluster:
            if Cum_cap < maxCapacity:
                route1.append(item)
                Cum_cap += Cum_cap
            else:
                route2.append(item)
                Cum_cap += Cum_cap
        print("PODs within route1: ---")
        for item in route1:
            print(item)

        print("PODs within route2: ---")
        for item in route2:
            print(item)

        for item in secondcluster:
            if Cum_cap < maxCapacity:
                route1.append(item)
                Cum_cap += Cum_cap
            else:
                route3.append(item)
                Cum_cap += Cum_cap
        print("PODs within route1: ---")
        for item in route1:
            print(item)

        print("PODs within route2: ---")
        for item in route2:
            print(item)


        #all_routes = route1+route2 + route3 +route4
        for item in route3: #route4

            if Cum_cap > maxCapacity:
                prunnedroute.append(item)
                Cum_cap += Cum_cap

        print("PODs within prunned route, not yet assigned: ---")
        for item in prunnedroute:
            print(item)
    with open('newroutes.csv', 'w') as out_file:
        new_list = csv.writer(out_file)

        webbrowser.open("https://planner.myrouteonline.com/route-planner")


def capacity():
    with open('PODlist2.csv', 'r+') as in_file:
        OurPOD = csv.reader(in_file)
        has_header = csv.Sniffer().has_header(in_file.read(1024))
        in_file.seek(0)  # Rewind.
        if has_header:
            next(OurPOD)  # Skip header row.

        for row in OurPOD:
            popn.append(row[2])
        x =0
        while x < (len(popn)):
            cap = popn[x]
            x +=1
            #print (cap)
            return cap

def dist_cumu():
    with open('PODlist2.csv', 'r+') as in_file:
        OurPOD = csv.reader(in_file)

        distance = 0.0
        distance2 = 0.0
        has_header = csv.Sniffer().has_header(in_file.read(1024))
        in_file.seek(0)  # Rewind.

        if has_header:
            next(OurPOD)  # Skip header row.

        for row in OurPOD:
            x = row[3]
            y = row[4]

            #print(x)
            x =float(x)
            y = float(y)
            x0 = -118.453
            y0 = 34.21

            distance2 += math.sqrt((x - x0)**2 + (y - y0)**2)
            distance = math.sqrt((x - x0)**2 + (y - y0)**2)
    return distance
    #print (distance)


from numpy import array


def List2Graph(input_list):
    connections = []
    directions = [(-1, -1), (0, -1), (1, -1), (1, 0)]
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list[0])):
            for x, y in directions:
                if (i + y >= 0 and i + y < len(input_list) and j + x >= 0 and j + x < len(input_list)):
                    pair = (input_list[i][j])
                    connections.append(pair)
    return connections
    #print( connections)


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distance[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
        print(visited)
        print(path)
    return visited, path




def prune_route():
    # inputs
    routes = input("enter or read")
    weight = input("optimization weight")
    max_duration = input(" Maximum tour duration:")
    total_cap = input("Maximum vehicle capacity")
    pruned_pods = set()
    pruned_routes = []
    new_routes = set()
    for route in range(0, routes.size - 1):
        # put all into a temporary route
        current_cap = input("Current Capacity:")
        current_cap += current_cap
        if current_cap > total_cap:
            pruned_routes.append(route)
    for route in pruned_routes:
        # create a path through all pruned routes

        if duration < max_duration and pruned_cap < total_cap:
            new_routes.add(route)
        maxDistance = 0.0
        routeStartPod = None
        routeEndPod = None
        for POD.startPod in podsCutFromRoute:
            for PodDistanceNode.endPod in startPod.listOfClosestPods:
                if [podsCutFromRoute, endPod.c_podId] in podList:
                    if endPod.c_distanceToPod >= maxDistance:
                        routeStartPod = startPod
                        routeEndPod = c_allPods.get(endPod.c_podId)
                        maxDistance = endPod.c_distanceToPod



def culmulativeDistance(instance, PODs, startIndex, endIndex):
    # Returns the distance between the start and end index of customers.
    # If the customer is at the beginning or end, includes the depot
    distList = distanceList(instance, PODs)

    if startIndex == 0 or endIndex > len(PODs):
        distance = 9999999999999999999
    elif endIndex < len(PODs):
        distance = sum(distList[startIndex:endIndex + 1])
    elif endIndex == len(PODs):
        distance = sum(distList[startIndex:endIndex + 1])
        distance += instance['distance_matrix'][PODs[endIndex - 1]][0]
    return distance


def culmulativeDemand(instance, PODs, startIndex, endIndex):
    # Returns the total demand of the start and end index of customers.
    dmdList = demandList(instance, PODs)
    demand = sum(dmdList[startIndex:endIndex + 1])
    return demand


def demandList(instance, PODs):
    # Use the distance matrix and find the demand of all the
    # customers in the TSP tour
    demand = []
    for customerID in PODs:
        demand.append(instance['PodID_%d' % customerID])
    return demand


def distanceBetweenCustomers(instance, fromCustomer, toCustomer):
    return instance['distance_matrix'][fromCustomer][toCustomer]

def Dijkstra_Shortest_path():

    #print(nx.dijkstra_path_length(G, 0, 4))

    a = np.array(PODList)
    #G = nx.from_numpy_matrix(a)
    G = nx.path_graph(5)
    print(nx.dijkstra_path_length(G, 0, 4))
    print(nx.dijkstra_path(G, 0, 4))
    print([p for p in nx.all_shortest_paths(G, source=0, target=2)])

    Data = open('PODlist4.csv', "r")
    next(Data, None)  # skip the first line in the input file
    Graphtype = nx.DiGraph()

    G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype,
                          nodetype=int, data=(('weight', int),))

    for x in G.nodes():
        print("Node:", x, "has total #degree:", G.degree(x), " , In_degree: ", G.out_degree(x), " and out_degree: ",
              G.in_degree(x))
    for u, v in G.edges():
        print("Weight of Edge (" + str(u) + "," + str(v) + ")", G.get_edge_data(u, v))


def partitionpods(instance, PODs, lightRange=100, lightCapacity=50):
    # The method takes in a TSP tour, the time and capacity constraint
    # Returns a list indicating customers that the light resource
    # is able to deliver to - [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]

    considerList = [False] * len(PODs)  # zero list with length of PODs
    considerList[0] = True
    considerList[-1] = True
    clusterList = [0] * len(PODs)  # zero list with length of PODs
    with open('PODlist2.csv', 'r+') as in_file:
        distanceList= csv.reader(in_file)


        # Determine the order of the distance list
        distList = distanceList(instance, PODs)
        print(distList)
        sortedDistanceList = [0] * len(distList)
        for i, x in enumerate(sorted(range(len(distList)), key=lambda y: distList[y])):
            sortedDistanceList[x] = i

        # Start the cluster with the closest pair and add neighbouring customers until
        # the range or capacity constraint is reached. Then find the next closest pair
        # not part of any cluster and repeat until all customers are considered
        for i in range(len(PODs)):
            considerCustomer = sortedDistanceList.index(i)
            print("consider customer index: %d" % considerCustomer)
            # Determine the neighbouring nodes of the considerCustomer
            # Calculate the distance (include rendezvous)
            if considerCustomer == 0:
                clusterEdgeLocation = [considerCustomer, considerCustomer + 1]
                distance = 99999999999  # don't consider the first customer as light resource deliverable
            elif considerCustomer == (len(PODs) - 1):
                clusterEdgeLocation = [considerCustomer - 1, considerCustomer]
                distance = 99999999999  # don't consider the last customer as light resource deliverable
            else:
                clusterEdgeLocation = [considerCustomer - 1, considerCustomer + 1]
                distance = culmulativeDistance(instance, PODs,
                                           clusterEdgeLocation[0], clusterEdgeLocation[1])

            # Calculate the demand of considerCustomer
            demand = culmulativeDemand(instance, PODs, considerCustomer, considerCustomer)

            # First check if the customer is already considered, range feasibility and demand feasibility
            if (any(considerList[clusterEdgeLocation[0]:clusterEdgeLocation[1] + 1]) == True
                or distance > lightRange or demand > lightCapacity):
                continue
            # Passes all tests, initialize considerCustomer as lightCluster
            else:
                considerList[clusterEdgeLocation[0]:clusterEdgeLocation[1] + 1] = [True] * (
                    clusterEdgeLocation[1] - clusterEdgeLocation[0] + 1)
                clusterList[considerCustomer] = 1

                # Incrementally add the neighbouring customers until the edge of cluster reaches the ends of the list
                # Check range feasibility
                # Check demand feasibility
                while clusterEdgeLocation[0] != 0 or clusterEdgeLocation[1] + 1 != len(PODs):
                    distanceForward = culmulativeDistance(instance, PODs,
                                                      clusterEdgeLocation[0], clusterEdgeLocation[1] + 1)
                    distanceBackward = culmulativeDistance(instance, PODs,
                                                       clusterEdgeLocation[0] - 1, clusterEdgeLocation[1])
                    demandForward = culmulativeDemand(instance, PODs,
                                                  clusterEdgeLocation[0] + 1, clusterEdgeLocation[1])
                    demandBackward = culmulativeDemand(instance, PODs,
                                                   clusterEdgeLocation[0], clusterEdgeLocation[1] - 1)
                    print(
                        "Demand from %d to %d is: %d" % (clusterEdgeLocation[0] + 1, clusterEdgeLocation[1], demandForward))
                    print("Demand from %d to %d is: %d" % (
                        clusterEdgeLocation[0], clusterEdgeLocation[1] - 1, demandBackward))
                    print("Range is: %d and %d" % (distanceForward, distanceBackward))

                    # Greedy approach: look at the shortest distance neighbouring node to add to cluster
                    # If neighbouring node successfully pass the demand and time constraint
                    # Update the cluster list and the consider list
                    # Also check if there is a space for light resource to rendezvous
                    if (
                        distanceForward <= distanceBackward and distanceForward < lightRange and demandForward < lightCapacity
                        and clusterList[clusterEdgeLocation[1] + 1] == False):
                        considerList[clusterEdgeLocation[0] + 1:clusterEdgeLocation[1] + 1] = [True] * (
                            clusterEdgeLocation[1] - clusterEdgeLocation[0])
                        clusterList[clusterEdgeLocation[0] + 1:clusterEdgeLocation[1] + 1] = [1] * (
                            clusterEdgeLocation[1] - clusterEdgeLocation[0])
                        clusterEdgeLocation[1] = clusterEdgeLocation[1] + 1
                        print("Cluster forwards is added")
                    elif (distanceForward > distanceBackward) and (distanceBackward < lightRange) and (demandBackward < lightCapacity)and (clusterList[clusterEdgeLocation[0] - 1] == False):
                        considerList[clusterEdgeLocation[0]:clusterEdgeLocation[1]] = [True] * (
                                clusterEdgeLocation[1] - clusterEdgeLocation[0])
                        clusterList[clusterEdgeLocation[0]:clusterEdgeLocation[1]] = [1] * (
                            clusterEdgeLocation[1] - clusterEdgeLocation[0])
                        clusterEdgeLocation[0] = clusterEdgeLocation[0] - 1
                        print("Cluster backwards is added")
                    else:
                        break
                    print(clusterList)
                    print("The cluster edge is at: %d and %d" % (clusterEdgeLocation[0], clusterEdgeLocation[1]))
        return clusterList

def calc_distances(p0, points):
    pd.to_numeric(p0.float[0])
    return ((p0- points)**2).sum(axis=1)

with open('PODlist2.csv', 'r+') as in_file:
    OurPOD2 = csv.reader(in_file)

    has_header = csv.Sniffer().has_header(in_file.read(1024))
    in_file.seek(0)  # Rewind.

    if has_header:
        next(OurPOD2)  # Skip header row.

    PODList2 = list(OurPOD2)
def graipher(pts,K):

    farthest_pts = np.zeros((K, 4))
    farthest_pts[0] = pts[np.random.randint(len(pts))]
    distances = calc_distances(farthest_pts[0], pts)
    #distances = dist_cumu()
    for i in range(1, K):
        farthest_pts[i] = pts[np.argmax(distances)]
        distances = np.minimum(distances, calc_distances(farthest_pts[i], pts))
        #distances = np.minimum(distances, dist_cumu(), pts)

N, P = 80, 40
pts = np.random.random_sample((N,25))
#farthest_pts = op(pts, N, P)

two_phase()
 getConnections(PODList)
#partitionpods(PODList, PODList[0], lightRange=100, lightCapacity=50)
#prune_route()
#List2Graph(PODList)
#maxDepth(PODList)
#Dijkstra_Shortest_path()
#demandList(PODList[0], PODList)
#graipher(PODList2, P)
#capacity()