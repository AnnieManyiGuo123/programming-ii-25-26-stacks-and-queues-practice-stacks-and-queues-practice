def is_balanced(expression):
 stack = []
 
 for char in expression:
  if char == '(':
   # Task: what do we do?
   pass
 elif char == ')':
   # Task: what do we do?
   pass
 
 # Task: how do we know if balanced?
 return True
# Test cases
print(is_balanced("(5 + 3)")) # Should be True
print(is_balanced("((5 + 3)")) # Should be False
print(is_balanced("(5 + (3 * 2))")) # Should be True
