######################################################

#   Solved on Monday, 14 - 03 - 2022.

######################################################


######################################################

#   Runtime: 40ms   -   70.16%
#   Memory: 13.8MB  -   99.13%

######################################################

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Stack to store directory names of the given path
        pathComponents = []
        # Initialising with 1 since given that path[0] will always be "/"
        index = 1
        # Traversing the path
        while index < len(path):
            # Stores the directory name between "/" and "/"
            curr = ""
            # If we have "/" at index
            if path[index] == "/":
                # We just have to omit it. So increasing index by 1
                index += 1
            else:
                # If index  != "/" there are 3 possibilities
                # a) Having a single ".". In this case we have to just omit it
                # b) Having "..". In this case we have to go back 1 directory
                # which can be done by popping last directory from pathComponents
                # c) Having a directory name. In this case we have to add it to
                # pathComponenets
                while index < len(path) and path[index] != "/":
                    # Looping till we reach "/" or end of string and adding chars to
                    # curr
                    curr += path[index]
                    index += 1
                # b) case. If pathComponents is empty, that means we are at root directory
                # In OS, parent of root will be root only. So no need to pop.
                if curr == "..": 
                    if len(pathComponents) != 0: pathComponents.pop()
                # a) case. Omit it
                elif curr == ".": continue
                # c) case. Add it to pathComponents
                else: pathComponents.append(curr)
        # Joining all the strings present in pathComponents separated by "/"
        # Since we need "/" at start, adding it at the beginning and returning it
        return "/" + "/".join(pathComponents)