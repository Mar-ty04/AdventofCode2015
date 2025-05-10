#Advent of Code 2015: Day 1 

#function for part 1:
def wrapping_paper(file_input):

    file = open(file_input).read().splitlines() 
    total_square_feet = 0

    for dimensions in file:
        length, width, height = sorted(map(int, dimensions.split("x")))

        total_square_feet += 2 * length * width + 2 * width * height + 2 * length * height + length * width 

    return total_square_feet

#function for part 2: 
def ribbion_required(file_input):

    file = open(file_input).read().splitlines()
    total_ribbion_needed = 0

    for dimensions in file:
        length, width, height = sorted(map(int, dimensions.split("x")))

        total_ribbion_needed += 2 * (length + width) + (length * width * height)

    return total_ribbion_needed

#main function
def main():

    input_txt = "input.txt"
    total_wrapping_needed = wrapping_paper(input_txt)
    total_ribbion_needed = ribbion_required(input_txt)

    print(f"The elves need {total_wrapping_needed} square feet of wrapping paper.")
    print(f"The elves need {total_ribbion_needed} feet of ribbon.")

main() 

