from src.tools.loader import load_data
from collections import defaultdict
from itertools import combinations
import networkx as nx

TESTING = False


def parse_input(data):
    computers = set()
    connections = defaultdict(set)
    for line in data:
        a, b = line.split("-")
        computers.add(a)
        computers.add(b)
        connections[a].add(b)
        connections[b].add(a)
    return computers, connections


if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    computers, connections = parse_input(data)

    list_of_three_sets = []
    set_of_three_tuples = set()

    for computer in computers:
        if computer.startswith("t"):
            for a, b in combinations(computers, 2):
                if a != computer and b != computer and a != b:
                    if a in connections[b] and b in connections[computer] and computer in connections[a]:
                        if set([a, b, computer]) not in list_of_three_sets:
                            list_of_three_sets.append(set([a, b, computer]))
                            set_of_three_tuples.add(tuple([a, b, computer]))

    print(len(set_of_three_tuples))

    computers, connections = parse_input(data)
    G = nx.Graph()

    for comp in computers:
        G.add_node(comp)

    set_of_edges = set()
    for line in data:
        a, b = line.split("-")
        set_of_edges.add((a, b))

    for a, b in set_of_edges:
        G.add_edge(a, b)

    iterators = list(nx.find_cliques(G))

    solution = max(iterators, key=len)

    print(solution)
    for a in sorted(solution):
        print(a, end=",")

    print()
