#!/usr/bin/env python
# coding: utf-8

# In[24]:


LINE_WIDTH = 85

def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")
    
def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")
    
def error(msg):
    print(f"Error! {msg}\n")

def menu():
    print(f"""Please select one of the following options:
    {"[car]":<20} Select car details based on Car_ID
    {"[cylinder_num]":<20} All cars for a specified cylinder number
    {"[carbody]":<20} All cars in the specified car body
    {"[columns_specified_2_5]":<25} Retrieve a specific number of columns (2 up to 5)
    {"[carnames_alphabetically]":<25} Car names alphabetically
    {"[car_body_prices]":<20} Summary of sales (total car price) for each car body
    {"[top_5_car_sale]":<20} Top 5 car sale by price(the most expensive) and per car body
    {"[self_selected_data]":<20} Details of cars based on your own selection
    {"[cars_per_fuelsystem]":<20} Display the numbr of cars per fuel system using a bar chart
    {"[hp_5cheapest_cars]":<20} Display the horsepower of the top 5 car sale by price using subplot
    {"[buying_patterns]":<20} customers’ buying behaviour using a suitable visualisation
    {"[exit]":<20} : Exit
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()
