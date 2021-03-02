class Solution:
    def calculate(self, s: str) -> int:
        
        # define basic calculation
        def result(operator: str, value2:int, value1:int): # value2 first, because of pop()
            if operator == '*':
                return value1 * value2
            elif operator == '/':
                return value1 / value2
            elif operator == '+':
                return value1 + value2
            elif operator == '-':
                return value1 - value2
        
        # define priority = (number of quotes, priorityMap[operator]) 
        priorityMap = {'+':0, '-':0, '*':1, '/':1}
        
        # init
        values = [] # stack of numbers
        operators = [] # stack of (priority, operator)
        
        value = ''
        countQuotes = 0
        for char in s:
            if char.isdigit():
                value = value + char
                
            elif char in ['+','-','*','/']: # operators
                # check minus sign
                if (char == '-') and (value == ''):
                    value = '0' # add 0 in front of -
                
                # append the last value to stack
                values.append(int(value))
                value = ''
                
                # check operators' priority
                priority = (countQuotes, priorityMap[char])
                while len(operators):
                    if operators[-1][0] >= priority:
                        values.append(result(operators.pop()[1], values.pop(), values.pop()))
                    else:
                        break
                
                # append the new operator to stack
                operators.append((priority, char))
            
            elif char == '(':
                countQuotes += 1
            elif char == ')':
                countQuotes -= 1
            else: # pass for others like space sign ' '
                continue
            
        
        # push the last number on hand to stack
        if len(value):
            values.append(int(value))
            
        # clear stackes
        while len(operators):
            values.append(result(operators.pop()[1], values.pop(), values.pop()))
        
        return values[0]