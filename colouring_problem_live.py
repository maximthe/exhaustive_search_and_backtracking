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
        pass

    def is_valid_colour(self, node, colour):
        """True if no neighbour of node is already assigned this colour."""
        pass

    def is_fully_coloured(self):
        pass

    def is_valid_colouring(self):
        """Check that no two adjacent nodes share a colour."""
        pass
    
    def get_available_colours(self, node, k):
        """Return all colours 1..k not yet used by any neighbour of node."""
        pass

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
        pass

        # Base case: all nodes have been assigned a colour.

        # Pick the next node to colour.

        # Try every colour, valid or not, check constraint at the end.

    recurse(graph.get_uncoloured_nodes(), dict(graph.colouring))
    return solutions


# ---------------------------------------------------------------------------
# Backtracking
# ---------------------------------------------------------------------------

def solve_backtracking(graph, k):
    """Same structure as exhaustive search, but only tries colours that are
    valid given the current neighbours. Invalid branches are pruned immediately."""

    solutions = []

    def recurse(uncoloured, colouring):
        pass

        # Base case: all nodes have been assigned a colour.

        # Pick the next node to colour.

        # Only try colours that don't conflict with already-coloured neighbours.

    recurse(graph.get_uncoloured_nodes(), dict(graph.colouring))
    return solutions


if __name__ == "__main__":
    from graph_draw import draw, draw_all_solutions
 
    g = make_example_graph()
    draw(g, title="Initial graph, uncoloured")
 
    print("--- Exhaustive ---")
    solutions = solve_exhaustive(g, k=3)
    print(f"Found {len(solutions)} valid colourings.")
    draw_all_solutions(g, solutions, title="Exhaustive — all solutions")
 
    print()
 
    g = make_example_graph()
    print("--- Backtracking ---")
    solutions = solve_backtracking(g, k=3)
    print(f"Found {len(solutions)} valid colourings.")
    draw_all_solutions(g, solutions, title="Backtracking — all solutions")
 