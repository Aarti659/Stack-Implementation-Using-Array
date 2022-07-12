class Node:
    def __init__(self, Data=None, next=None):
        self.Data = Data
        self.next = next


class Stack:

    def __init__(self):
        self.top = None


    def push(self, Data):
        if self.top is None:
            self.top = Node(Data, None)
            return
        self.top = Node(Data, self.top)


    def pop(self):
        if self.top is None:
            return
        temp = self.top
        if self.top is not None:
            self.top = self.top.next
        temp.next = None
        return temp.Data

    def peek(self):
        return self.top.Data


    def clearstack(self):
        self.top = None


    def emptystack(self):
        if self.top is None:
            return True
        return False


    def display(self):
        ITR = self.top
        sstr = ' '
        while ITR:
            sstr += str(ITR.Data) + '-->'
            ITR = ITR.next
        print(sstr)


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(40)
    stack.peek()
    stack.display()
    stack.pop()
    stack.push(30)
    stack.display()
    stack.clearstack()
    stack.display()




