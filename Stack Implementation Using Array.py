class StackUsingArray:
    def __init__(self):
        self.stack = []
    def push(self, Element):
        self.stack.append(Element)
    def pop(self):
        if(not self.isEmpty()):
            lastElement = self.stack[-1]
            del(self.stack[-1])
            return lastElement
        else:
            return("Stack Already Empty")

    def isEmpty(self):
        return self.stack == []

    def printStack(self):
        print(self.stack)
if __name__ == "__main__":
    S = StackUsingArray()
    print("*"*5+" Stack Using Array HolyCoders.com "+5*"*")
    while(True):
        el = int(input("1 for Push\n2 for Pop\n3 to check if it is Empty\n4 to print Stack\n5 to exit\n"))
        if(elem == 1):
            item = input("Enter Element to push in stack\n")
            S.push(item)
        if(elem == 2):
            print(S.pop())
        if(elem== 3):
            print(S.isEmpty())
        if(elem == 4):
            S.printStack()
        if(elem == 5):
            break



