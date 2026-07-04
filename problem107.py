import numpy as np
from collections import deque


def read_file_numpy_fast(filepath):
    data = np.genfromtxt(
        filepath,
        delimiter=",",
        dtype=float,
        missing_values="-",
        filling_values=np.nan
    )
    return data


def is_graph_connected(adj):
    n = adj.shape[0]
    start = 0
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        neighbors = np.where(~np.isnan(adj[node]))[0]

        for nb in neighbors:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)

    return len(visited) == n


def reverse_delete_mst(adj):
    # Maak een lijst van alle edges (i, j, weight)
    edges = []
    n = adj.shape[0]

    for i in range(n):
        for j in range(i + 1, n):
            if not np.isnan(adj[i, j]):
                edges.append((i, j, adj[i, j]))

    # Sorteer edges van groot → klein
    edges.sort(key=lambda x: x[2], reverse=True)

    original_sum = np.nansum(adj)

    for (i, j, w) in edges:
        # Verwijder edge
        adj[i, j] = np.nan
        adj[j, i] = np.nan

        # Check of graaf nog connected is
        if not is_graph_connected(adj):
            # Edge was nodig → terugplaatsen
            adj[i, j] = w
            adj[j, i] = w

    mst_sum = np.nansum(adj)
    saving = original_sum - mst_sum

    return adj, mst_sum, saving


if __name__ == '__main__':
    network_np = read_file_numpy_fast('problem107.txt')

    mst, mst_sum, saving = reverse_delete_mst(network_np)

    print(f"MST totale waarde: {mst_sum}")
    print(f"Besparing t.o.v. origineel: {saving/2}") # de graph is symmetrisch, dus delen door 2 om dubbele telling te vermijden
    
