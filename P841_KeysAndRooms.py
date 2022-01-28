######################################################

#   Solved on Thursday, 27 - 01 - 2022.

######################################################


######################################################

#   Runtime: 60ms   -   94.94%
#   Memory: 14.3MB  -   99.93%

######################################################

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # If we consider rooms as nodes of a graph and values present in
        # rooms[i] as edges which says that from rooms[i] we can go to rooms[j]
        # we can solve this problem using BFS traversal starting from room 0.
        # Because, while traversing the graph we traverse all the nodes that are
        # possible to reach starting from 0.
        # If number of nodes we traversed == number of rooms that means we can
        # open all rooms. So we return True. Else we return False

        # Queue for BFS
        queue = [0]
        # Set to store already visited room numbers to avoid duplicate traversals
        visited = set()
        # Since, we start at 0, adding it as visited
        visited.add(0)
        numOfRoomsVisited = 0
        
        while queue:
            # Getting the next room
            roomNum = queue.pop(0)
            # We visit that room, so we increase numOfRoomsVisited by 1
            numOfRoomsVisited += 1
            # Getting all the keys in that room
            for room in rooms[roomNum]:
                # If the room to which current key points is not already visited
                if room not in visited:
                    # We consider it as visited and add it queue
                    visited.add(room)
                    queue.append(room)
                    
        return numOfRoomsVisited == len(rooms)