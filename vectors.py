
import math

vectors = []

# Asks the user for the list of vectors to compute
def promptEquation():
    print("Enter a list of vectors, to subtract, just flip the magnitude or components of the vector.")
    print("Enter the list of vectors as components (x+y) or magnitude&direction (m@d)")
    print("Enter vectors (enter 'done' when finished): ")
    vector = ""
    i = 0 # to keep track of vector #
    while True: # until the user enters "done"
        vector = input(f"Enter vector {i + 1}: ") # ask the user for this vector #
        if vector == "done": # if the user enters done, stop asking
            break
        if "@" in vector: # if the vector contains @, try and parse it as a magnitude and direction case
            mag = float(vector.split("@")[0]) # the magnitude is the number before the @
            dir = float(vector.split("@")[1]) # the direction is the number after the @
            x_comp = mag * math.cos(math.radians(dir)) # calculate the x component (r*cos(theta))
            y_comp = mag * math.sin(math.radians(dir)) # calculate the y component (r*sin(theta))
            vectors.append([x_comp, y_comp]) # add the vectors as a list to the vector list
        else: # otherwise its an x and y component separated by "+"
            x = float(vector.split("+")[0]) # the x component of the vector
            y = float(vector.split("+")[1]) # the y component of the vector
            vectors.append([x, y]) # add them as a list to the vector list
        i += 1 # next vector number


def calculateResultant():
    r_x = 0 # resultant x
    r_y = 0 # resultant y
    for vector in vectors:
        r_x += vector[0] # sum every x component
        r_y += vector[1] # sum every y component
    mag = math.sqrt((r_x ** 2) + (r_y ** 2)) # calculate the magnitude with formula sqrt(x^2 + y^2)
    dir = 0 # the direction of the vector
    if r_x == 0: # if r_x is 0, don't divide by 0
        dir = 90 # dir is always 90, will be fixed by quadrant logic
    else:
        dir = math.degrees(math.atan(r_y / r_x)) #used atan(y/x) to find the angle between vector and x-axis
    if r_y < 0: # if r_y is negative, we'll need to manipulate the angle
        dir += 180 # if we should be in the third quadrant, add 180 to our positive angle
        if r_x > 0: # if we should be in the fourth quadrant, add 180 to our negative angle (again)
            dir += 180
    elif r_x < 0: # if we should be in the second quadrant, add 180 to our negative angle
        dir += 180
    # just shows resultant stats
    print("----------------\nThe resultant vector:")
    print("\tComponents:")
    print(f"\t\tx: {r_x}") # formatted strings
    print(f"\t\ty: {r_y}")
    print("\tVector equation:")
    print(f"\t\t{mag} @ {dir} degrees")

def main():
    print("Vector Adder v1 by Devin")
    print("For Soffia <3")
    print("----------------")
    promptEquation()
    calculateResultant()

if __name__ == "__main__":
    main()