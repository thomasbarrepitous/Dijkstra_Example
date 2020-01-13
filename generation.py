import networkx as nx
import matplotlib.pyplot as plt
from random import randint, randrange, shuffle


class GraphGen:
    BORNEMIN = 1
    BORNEMAX = 10

    def __init__(self, min, max):
        """Class generator"""
        self.BORNEMIN = min
        self.BORNEMAX = max

    #Generation for test purposes
    def generate_test_sample_1(self, graph):
        for n in range(1, 8):
            graph.add_node(str(n), pos=1, dist=9999, visited=False)
        graph.add_edge("1", "2", weight=3)
        graph.add_edge("1", "7", weight=2)
        graph.add_edge("2", "7", weight=4)
        graph.add_edge("2", "3", weight=2)
        graph.add_edge("3", "4", weight=2)
        graph.add_edge("3", "5", weight=5)
        graph.add_edge("5", "6", weight=1)
        return graph

    #Generation for test purposes
    def generate_test_sample_2(self, graph, cities):
        for n in range(len(cities)):
            graph.add_node(cities[n], pos=(
                randint(1, 1000), randint(1, 1000)), dist=9999, visited=False)
        for i in range(3):
            graph.add_edge(cities[0],cities[i], weight=randint(self.BORNEMIN, self.BORNEMAX))
            graph.add_edge(cities[len(cities)-1],cities[len(cities)-i-1], weight=randint(self.BORNEMIN, self.BORNEMAX))
        for j in range(1, len(cities)-1):
            for k in range(1, len(cities)-1):
               graph.add_edge(cities[j], cities[k], weight=randint(self.BORNEMIN, self.BORNEMAX))
        return graph

    #Graph with each node randomly having between 1 and 4 edges and random weights
    def generate_cities(self, graph, cities):
        for n in range(len(cities)):
            graph.add_node(cities[n], pos=(
                randint(1, 1000), randint(1, 1000)), dist=9999, visited=False)
        for c_node in range(len(cities)):
            for ite in range(randrange(1,3)): 
                while True:
                    target_node = randrange(len(cities))
                    #Avoid self edges and multiple edges on the same nodes
                    if(target_node != c_node and not (graph.has_edge(cities[c_node], cities[target_node]))): break
                graph.add_edge(cities[c_node],cities[target_node], weight=randint(self.BORNEMIN, self.BORNEMAX))
        return graph

    #Switch statement for which generation method to choose
    def gen_method(self, method, graph, **kwargs):
        json = kwargs.get("json", None)
        if(method == "test_sample_1"):
            self.generate_test_sample_1(graph)
        elif(method == "test_sample_2"):
            self.generate_test_sample_2(graph, json)
        elif(method == "cities"):
            while True:
                self.generate_cities(graph, json)
                if nx.is_connected(graph): break
        return graph