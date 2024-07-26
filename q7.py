# String Stripping and Justifying

# Task: Given the string s, use string methods to:
# Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
# Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
# Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
# s:str ="   Python is fun!   "
# Expected Output:
# Python is fun!
# Python is fun!*****
# *****Python is fun!

s : str = "   Python is fun!   "
print(s.strip())
print(s.strip().ljust(20,'*'))
print(s.strip().rjust(20,'*'))