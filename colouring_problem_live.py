"""
Graph Colouring — Practical Session
=====================================
Given a graph and k colours, assign a colour to every node such that no two
adjacent nodes share the same colour.
"""


class Graph:
    """
    Undirected graph with adjacency list and node colouring.
    Colours are integers 1..k. Uncoloured nodes store None.
    """

    def __init__(self, nodes, edges):
        """
        :param nodes: list[int]
        :param edges: list[tuple[int, int]] — undirected pairs
        """
        self.nodes = set(nodes)
        self.edges = {node: set() for node in nodes}
        for u, v in edges:
            self.edges[u].add(v)
            self.edges[v].add(u)
        self.colouring = {node: None for node in nodes}

    # ------------------------------------------------------------------
    # Graph queries
    # ------------------------------------------------------------------

    def get_neighbours(self, node):
        return self.edges[node]

    def get_uncoloured_nodes(self):
        return [node for node, colour in self.colouring.items() if colour is None]

    # ------------------------------------------------------------------
    # Helpers: fill in
    # ------------------------------------------------------------------

    def get_neighbour_colours(self, node):
        """Return the set of colours already used by neighbours of node."""
        out = []

        for adj_node in self.edges[node]:
            if adj_node in self.colouring:
                out.append(self.colouring[adj_node])

        return out

    def is_valid_colour(self, node, colour):
        """True if no neighbour of node is already assigned this colour."""
        return colour not in self.get_neighbour_colours(node)

    def is_fully_coloured(self):
        for node in self.nodes:
            if self.colouring[node] is None:
                return False

        return True


    def is_valid_colouring(self):
        """Check that no two adjacent nodes share a colour."""
        for node in self.nodes:
            if not self.is_valid_colour(node, self.colouring[node]):
                return False

        return True

    def get_plausible_colours(self, node, k):
        """Return all colours 1..k not yet used by any neighbour of node."""
        neighboring_colours = self.get_neighbour_colours(node)
        out = [colour for colour in range(k) if colour not in neighboring_colours]
        
        return out

# ---------------------------------------------------------------------------
# Example graph
# ---------------------------------------------------------------------------

def make_example_graph():
    nodes = [0, 1, 2, 3, 4]
    edges = [
        (0, 1), (0, 2), (0, 3),
        (1, 2),
        (2, 3),
        (4, 0), (4, 2),
    ]
    return Graph(nodes, edges)



# ---------------------------------------------------------------------------
# Exhaustive search
# ---------------------------------------------------------------------------

def solve_exhaustive(graph, k):
    """Try every colour for every node. No pruning, invalid colourings are
    only recorded once the graph is fully coloured. Returns all valid solutions."""

    solutions = []

    def recurse(uncoloured, colouring):

        # Base case: all nodes have been assigned a colour.
        if graph.is_fully_coloured():
            if graph.is_valid_colouring():
                sol = graph.colouring.copy()
                solutions.append(sol)
            return

        # Pick the next node to colour.
        current = uncoloured[0]
        uncoloured_copy = uncoloured.copy()
        uncoloured_copy = uncoloured_copy[1:]

        # Try every colour, valid or not, check constraint at the end.
        for colour in range(k):

            colouring_copy = colouring.copy()
            colouring_copy[current] = colour
            graph.colouring = colouring_copy

            recurse(uncoloured_copy, colouring_copy)


    recurse(graph.get_uncoloured_nodes(), dict(graph.colouring))
    return solutions


# ---------------------------------------------------------------------------
# Backtracking
# ---------------------------------------------------------------------------
def solve_backtracking(graph, k):
    """Try every colour for every node. No pruning, invalid colourings are
    only recorded once the graph is fully coloured. Returns all valid solutions."""

    solutions = []

    def recurse(uncoloured, colouring):

        # Base case: all nodes have been assigned a colour.
        if graph.is_fully_coloured():
            sol = graph.colouring.copy()
            solutions.append(sol)
            return

        # Pick the next node to colour.
        current = uncoloured[0]
        uncoloured_copy = uncoloured.copy()
        uncoloured_copy = uncoloured_copy[1:]

        # Try every colour, valid or not, check constraint at the end.
        for colour in graph.get_plausible_colours(current, k):

            colouring_copy = colouring.copy()
            colouring_copy[current] = colour
            graph.colouring = colouring_copy

            recurse(uncoloured_copy, colouring_copy)


    recurse(graph.get_uncoloured_nodes(), dict(graph.colouring))
    return solutions


if __name__ == "__main__":
    g = Graph([0, 1, 2, 3], [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)])
    solutions_0 = solve_exhaustive(g, 3)
    g = Graph([0, 1, 2, 3], [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)])
    solutions_1 = solve_backtracking(g, 3)
    print(solutions_0)
    print(solutions_1)
