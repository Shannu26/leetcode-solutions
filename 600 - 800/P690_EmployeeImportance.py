######################################################

#   Solved on Wednesday, 26 - 01 - 2022.

######################################################


######################################################

#   Runtime: 135ms   -   99.96%
#   Memory: 15.4MB  -   89.36%

######################################################

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adjacencyList = {}
        # Converting the employees list into adjacencyList. 
        # Since we don't which employee info is present at which index, it is hard
        # to traverse next employee's list if we use the given employees list
        # Given structure is
        # employees is a list of employees where employee[i] is an object having
        #   employee.id
        #   employee.importance
        #   employee.subordinates: List of ids of his subordinates
        # We convert them into a dictionary having structure
        #   employee.id as key
        #   tuple(employee.importance, employee.subordinates) as value
        for employee in employees:
            adjacencyList[employee.id] = (employee.importance, employee.subordinates)
        # BFS Logic starts here
        # Creating a queue with given start id as the value
        queue = [id]
        totalImportance = 0
        # While there are still elements to visit in queue
        while queue:
            # Geting the next employee id
            id = queue.pop(0)
            # Adding the importance of employee with id to total since he is a
            # direct or indirect subordinate of given employee id
            totalImportance += adjacencyList[id][0]
            # Why we need not check whether we have already visited an id is
            # Given that no employee has more than 1 leader. So, we can either
            # reach an id or we can't. But there is no possibility for reaching
            # an id twice
            for subordinate in adjacencyList[id][1]: queue.append(subordinate)
        
        return totalImportance