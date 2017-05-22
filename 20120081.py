from collections import deque


n, m, v = map(int, input().split())
edges = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    edges[v1][v2] = edges[v2][v1] = 1

def get_result(dfs=True):
    visited = set()
    visits = []
    buf = deque()
    buf.append(v)
    while len(visited) != n:
        v1 = buf.pop() if dfs else buf.popleft()
        if v1 in visited:
            continue
        visited.add(v1)
        visits.append(str(v1))
        v1_edges = list(enumerate(edges[v1]))
        if dfs:
            v1_edges.reverse()
        for i, v2 in v1_edges:
            if v2:
                buf.append(i)
    return visits

print(' '.join(get_result(True)))
print(' '.join(get_result(False)))
