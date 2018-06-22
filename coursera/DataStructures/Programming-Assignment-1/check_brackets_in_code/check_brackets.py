# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position
    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def PopFront(stack):
    if len(stack)==0:
        return
    return stack.pop(0)

def BracketChecker(text):
    opening_brackets_stack = []
    count=0
    # print(text,", ", len(text))
    for i, next in enumerate(text):
        # print("i'm enumerating")
        count+=1
        # print("i: ",i)
        if next == '(' or next == '[' or next == '{':
            # print("next is an opening bracket: ",next)
            b=Bracket(next,i+1)
            opening_brackets_stack.insert(0,b)
        elif next == ')' or next == ']' or next == '}':
            # print("next is a closing bracket: ",next)
            if len(opening_brackets_stack)==0:
                # print("len(opening_brackets_stack) was 0")
                return i+1
            top=PopFront(opening_brackets_stack)
            # print("top: ",top.bracket_type,", next: ",next)
            if (top.bracket_type=='(' and next!=')') or (top.bracket_type=='[' and next!=']') or (top.bracket_type=='{' and next!='}'):
                return i+1
    if len(opening_brackets_stack)==0:
        return "Success"
    return opening_brackets_stack[0].position

if __name__ == "__main__":
    text = input()
    print(BracketChecker(text))
