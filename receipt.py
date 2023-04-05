import csv
from datetime import datetime

def main():
    try:

        products_dict = read_dictionary("products.csv", 0)

        print()

        store_name = "Inkom Emporium"
        print()
        print(store_name)

        with open("request.csv" ,"rt") as file_csv:

            reader = csv.reader(file_csv)

            next(reader)
            print("Requested Item: ")
            print()
            num_items = 0 
            sub_total_due = 0
            total = 0
            sales_tax = 0

            for row in reader:
                
                order = row[0]
                quantity = int(row[1])

                num_items += quantity
                value  = products_dict[order]
                item = value[0]
                price = float(value[1])
                print(f"{item}: {quantity} @ {price}")
        

                sub_total =  quantity * price
                sub_total_due += sub_total
            
            sales_tax = 0.06 * sub_total_due
            total = sales_tax + sub_total_due
            print(f"The number of Items: {num_items}")
            print(  )


            print(f"Subtotal: {round(sub_total_due, 2)}")
            print()
 
            print(f"Sales tax: {round(sales_tax, 2)}")

            print()


            print(f"Total: {round(total, 2)}")



            # amount = products_dict[quantity]




        print(f"Thank you for shopping at the {store_name}")

        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%A %I:%M %p}")
    except FileNotFoundError as not_found_err:
        
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")
    
    except KeyError as wrong_key:
        print(type(wrong_key).__name__, wrong_key, sep=":" )
        print(f"Error: unknown product ID in the request.csv file {wrong_key}")

    except PermissionError as not_permit:
        print(f"You dont have permission to read {file_csv}")
        print(f"Thank you.")





def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    csv_dict = {}

    with open(filename, "rt") as file_csv:

        reader = csv.reader(file_csv)
      
        next(reader)
        
        for row_list in reader:
            key = row_list[key_column_index]
            product_name = row_list[1]
            product_price = float(row_list[2]) 

            csv_dict[key] = [product_name, product_price]

    return csv_dict


if __name__ == "__main__":
    main()