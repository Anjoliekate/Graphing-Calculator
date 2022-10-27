from graphics import *
from stack import Stack


def PrintDirections():
    print("Hello", "welcome to the newest generation graphing calculator program. To start please enter a function you would like to calculate. ")
    print("Valid expressions consists of single digit integers, the variable x, the operators +, -, /, and *, and parenthesis.")

def EvaluatePostfix(postfix, x):
    s = Stack()
    for c in postfix:
        if c in "0123456789":
            s.Push(float(c))
        elif c == "x":
            s.Push(x)

        elif c == "+":
            rhs = s.Pop()
            lhs = s.Pop()
            answer = lhs + rhs
            s.Push(answer)

        elif c == "-'":
            rhs = s.Pop()
            lhs = s.Pop()
            answer = lhs - rhs
            s.Push(answer)

        elif c == "*":
            rhs = s.Pop()
            lhs = s.Pop()
            answer = lhs * rhs
            s.Push(answer)

        elif c == "/":
            rhs = s.Pop()
            lhs = s.Pop()
            answer = lhs / rhs
            s.Push(answer)

    return s.Pop()


def InfixToPostfix(infix):
    postfix = ""
    s = Stack()
    for c in infix:

        if c in "1234567890":
            postfix += c

        elif c == 'x':
            postfix += c

        elif c in "+-":
            while not s.IsEmpty() and s.Top() in "*/+-":
                postfix += s.Pop()
            s.Push(c)

        elif c in "*/":
            while not s.IsEmpty() and s.Top() in "*/":
                postfix += s.Pop()
            s.Push(c)

        elif c == "(":
            s.Push(c)

        elif c == ")":
            while s.Top() != "(":
                postfix += s.Pop()
            s.Pop()

    while not s.IsEmpty():
        postfix += s.Pop()

    return postfix


def main():

    PrintDirections()
    infixFunction = input("Enter your function here(ex: x*x): ")
    print(infixFunction)
    postfixFunction = InfixToPostfix(infixFunction)
    print(postfixFunction)

    win = GraphWin("My Graphing Calculator", 600, 600)
    
    XLOW = -10
    XHIGH = +10
    YLOW = -10
    YHIGH = +10
    XINC = .01
    

    win.setCoords(XLOW, YLOW, XHIGH, YHIGH)

    x = XLOW
    print(XLOW)

    while x < XHIGH:
        y = EvaluatePostfix(postfixFunction, x)
        x2 = x + XINC
        y2 = EvaluatePostfix(postfixFunction, x2)
        line = Line(Point(x,y), Point(x2,y2))
        line.draw(win)
        x+=XINC
    win.getMouse()
    win.close()


main()
