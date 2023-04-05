def main():
    # Create a dictionary that contains data about six vehicles.
    # The key for each vehicle in the dictionary is the vehicle's
    # identification number (VIN). The value for each vehicle is
    # a list that contains the year, manufacturer, model, color,
    # engine design, and engine displacement.
    vehicles_dict = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
    }

    MANUFACTURER_INDEX = 1
    MODEL_INDEX = 2
    COLOR_INDEX = 3

    # Ask the user for a vehicle identification number (VIN).
    vin = input("Please enter a VIN: ")

    # Check if the vin is a key that is in the vehicles dictionary.
    if vin in vehicles_dict:
        #This stores all the value in the user input key
        data = vehicles_dict[vin]

        #This retireves the second index in the user  input key value                                             
        manufacturer = data[1]

        #This retireves the third index in the user  input key value

        model = data[2]
        #This retireves the fourth index in the user  input key value

        color = data[3]
        #This retireves the first index in the user  input key value

        year = data[0]
        #This retireves the fifth index in the user  input key value

        engine_design = data[4]
        #This retireves the sixth index in the user  input key value

        engine_displacement = [5]

        # Find the data for the vehicle that the user wants.
        pass
        print(f"The manufacturer is {manufacturer}. The mode is {model}. The color is {color} ")
        # Print the manufacturer, model, and color of the vehicle.
        # Don't print the year, engine design, or displacement.
        pass

    else:
        # Print a message stating that the VIN entered
        # by the user is not in the dictionary.
        print(f"{vin} is not in the dictionary.")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
       

            