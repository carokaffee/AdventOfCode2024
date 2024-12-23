from src.tools.loader import load_data
from itertools import combinations
import networkx as nx

TESTING = False


def parse_input(data):
    computers = set()
    edges = set()

    for line in data:
        a, b = line.split("-")
        computers.update({a, b})
        edges.add((a, b))

    return computers, edges


def initialize_graph(computers, edges):
    G = nx.Graph()
    G.add_nodes_from(computers)
    G.add_edges_from(edges)
    return G


def find_chief_historian_cliques(G):
    chief_cliques = set()
    for node in [n for n in G.nodes() if n.startswith("t")]:
        for a, b in combinations(G.neighbors(node), 2):
            if G.has_edge(a, b):
                chief_cliques.add(tuple(sorted([a, b, node])))

    return len(chief_cliques)


def find_largest_clique(G):
    cliques = list(nx.find_cliques(G))
    largest_clique = sorted(max(cliques, key=len))
    return ",".join(largest_clique)


if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    computers, edges = parse_input(data)
    G = initialize_graph(computers, edges)

    # PART 1
    # test:      7
    # answer: 1368
    print(find_chief_historian_cliques(G))

    # PART 2
    # test:                              co,de,ka,ta
    # answer: dd,ig,il,im,kb,kr,pe,ti,tv,vr,we,xu,zi
    print(find_largest_clique(G))
