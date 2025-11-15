#Advent of Code 2015: Day 5

#function for part 1
def is_nice_part1 (file_input):

    file = open(file_input).read().splitlines()

    vowels = 'aeiou'
    nice_count = 0

    for line in file:
        v_count = 0
        double_letter = False
        forbidden = False

        #check for vowels and count them 
        for char in line:
            if char in vowels:
                v_count += 1
        
        #check for double letters
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                double_letter = True
        
        #check for forbidden strings
        forbidden_strings = ['ab', 'cd', 'pq', 'xy']
        for fs in forbidden_strings:
            if fs in line:
                forbidden = True

        #determine if the string is nice
        if v_count >= 3 and double_letter and not forbidden:
            nice_count += 1
    
    return nice_count

#function for part 2
def is_nice_part2(file_input):

    file = open(file_input).read().splitlines()

    nice_count = 0

    for line in file:
        pair_repeat =  False
        repeat_with_one_between = False

        #check for pair that appears at least twice (no overlap)
        for i in range(len(line)-1):
            pair = line[i:i+2]
            if pair in line[i+2:]:
                pair_repeat = True
                break

        #check for repeat with one letter between
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                repeat_with_one_between = True
                break

        if pair_repeat and repeat_with_one_between:
            nice_count += 1
    
    return nice_count


#main function
def main():

    input_file = 'day5input.txt'

    result1 = is_nice_part1(input_file)
    result2 = is_nice_part2(input_file)

    print("Part 1 nice strings:", result1)
    print("Part 2 nice strings:", result2)

main()
