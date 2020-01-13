import networkx as nx
import matplotlib.pyplot as plt
from generation import GraphGen
from dijkstra import Dijkstra

# Json File's name
json_file = ""
# Data fetch from the Json File
data = []
# Parsed data
ville = ["Agen", "Toulouse", "Bordeaux", "Paris", "Marseille",
         "Lille", "Soubran", "Pau", "Rennes", "Reims", "Rouen", "Metz",
         "Luxembourg", "Milan", "Berlin", "Dortmund", "Zurich", "Londres", "Brussels"]

G = nx.Graph()

gen = GraphGen(1, 10)

#Generate a random graph
gen.gen_method("cities", G, json=ville)
sdeb = "Agen"
sfin = "Brussels"

"""
gen.gen_method("test_sample_1", G)
sdeb = "1"
sfin = "6"
"""

"""
gen.gen_method("test_sample_2", G, json=ville)
sdeb = "Agen"
sfin = "Metz"
"""


#dijkstra algorithm call
sol = Dijkstra()
print("Path : " + str(sol.dijkstra_main(G, sdeb, sfin)))


# Draw & Show Graph #

pos = nx.spring_layout(G)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 5]

# nodes
nx.draw_networkx_nodes(G, pos, node_size=200)
# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge,
                       width=3, alpha=0.5, edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=esmall,
                       width=3, alpha=0.5, edge_color='b')
# labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()



