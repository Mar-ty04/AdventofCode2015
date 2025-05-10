#Advent of Code 2015: Day 04

import hashlib

#function for part 1 (we use the same one for part 2 due to how we implemented it)
def smallest_positive_number(secret_key, leading_zeros_amount):

    #adding 0s to our string based on how much user puts
    leading_zeros = "0" * leading_zeros_amount

    number = 0

    #having our hash input be our secret key and amount of zeroes comibined as per the prompt
    hash_input = f"{secret_key}{number}"
    #using our library to encode it and then hash it with md5 and have it result in a hexadecimal
    md5_hashinput = hashlib.md5(hash_input.encode()).hexdigest()

    while not md5_hashinput.startswith(leading_zeros):

        #keep increasing our number until we finally find the smallest positive number to make it true
        number += 1
        #update our input and hashes with this new number found to try again until we find it 
        hash_input = f"{secret_key}{number}"
        md5_hashinput = hashlib.md5(hash_input.encode()).hexdigest()

    return number 

def main():

    zeros_amount = 5 
    zeros_amount_2 = 6
    secret_key = "yzbqklnj"

    result = smallest_positive_number(secret_key, zeros_amount)
    result_2 = smallest_positive_number(secret_key, zeros_amount_2)

    print(f"the smallest positive number is {result} with 5 leading zeros.")
    print(f"the smallest positive number is {result_2} with 6 leading zeros.")

main()