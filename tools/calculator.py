from collections import deque


def get_priority(op):
    if op in "*/":
        return 5
    elif op in "+-":
        return 3
    elif op == "(":
        return 1
    else:
        return -1


def infix_to_postfix(infix):
    postfix, stack = [], deque()

    for token in infix:
        if token.isdigit():
            postfix.append(token)
        else:
            if token == "(":
                stack.append("(")
            elif token == ")":
                while (top := stack.pop()) != "(":
                    postfix.append(top)
            else:
                while stack and get_priority(stack[-1]) >= get_priority(token):
                    postfix.append(stack.pop())
                stack.append(token)
    while stack:
        postfix.append(stack.pop())

    return postfix


def calculator(infix):
    stack = []
    for token in infix_to_postfix(infix):
        if token.isdigit():
            stack.append(int(token))
        else:
            num1, num2 = stack.pop(), stack.pop()
            if token == "+":
                stack.append(num1 + num2)
            elif token == "-":
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(num1 * num2)
            else:
                stack.append(num1 // num2)
    return stack.pop()


print(calculator("2+4*5+3"))
