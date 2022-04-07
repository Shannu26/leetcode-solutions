######################################################

#   Solved on Tuesday, 22 - 03 - 2022.

######################################################


######################################################

#   Runtime: 32ms   -   98.62%
#   Memory: 14.9MB  -   94.47%

######################################################

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """
            Assume we have n empty in which we have arrange alphabets so that
            their sum is equal to k and the string we get from those slots is 
            the least lexographically possible solution

            To get the least lexographical solution what we can do is, we can start
            filling the slots from the last, so that k value will reduce from last
            slot to first slot.

            If k = 26, we can do "ay" and "z" too. But if n = 2, "ay" is the correct
            solution. So, constraint is we have to definitely use all the slots. So
            lets initally fill all slots with "a". We have filled n slots with "a"
            which has value 1, so we can reduce k by n
                    k -= n

            Now, we can do it without loop if we think the possible ways here.
            Let's say k > 25 where 25 is the value of "y". Why we considered 25
            instead of 26 is, since "a" is already in the slot, we can simply add
            25 to a slot to make it 26 i.e; "z"

            If k > 25, and since already all slots are filled with "a". Let's think
            how many slots can we add extra 25 to already existing 1. The answer is
            k // 25 slots from the end. So we will add 25 to last k // 25 slots

            Now, last k // 25 slots are correctly filled, we have to still fill
            n - (k // 25) slots with k = k % 25 value.

            Now there are 2 possible cases. If k == 0, that means 25 is able to 
            divide k completely. So, in that string there will be only k // 25 "z"s
            and n - (k // 25) "a"s. If k != 0, then we have add that slot after
            filling last k // 25 slots

            Finally we will return string form of that slots
        """
        # Reducing k by n assuming we have filled "a" in all n slots
        k -= n
        # Adding as many "z"s as possible to string
        string = "z" * (k // 25)
        # Changing n and k
        n -= (k // 25)
        k = k % 25
        # If k != 0, we have add that remaining value to (k // 25) + 1 slot from last
        if k != 0: 
            string = chr(k + 97) + string
            # We have filled another slot. So, n -= 1
            n -= 1
        # Filling n slots in the start with a
        string = "a" * n + string
        
        return string