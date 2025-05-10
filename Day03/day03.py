#Advent of Code 2015: Day 03

#Function for part 1:

def houses_visited(direction_file):

    direction_file = open("input.txt").read().strip()

    #set up our coordinates
    x, y = 0, 0 
    visited_houses = set()
    #add our starting point 
    visited_houses.add((x,y))

    for movement in direction_file:
        #moving up "north"
        if movement == "^":
            y += 1
        #moving down "south"
        elif movement == "v":
            y -= 1
        #moving to the right "east"
        elif movement == ">":
            x += 1
        #remaining possible movement is to the right "west"
        else:
            x -= 1
    
        #lets add these new coordinates to our set of visited houses 
        visited_houses.add((x,y))
        
    return len(visited_houses)

#function for part 2:
def houses_visited_robosanta(directions_file):

    directions = open(directions_file).read().strip()

    #set up our coordinates for santa 
    x_santa, y_santa = 0, 0 
    #set up our coordinates for robosanta
    x_robosanta, y_robosanta = 0, 0

    visited_houses = set()
    #add starting position 
    visited_houses.add((x_santa, y_santa))

    for i, movement in enumerate(directions):

        if i % 2 == 0: #it is santa's turn 
            #moving up "north"
            if movement == "^":
                y_santa += 1
            #moving down "south"
            elif movement == "v":
                y_santa -= 1
            #moving to the right "east"
            elif movement == ">":
                x_santa += 1
            #remaining possible movement is to the right "west"
            else:
                x_santa -= 1
            visited_houses.add((x_santa, y_santa))

        else: #it is robosanta turn 
            #moving up "north"
            if movement == "^":
                y_robosanta += 1
            #moving down "south"
            elif movement == "v":
                y_robosanta -= 1
            #moving to the right "east"
            elif movement == ">":
                x_robosanta += 1
            #remaining possible movement is to the right "west"
            else:
                x_robosanta -= 1
            
            visited_houses.add((x_robosanta, y_robosanta))
        
    return len(visited_houses)

def main():

    directions = "input.txt"
    number_of_houses_visited = houses_visited(directions)
    number_of_houses_with_robosanta = houses_visited_robosanta(directions)

    print(f"Santa visited {number_of_houses_visited} houses.")
    print(f"Santa and Robosanta visted {number_of_houses_with_robosanta} houses total.")
main()