######################################################

#   Solved on Tuesday, 26 - 10 - 2021.

######################################################


######################################################

#   Runtime: 24ms   -   98.81%
#   Memory: 14.1MB  -   85.41%

######################################################


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
            Logic is, we convert pattern string into a numeric string, starting with
            value = 0.
            Then we generate numeric string for each word and check if numeric string 
            of word == pattern. If yes, we added it to result list
        """
        def generateNumericString(word):
            """
                Logic is, we start with value = 0, we loop through the word
                if word[i] is not already visited which is stored in mapping 
                dictionary, we add word[i] to dictionary as key and value as value.
                Then we increment value by 1.
                In each iteration, we add mapping[word[i]] to string. To separate
                each character, we add "+" between them
                Finally we return that string

                Example: word = "abbac", mapping = {}, string = "", value = 0
                "a" not in mapping, so mapping = {"a": 0}, string = "0+", value = 1
                "b" not in mapping, so mapping = {"a": 0, "b": 1}, string = "0+1+",
                value = 2
                "b" in mapping, so mapping = {"a": 0, "b": 1}, string = "0+1+1+",
                value = 2
                "a" in mapping, so mapping = {"a": 0, "b": 1}, string = "0+1+1+0+",
                value = 2
                "c" not in mapping, so mapping = {"a": 0, "b": 1, "c": 2}, 
                string = "0+1+1+0+2+", value = 3

                We return "0+1+1+0+2+"

                For similar pattern, "zcczb", mapping = {}, string = "", value = 0
                "z" not in mapping, so mapping = {"z": 0}, string = "0+", value = 1
                "c" not in mapping, so mapping = {"z": 0, "c": 1}, string = "0+1+",
                value = 2
                "c" in mapping, so mapping = {"z": 0, "c": 1}, string = "0+1+1+",
                value = 2
                "z" in mapping, so mapping = {"z": 0, "c": 1}, string = "0+1+1+0+",
                value = 2
                "b" not in mapping, so mapping = {"z": 0, "c": 1, "b": 2}, 
                string = "0+1+1+0+2+", value = 3

                We return "0+1+1+0+2+".

                So, from above we can say that abbac and zcczb has same pattern
            """
            mapping = {}
            string = ""
            value = 0
            for i in range(len(word)):
                if word[i] not in mapping:
                    mapping[word[i]] = value
                    value += 1
                string += str(mapping[word[i]]) + "+"
            return string
        matches = []
        # Generating numeric string for pattern
        pattern = generateNumericString(pattern)
        for word in words:
            # Generating numeric string for each word.
            patternForWord = generateNumericString(word)
            if pattern == patternForWord: matches.append(word)
        
        return matches