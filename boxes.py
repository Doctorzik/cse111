#This program computes and display the number of boxes that each item can hold

import math
manufacture_item = int(input("what is the number of manufactured items? ")) # This ask for item manufactured by company

user_item_packed = int(input("what is the number of user packed items? ")) # this ask for item the user packed

number_of_boxes = math.ceil(manufacture_item / user_item_packed)

print(number_of_boxes)




