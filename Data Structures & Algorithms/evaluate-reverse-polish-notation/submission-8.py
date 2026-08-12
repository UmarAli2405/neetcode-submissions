class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer = 0
        my_stack = []
        operators = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] in operators:
                top = int(my_stack.pop())
                second = int(my_stack.pop())
                if tokens[i] == '+':
                    answer = top + second
                elif tokens[i] == '-':
                    answer = second - top
                elif tokens[i] == '*':
                    answer = top * second
                elif tokens[i] == '/':
                    answer = int(second / top)
                my_stack.append(answer)
            else:
                my_stack.append(tokens[i])

        return int(my_stack[0])