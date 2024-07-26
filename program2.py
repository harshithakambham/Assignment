from collections import deque, defaultdict

# Define the friendships as an adjacency list
friends = {
    'Alice': ['Bob'],
    'Bob': ['Alice', 'Janice'],
    'Janice': ['Bob'],
    # Add more friends and relationships here if needed
}

def find_all_friends(name):
    """Return all friends of the given person."""
    return friends.get(name, [])

def find_common_friends(name1, name2):
    """Return common friends of the two given people."""
    friends1 = set(find_all_friends(name1))
    friends2 = set(find_all_friends(name2))
    return list(friends1 & friends2)

def nth_connection(start, end):
    """Return the nth connection between start and end.
    
    If no connection exists, return -1.
    """
    if start == end:
        return 0  # The same person is at 0 connections away
    
    visited = set()
    queue = deque([(start, 0)])
    
    while queue:
        current, distance = queue.popleft()
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for friend in friends.get(current, []):
            if friend == end:
                return distance + 1
            if friend not in visited:
                queue.append((friend, distance + 1))
    
    return -1

# Examples
print("Friends of Alice:", find_all_friends('Alice'))
print("Friends of Bob:", find_all_friends('Bob'))
print("Common friends of Alice and Bob:", find_common_friends('Alice', 'Bob'))
print("Nth connection between Alice and Janice:", nth_connection('Alice', 'Janice'))
print("Nth connection between Alice and Bob:", nth_connection('Alice', 'Bob'))
print("Nth connection between Alice and Charlie:", nth_connection('Alice', 'Charlie'))
''' 
Time complexity:
1.	find_all_friends(name): O(1)O(1)O(1) - Direct lookup in a dictionary.
2.	find_common_friends(name1, name2): O(F1+F2)O(F1 + F2)O(F1+F2), where F1F1F1 and F2F2F2 are the number of friends for name1 and name2.
3.	nth_connection(start, end): O(V+E)O(V + E)O(V+E), where V is the number of vertices (friends) and E is the number of edges (friendships). This is due to the BFS traversal of the graph.
Space Complexity:
1.	find_all_friends(name): O(1)O(1)O(1) - The space used is constant as it only involves storing the list of friends.
2.	find_common_friends(name1, name2): O(F1+F2)O(F1 + F2)O(F1+F2) - Space used for the sets of friends.
3.	nth_connection(start, end): O(V)O(V)O(V) - Space for the visited set and the BFS queue.

'''
