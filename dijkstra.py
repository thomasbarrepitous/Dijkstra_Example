import heapq


class Dijkstra:
    # Heap
    border_nodes = []

    current_node = 0
    previous = {}


    # Main loop
    def dijkstra_main(self, G, sdeb, sfin):
        G = self.initialisation(G, sdeb)

        while True:
            self.lowest_node_search(G)
            G.nodes[self.current_node]['visited'] = True
            (temp, self.current_node) = heapq.heappop(self.border_nodes)

            if((len(self.border_nodes) == 0)):
                break
        return self.path_creation(self.previous, sdeb, sfin)


    # Graph and variables setup
    def initialisation(self, G, sdeb):
        G.nodes[sdeb]['dist'] = 0
        self.current_node = sdeb
        return G


    # Find the lowest node for the self.current_node between each of its neighbor
    def lowest_node_search(self, G):
        # For all the neighbors of the current node
        for n in iter(G[self.current_node]):
            if(G.nodes[n]['visited'] == False):
                self.dist_update(G, n)
                heapq.heappush(self.border_nodes, (G.nodes[n]['dist'], n))


    # Update the distance between the current node and one target node
    def dist_update(self, G, target_node):
        if G.nodes[target_node]['dist'] >= G.nodes[self.current_node]['dist'] + G.edges[target_node, self.current_node]['weight']:
            G.nodes[target_node]['dist'] = G.nodes[self.current_node]['dist'] + \
                G.edges[target_node, self.current_node]['weight']
            self.previous[target_node] = self.current_node
        else:
            G.nodes[self.current_node]['dist'] = G.nodes[target_node]['dist'] + \
                G.edges[target_node, self.current_node]['weight']


    # Recreate the path from the "previous" array
    def path_creation(self, previous, sdeb, sfin):
        path = []
        s = sfin
        while s != sdeb:
            path.append(s)
            s = previous[s]
        path.append(sdeb)
        return path[::-1]
