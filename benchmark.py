import time
from colouring_problem import Graph, solve_exhaustive, solve_backtracking


def make_benchmark_graph():
    nodes = list(range(8))
    edges = [
        (0, 1), (0, 3), (0, 4),
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 4), (2, 5),
        (3, 4),
        (4, 5), (4, 6),
        (6, 7),
    ]
    return Graph(nodes, edges)


def make_large_graph():
    nodes = list(range(13))
    edges = [
        (0, 1), (0, 2), (0, 3),
        (1, 2), (1, 3), (1, 4),
        (2, 3), (2, 4),
        (3, 4),
        (5, 6), (5, 7), (5, 8),
        (6, 7), (6, 8), (6, 9),
        (7, 8), (7, 9),
        (8, 9),
        (4, 5), (3, 6), (2, 7),
        (0, 10), (1, 10), (10, 11),
        (5, 11), (9, 12), (8, 12), (11, 12),
    ]
    return Graph(nodes, edges)


def run(label, solver, graph, k):
    start = time.perf_counter()
    solutions = solver(graph, k)
    elapsed = time.perf_counter() - start
    print(f"  {label:<30} {len(solutions):>3} solutions   {elapsed:.3f} s")


if __name__ == "__main__":
    K = 4

    print(f"Small graph (8 nodes), k={K}")
    run("Exhaustive",             solve_exhaustive,          make_benchmark_graph(), K)
    run("Backtracking",           solve_backtracking,        make_benchmark_graph(), K)

    print()
    print(f"Large graph (13 nodes), k={K}")
    run("Exhaustive",             solve_exhaustive,          make_large_graph(), K)
    run("Backtracking",           solve_backtracking,        make_large_graph(), K)