# Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.


anton_name :str ="Anton"
anton_age : int = 21
beth_name : str ="Beth"
beth_age : int = anton_age + 6
chen_name : str ="Chen"
chen_age : int = beth_age + 20
drew_name : str ="Drew"
drew_age : int = chen_age + anton_age
ethan_name : str ="Ethan"
ethan_age : int = chen_age
print(f"{anton_name} is {anton_age}")
print(f"{beth_name} is {beth_age}")
print(f"{chen_name} is {chen_age}")
print(f"{drew_name} is {drew_age}")
print(f"{ethan_name} is {ethan_age}")