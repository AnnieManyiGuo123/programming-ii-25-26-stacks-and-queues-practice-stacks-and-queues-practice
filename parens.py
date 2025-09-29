def is_balanced(expression):
 stack = []
 
 for char in expression:

  if char == '(':
   # Task: what do we do?
    stack.append('(')
  elif char == ')':
   # Task: what do we do?
    stack.pop()
 
 # Task: how do we know if balanced?

 if len(stack) == 0:
   return True
 else:
   return False 


# Test cases
print(is_balanced("(5 + 3)")) # Should be True
print(is_balanced("((5 + 3)")) # Should be False
print(is_balanced("(5 + (3 * 2))")) # Should be True
