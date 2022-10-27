class Stack:

    def __init__(self):
        self.data = []

    def IsEmpty(self):
        return self.data == []

    def Push(self, item):
        self.data.append(item)
        return

    def Pop(self):
        if self.data == []:
            return False
        return self.data.pop()

    def Top(self):
        return self.data[-1]

   # def append(self, op):
      #  self.Stack.append(str(op))
