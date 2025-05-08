
string_input = open("input.txt").read().strip()
floor_num = 0


for char in string_input:
    if char == "(":
        floor_num += 1
    if char == ")":
        floor_num -= 1

print(f"Santa is on floor number {floor_num}.")
