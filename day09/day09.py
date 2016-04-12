#!/usr/bin/env python3

class Edge:
    def __init__(self, start_city, end_city, distance):
        self.start_city = start_city
        self.end_city = end_city
        self.distance = distance

class Graph:
    def __init__(self, edges, cities):
        self.edges = edges
        self.cities = cities
        self.global_distance = -1

    def get_distance(self, comparison_func):
        self.comparison_func = comparison_func 
        for city in self.cities:
            new_cities = list(self.cities)
            new_cities.remove(city)
            self.recursive_choose(0, city, new_cities, self.edges)
        return self.global_distance

    def recursive_choose(self, total, current_city, cities, edges):
        if len(edges) == 0:
            if self.global_distance == -1 or self.comparison_func(total, self.global_distance): 
                self.global_distance = total
            return

        for edge in edges:
            if edge.start_city == current_city or edge.end_city == current_city:
                if (edge.start_city == current_city): 
                   new_city = edge.end_city
                else: 
                   new_city = edge.start_city

                distance = edge.distance
                new_cities = list(cities)
                new_cities.remove(new_city)
                new_edges = list(edges)
                 
                for new_edge in edges:
                    if new_edge.start_city == current_city or new_edge.end_city == current_city:
                        new_edges.remove(new_edge)
            
                self.recursive_choose(total + distance, new_city, new_cities, new_edges)

def greater_than(a, b):
    if (a > b): return True

def less_than(a, b):
    if (a < b): return True

edges = []
cities = []

with open("input_day09.txt", "r") as fin:
    for line in fin.readlines():
        fields = line.split()
        edge = Edge(fields[0], fields[2], int(fields[4]))
        edges.append(edge)
        if fields[0] not in cities: cities.append(fields[0])
        if fields[2] not in cities: cities.append(fields[2])
 
city_graph = Graph(edges, cities)
print("Shortest distance: %d" % city_graph.get_distance(less_than))
print("Longest distance: %d" % city_graph.get_distance(greater_than))
