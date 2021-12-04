from stack import Stack

def AreBracketsBalanced(expr):
    if not expr:
        return 'Empty'

    stack = Stack()
    for char in expr:
        if char in ["(", "{", "[", "<"]:
            stack.push(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    stack.push(current_char)
                    break
            if current_char == '{':
                if char != "}":
                    stack.push(current_char)
                    break
            if current_char == '[':
                if char != "]":
                    stack.push(current_char)
                    break
            if current_char == '<':
                if char != ">":
                    stack.push(current_char)
                    break
    if stack.size() == 0:
        return "Balanced"
    else:
        return "Unbalanced"

if __name__ == "__main__":
    string1 = "{[]{()}}"
    print(string1, "-", AreBracketsBalanced(string1))

    string2 = "[{}{})(]"
    print(string2, "-", AreBracketsBalanced(string2))

    string3 = "((()"
    print(string3, "-", AreBracketsBalanced(string3))