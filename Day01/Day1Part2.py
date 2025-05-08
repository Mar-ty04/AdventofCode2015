
string_input = open("input.txt").read().strip()

floor_num = 0 
index = 0

for char in string_input:
    index += 1
    if char == "(":
        floor_num += 1
        
    elif char == ")":
        floor_num -= 1
        
    if floor_num == -1:
        break

print(f"Santa entered the basement at character position {index}.")
