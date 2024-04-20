def isValid(s):
    pairs = {")":"(", "]":"[", "}":"{"}
    stack = []
    for i in s:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs:
            if not stack or stack[-1] != pairs[i]: #if there is no opening bracket in stack ---> false; if last element not equal its pair bracket -->false
                return False
            stack.pop() #remove top element from stuck because its matching closing bracket has been found
        else:
            pass # if it is not brackets(whitespace or smth else), ignore
    return not stack #if stuck is empty at the end --> True, means all opening brackets were matched; if not empty  --> False