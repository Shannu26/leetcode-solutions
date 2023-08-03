######################################################

#   Solved on Monday, 24 - 01 - 2022.

######################################################


######################################################

#   Runtime: 24ms   -   94.51%
#   Memory: 14.1MB  -   97.80%

######################################################

class Solution:
    def solveEquation(self, equation: str) -> str:
        # values stores the constant and x values after solving the equation
        # Example: 2x = 10
        # values[0] will be 10 and values[1] will be 2
        values = [0, 0]
        # Pointer to determine which index in values we have to update.
        # if isX = 0 we will change constant value
        # if isX = 1 we will change x coefficient
        isX = 0
        # Pointer to traverse the equation from the end
        index = -1
        # When we move a value from left side of = to right side, its value will
        # change from + to - or - to +. Initially sign will be +. So sign = 1
        sign = 1
        # value determines the value we need to add to values array. We initialize
        # with 1 because consider "1 + x = 10". Here for x there is not coefficient
        # before it, but we know that it has coefficient 1 if nothing is specified
        # For that case, we initialized with 1
        value = 1
        # Traversing equation from end to start
        while index >= -len(equation):
            # If index value is x then if we have some digits to its left they are
            # x's coefficients. So we change isX to 1
            if equation[index] == 'x':
                isX = 1
            # If index value is digit, we will loop till we find a char which is not
            # a digit
            if equation[index].isdigit():
                value = ""
                while index >= -len(equation) and equation[index].isdigit(): 
                    value = equation[index] + value
                    index -= 1
                value = int(value)
                # Why we increase index by 1 is above loop breaks when we encounter
                # a non digit value. Since we decrease index by 1 at end of outer loop
                # char at index will go unchecked. So, we increase index by 1 so that
                # in next iteration index will be this char position
                index += 1
            # If index value is + we just have to add the value multiplied by sign to
            # required values position using isX
            # Then we change isX and value to default values to avoid next iterations
            # ambiguity
            if equation[index] == '+':
                values[isX] += sign * value
                isX = 0
                value = 1
            # If index value is - we  have to subtract the value multiplied by sign to
            # required values position using isX
            # Then we change isX and value to default values to avoid next iterations
            # ambiguity
            if equation[index] == '-':
                values[isX] += -1 * sign * value 
                isX = 0
                value = 1
            # If index value is =
            if equation[index] == "=":
                # We will change values at index isX with sign * value only when 
                # char to right of = is not + or -. Because, if right char is + or -
                # value to their right is already added to values list and value and
                # isX are set to default values. If we again change values now, a
                # wrong 1 is added to constant i.e; values[isX]. So, to avoid it
                # we are using this check
                if equation[index + 1] not in ("+", "-"): values[isX] += sign * value
                # Setting isX and value to default
                isX = 0
                value = 1
                # Since we encountered =, we move all chars to its left to right to make
                # equation from equation1 = equation2 to 0 = equation2 - equation1
                # For that we need to multiply chars to left of = by -1. So we are changing
                # sign to -1
                sign = -1
            index -= 1
        # After traversing the equation ends, if first char is + or -, last number
        # is already added to values array. If not it is not added. To add it we add
        # these check
        if equation[0] not in ("+","-"): values[isX] += sign * value
        # If x == 0
        if values[1] == 0:
            # If constant is also 0, we can have infinite solution right. So, we
            # return it
            if values[0] == 0: return "Infinite solutions"
            # If constannt is not 0, we can't get constant from 0, so we return 
            # No solution
            else: return "No solution"
        # If above condition is not true, final equation will be like
        #   values[1] * x + values[0] = 0
        #   => values[1] * x = -1 * values[0]
        #   => x = -1 * values[0] // values[1]
        # So, we return it
        else: return "x=" + str(-1 * values[0] // values[1])
