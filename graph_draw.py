"""
graph_draw.py — visualisation helper for the Graph Colouring session.

Usage:
    from graph_draw import draw

    draw(graph)                  # draw current colouring
    draw(graph, title="Step 3")  # with a custom title

Requires matplotlib. Install with: pip install matplotlib
"""

import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# Colour map: matches the COLOUR_NAMES in Graph.
COLOUR_MAP = {
    None: "#d0d0d0",   # uncoloured — light grey
    1:    "#e74c3c",   # Red
    2:    "#3498db",   # Blue
    3:    "#2ecc71",   # Green
    4:    "#f1c40f",   # Yellow
    5:    "#e67e22",   # Orange
}

COLOUR_NAMES = {
    None: "uncoloured",
    1: "Red", 2: "Blue", 3: "Green", 4: "Yellow", 5: "Orange",
}


def _circular_layout(nodes):
    """Place nodes evenly around a circle. Returns {node: (x, y)}."""
    n = len(nodes)
    positions = {}
    for i, node in enumerate(sorted(nodes)):
        angle = 2 * math.pi * i / n
        positions[node] = (math.cos(angle), math.sin(angle))
    return positions


def draw(graph, title="Graph Colouring", pos=None):
    """
    Draw the graph with its current colouring.

    :param graph: The Graph instance to draw.
    :param title: Title shown above the plot.
    :param pos: Optional dict {node: (x, y)} for custom layout.
                Defaults to a circular layout.
    """
    if pos is None:
        pos = _circular_layout(graph.nodes)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=14, pad=16)

    # Draw edges.
    drawn_edges = set()
    for u in graph.nodes:
        for v in graph.get_neighbours(u):
            edge = tuple(sorted((u, v)))
            if edge not in drawn_edges:
                x0, y0 = pos[u]
                x1, y1 = pos[v]
                ax.plot([x0, x1], [y0, y1], color="#aaaaaa", linewidth=1.5, zorder=1)
                drawn_edges.add(edge)

    # Draw nodes.
    for node in graph.nodes:
        x, y = pos[node]
        colour = graph.colouring[node]
        face = COLOUR_MAP.get(colour, "#d0d0d0")
        circle = plt.Circle((x, y), 0.12, color=face, ec="#333333", linewidth=2, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(node), ha="center", va="center",
                fontsize=12, fontweight="bold", zorder=3)

    # Legend showing which colours are in use.
    used_colours = set(graph.colouring.values())
    handles = [
        mpatches.Patch(color=COLOUR_MAP[c], label=COLOUR_NAMES[c])
        for c in sorted(used_colours, key=lambda c: (c is None, c))
    ]
    if handles:
        ax.legend(handles=handles, loc="upper right", framealpha=0.9)

    plt.tight_layout()
    plt.show()


def draw_solution(graph, solution, title="Solution", pos=None):
    """
    Temporarily apply a saved solution dict to the graph and draw it,
    then restore the original colouring.

    :param graph: The Graph instance.
    :param solution: A colouring dict {node: colour} as returned by the solvers.
    :param title: Title shown above the plot.
    :param pos: Optional custom layout.
    """
    original = dict(graph.colouring)
    graph.colouring = dict(solution)
    draw(graph, title=title, pos=pos)
    graph.colouring = original


def draw_all_solutions(graph, solutions, title="All valid colourings", pos=None):
    """
    Draw every solution in a grid of subplots — useful for comparing results.

    :param graph: The Graph instance.
    :param solutions: List of colouring dicts as returned by the solvers.
    :param pos: Optional custom layout.
    """
    n = len(solutions)
    if n == 0:
        print("No solutions to draw.")
        return

    if pos is None:
        pos = _circular_layout(graph.nodes)

    cols = min(3, n)
    rows = math.ceil(n / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 5 * rows))

    # Normalise axes to always be a flat list.
    if n == 1:
        axes = [axes]
    else:
        axes = list(axes.flat)

    drawn_edges = set()
    for u in graph.nodes:
        for v in graph.get_neighbours(u):
            drawn_edges.add(tuple(sorted((u, v))))

    original = dict(graph.colouring)

    for i, solution in enumerate(solutions):
        ax = axes[i]
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(f"Solution {i + 1}", fontsize=11)

        for u, v in drawn_edges:
            x0, y0 = pos[u]
            x1, y1 = pos[v]
            ax.plot([x0, x1], [y0, y1], color="#aaaaaa", linewidth=1.5, zorder=1)

        for node in graph.nodes:
            x, y = pos[node]
            colour = solution[node]
            face = COLOUR_MAP.get(colour, "#d0d0d0")
            circle = plt.Circle((x, y), 0.12, color=face, ec="#333333", linewidth=2, zorder=2)
            ax.add_patch(circle)
            ax.text(x, y, str(node), ha="center", va="center",
                    fontsize=11, fontweight="bold", zorder=3)

    # Hide any unused subplot slots.
    for j in range(n, len(axes)):
        axes[j].set_visible(False)

    graph.colouring = original
    plt.suptitle(title, fontsize=14, y=1.02)
    plt.tight_layout()
    plt.show()