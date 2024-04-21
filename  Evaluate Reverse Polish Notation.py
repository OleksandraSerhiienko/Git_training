def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = [] #linear data structure that follows the Last In, First Out (LIFO) principle
        operations = {"+", "-", "*", "/"} #set
        for i in tokens:
            if i in operations:
                b = stack.pop() #this line pops the top element from the stack (b) and assigns it to the variable b
                a = stack.pop() #pops the next element from the stack (a) and assigns it to the variable a
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    stack.append(int(float(a)/b)) 
            else:
                stack.append(int(i)) #if i is an integer, not operator, it appends to a stack
        return stack[0] #returns final element from the stack
                