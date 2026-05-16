import numpy as np
import heapq

def euler83(matrix: np.ndarray) -> int:
    n = matrix.shape[0]

    # afstandsmatrix
    dist = np.full((n, n), np.inf)
    dist[0, 0] = matrix[0, 0]

    # min-heap voor Dijkstra
    pq = [(matrix[0, 0], 0, 0)]

    # 4 richtingen
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    # dirs = [(1,0), (0,1)] # dit zou de code worden voor problem 81

    while pq:
        cost, r, c = heapq.heappop(pq)

        # als we een slechter pad poppen → skip
        if cost > dist[r, c]:
            continue

        # doel bereikt
        if r == n-1 and c == n-1:
            return int(cost)

        # buren
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                new_cost = cost + matrix[nr, nc]
                if new_cost < dist[nr, nc]:
                    dist[nr, nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

    return int(dist[n-1, n-1])

matrix = np.loadtxt("problem81.txt", delimiter=",", dtype=int)
print(euler83(matrix))
