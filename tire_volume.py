# This program calculate the output volume of space inside a tire. 
import math
from datetime import datetime 

tire_width = float(input("what is the width of the tire in millimetres? ")) # this take width input from the user

tire_aspect_ratio = float(input("What is the aspect ratio of the tire? ")) # This prompt the user for the aspect ratio of the tire

tire_diameter = float(input("What is the diameter that the tire fits in inches? ")) # This prompt the user for the diameter


second_side = (tire_width * tire_aspect_ratio) + (2540 * tire_diameter)

first_side = math.pi * tire_width**2 * tire_aspect_ratio * (second_side)

over_all = first_side / 10000000000

print(f"The Volume of space inside the tire is {over_all:.2f}litres")

tire_purchase = input(f"Do you want to buy tire with these dimensions? \n W: {tire_width} \n ASR: {tire_aspect_ratio}, \n D: {tire_diameter}")
if tire_purchase.lower() == "yes":
  contact = input("Please enter your Phone number for us to contact you: ")
else: 
  print("Thanks for using our program.")
current_date = datetime.now()

with open("volumes.txt" , mode="at") as tire_file:
  print(current_date , file=tire_file)
  print(f"{current_date: %Y-%m- %d} ,{round(tire_width, 2)}, {round(tire_aspect_ratio, 2)}, {round(tire_diameter, 2)}, {round(over_all, 2)}" , file=tire_file)
  print(f"The customers's contact is: {contact}", file=tire_file)