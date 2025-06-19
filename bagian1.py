def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result is not None:
                return result

    path.pop()
    return None

graph = {
    'Bandar Lampung': ['Metro', 'Pringsewu'],
    'Metro': ['Jambi', 'Pringsewu'],
    'Pringsewu': ['Jambi'],
    'Jambi': [],
}

start_node = 'Bandar Lampung'
goal_node = 'Jambi'
result = dfs(graph, start_node, goal_node)

if result:
    print(f"Jalur dari {start_node} ke {goal_node}: {' -> '.join(result)}")
else:
    print(f"Tidak ada jalur dari {start_node} ke {goal_node}.")
