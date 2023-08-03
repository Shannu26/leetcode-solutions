######################################################

#   Solved on Thursday, 24 - 03 - 2022.

######################################################


######################################################

#   Runtime: 460ms   -   91.40%
#   Memory: 20.8MB  -   80.59%

######################################################

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
            Logic is, first we sort people according to their weights
            Constraints given are 
                Atmost 2 people can travel per boat
                Weight of people on boat should be <= limit
            We will use 2 pointer approach: left and right of list
            Since we are sorting the list, if heavy person at right index
            can't sit together in a boat with left index person no one else can sit 
            with him, since left index person is the person with least weight. So heavy
            person will get a single boat for himself.
                In this case, we reduce right pointer by 1
            Else, light person and heavy person can sit in one boat. In other words
            light person can sit with any person from left to right since right person
            is the heaviest and he can sit with him too. If light person can sit with
            anyone, then he might as well pair with heaviest person itself
                In this case we increase left pointer by 1 and reduce right pointer
                by 1
            For both the above cases, we are using a boat. So, we increase boats count
            by 1
        """
        # Sorting the list
        people.sort()
        minBoats = 0
        left = 0
        right = len(people) - 1
        # Looping
        while left <= right:
            minBoats += 1
            # Case 2 involves increase of left pointer too, in addition to reducing
            # right pointer
            if people[left] + people[right] <= limit:
                left += 1
            # Since case 1 and 2 involves reducing right pointer
            right -= 1
        
        return minBoats