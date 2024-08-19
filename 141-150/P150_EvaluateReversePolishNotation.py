######################################################

#   Solved on Monday, 11 - 06 - 2023.

######################################################


######################################################

#   Runtime: 68ms   -   82.55%
#   Memory: 14.24MB  -   100.00%

######################################################

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
            The logic is to use a stack to store numbers.
            When we see something other than number, we pop
            twice to get numbers on which we need to apply this
            operation, apply that operation and we push the result
            back onto stack.
            At the end of execution, stack has only 1 value which is the
            result of the expression
        """
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = 0

                if token == "+": result = operand1 + operand2
                elif token == "-": result = operand2 - operand1
                elif token == "*": result = operand1 * operand2
                else: result = int(operand2 / operand1)

                stack.append(result)
            else: stack.append(int(token))
        
        return stack[-1]