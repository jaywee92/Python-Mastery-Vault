import matplotlib.pyplot as plt
def _show_or_save(fig, title="plot"):
    # In Obsidian execute-code, plots are embedded when plt.show() is called.
    # We avoid saving files here to honor "show-only" behavior.
    plt.show()
    try:
        plt.close(fig)
    except Exception:
        pass

def draw_array(values, highlight_index=None, title="Array"):
    xs = list(range(len(values)))
    colors = ["#4C78A8"] * len(values)
    if highlight_index is not None and 0 <= highlight_index < len(values):
        colors[highlight_index] = "#F58518"
    plt.figure(figsize=(6, 2))
    plt.bar(xs, values, color=colors)
    plt.xticks(xs)
    plt.title(title)
    plt.tight_layout()
    _show_or_save(plt.gcf(), title)

def draw_stack(values, title="Stack (top on right)"):
    xs = list(range(len(values)))
    plt.figure(figsize=(6, 2))
    plt.bar(xs, [1]*len(values), color="#54A24B")
    for i, v in enumerate(values):
        plt.text(i, 0.5, str(v), ha='center', va='center')
    plt.xticks(xs)
    plt.yticks([])
    plt.title(title)
    plt.tight_layout()
    _show_or_save(plt.gcf(), title)

def draw_queue(values, title="Queue (front on left)"):
    xs = list(range(len(values)))
    plt.figure(figsize=(6, 2))
    plt.bar(xs, [1]*len(values), color="#E45756")
    for i, v in enumerate(values):
        plt.text(i, 0.5, str(v), ha='center', va='center')
    plt.xticks(xs)
    plt.yticks([])
    plt.title(title)
    plt.tight_layout()
    _show_or_save(plt.gcf(), title)

def draw_sort(values, title="Sorting Snapshot"):
    xs = list(range(len(values)))
    plt.figure(figsize=(6, 3))
    plt.bar(xs, values, color="#72B7B2")
    plt.xticks(xs)
    plt.title(title)
    plt.tight_layout()
    _show_or_save(plt.gcf(), title)

def draw_search(values, index=None, title="Search"):
    xs = list(range(len(values)))
    colors = ["#4C78A8"] * len(values)
    if index is not None and 0 <= index < len(values):
        colors[index] = "#F58518"
    plt.figure(figsize=(6, 2))
    plt.bar(xs, values, color=colors)
    plt.xticks(xs)
    plt.title(title)
    plt.tight_layout()
    _show_or_save(plt.gcf(), title)

def _plot_node(ax, node, x, y, dx, dy):
    if node is None:
        return
    ax.text(x, y, str(node.value), ha="center", va="center",
            bbox=dict(boxstyle="circle", fc="#f7f7f7", ec="#333333"))
    if getattr(node, 'left', None):
        ax.plot([x, x - dx], [y, y - dy], color="#333333")
        _plot_node(ax, node.left, x - dx, y - dy, dx * 0.6, dy)
    if getattr(node, 'right', None):
        ax.plot([x, x + dx], [y, y - dy], color="#333333")
        _plot_node(ax, node.right, x + dx, y - dy, dx * 0.6, dy)

def draw_tree(root, title="Tree"):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis("off")
    ax.set_title(title)
    _plot_node(ax, root, 0, 0, 1.5, 1.0)
    _show_or_save(plt.gcf(), title)

def draw_graph(adj, title="Graph"):
    # Simple circular layout for small graphs
    import math
    nodes = list(adj.keys())
    n = len(nodes)
    if n == 0:
        return
    coords = {}
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / n
        coords[node] = (math.cos(angle), math.sin(angle))
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.axis("off")
    ax.set_title(title)
    for node, neighbors in adj.items():
        x1, y1 = coords[node]
        for nb in neighbors:
            if nb not in coords:
                continue
            x2, y2 = coords[nb]
            ax.plot([x1, x2], [y1, y2], color="#999999")
    for node, (x, y) in coords.items():
        ax.text(x, y, str(node), ha='center', va='center',
                bbox=dict(boxstyle="circle", fc="#f7f7f7", ec="#333333"))
    _show_or_save(plt.gcf(), title)
