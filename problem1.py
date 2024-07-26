from collections import deque, defaultdict

def topological_sort(vertices, edges):
    in_degree = {v: 0 for v in vertices}
    adj_list = defaultdict(list)
    
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1
    
    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []
    
    while queue:
        current = queue.popleft()
        topo_order.append(current)
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return topo_order

def calculate_times(tasks, durations, dependencies):
    adj_list = defaultdict(list)
    reverse_adj_list = defaultdict(list)
    for u, v in dependencies:
        adj_list[u].append(v)
        reverse_adj_list[v].append(u)
    
    topo_order = topological_sort(tasks, dependencies)
    
    EST = {task: 0 for task in tasks}
    EFT = {task: 0 for task in tasks}
    
    for task in topo_order:
        for neighbor in adj_list[task]:
            EST[neighbor] = max(EST[neighbor], EFT[task])
        EFT[task] = EST[task] + durations[task]
    
    max_eft = max(EFT.values())
    LFT = {task: max_eft for task in tasks}
    LST = {task: 0 for task in tasks}
    
    for task in reversed(topo_order):
        for neighbor in reverse_adj_list[task]:
            LFT[task] = min(LFT[task], LST[neighbor])
        LST[task] = LFT[task] - durations[task]
    
    return max(EFT.values()), max(LFT.values())

# Example usage
tasks = ['A', 'B', 'C', 'D', 'E']
durations = {'A': 3, 'B': 2, 'C': 4, 'D': 2, 'E': 1}
dependencies = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]

earliest_completion, latest_completion = calculate_times(tasks, durations, dependencies)

print(f"Earliest completion time: {earliest_completion}")
print(f"Latest completion time: {latest_completion}")

'''
Time Complexity: 
O(V+E)
Space Complexity: 
O(V+E)
'''