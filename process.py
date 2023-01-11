#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing all the necessary libraries
import tui
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import csv
import os

# to view the entire dataset
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_csv('CarPrice.csv')  # reading the csv file using pandas and storing the value in df


# function initialization
def use_car_data(df):
    tui.started('use_car_data')
    
#Using exception handling to catch any errors,that might occur while trying to access and read the file   
    file_path = 'CarPrice.csv'
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
    except IOError:
        print("Unable to open the file")

    df = pd.read_csv('CarPrice.csv')  # reading the csv file using pandas and storing the value in df
    
    tui.completed()



#function initialization
def car(df):

    tui.started("car")
    # reading data using pandas and storing in DataFrame df
    df = pd.read_csv('CarPrice.csv')

    # exception handling to catch any errors that might occur
    try:
        
        # collecting user input to display appropriate record
        car_id = int(input("Enter a car ID b/w 1 and 205: "))
        if car_id > 0 and car_id <= len(df['car_ID']):           
            Id = df[df['car_ID']==car_id]
            print(Id)
        else:
            print("PLease enter a valid Id")
    
    except ValueError:  
        print(f"Please enter a valid Id")    
    tui.completed()

    
# function initialization
def cylinder_num(df):
    
    tui.started('cylinder_num')

    # exception handling to catch any errors that might occur
    try:
        
        # using groupby() function from Pandas library to group the different types of cylinder numbers available
        # Once the grouping is done, iterating on the groups
        
        df_cynum_grouped = df.groupby(['cylindernumber'])
        for group, item_in_group in df_cynum_grouped:
            #print(f"Group: {group}")
            #print(item_in_group)
            print("Available cylinder numbers are : 2,3,4,5,6,8,12")
            print()
            num = int(input("Please select a cylinder number: "))
            print(f"The cars with the cylinder number {num} are: ")
            print()

            # Using get_group() method from groupby() object to retrieve a group from grouped DataFrame
            cars_with_cynum = df_cynum_grouped.get_group(num)[['CarName','cylindernumber']]
            print(cars_with_cynum)
            break
            
    except (NameError, ValueError, IOError, KeyError) as e:
        print("Enter a valid cylinder number, Error :",e)
        
    tui.completed()
    
    


# function initialization
def carbody(df):
    
    tui.started('carbody')
    
    # exception handling to catch any errors that might occur
    try:
        
        carbody_counts = df['carbody'].value_counts()
        # using groupby() function from Pandas library to group the different types of carbodies available
        carbody = df.groupby('carbody')

        
        # iterating over the groups
        for group,item_in_group in carbody:
            #print(f"Group {group}")
            #print(item_in_group)

            print("The available carbody types are: sedan, hatchback, wagon, hardtop, convertible")
            print()
            selected_type = input("Please enter a carbody type: ")
            print()
            
            #using the get_group method from the groupby object to select the user inputed carbody type 
            cars_for_carbody = carbody.get_group(selected_type)[['CarName','carbody']].head()
            print(cars_for_carbody)
            break
    
    except (KeyError, NameError, ValueError, IOError) as e:
        print("Error: Invalid carbody type: ",e)
        
        
    tui.completed()
    


#function initialization
def columns_specified_2_5(df):
    tui.started('columns_specified_2_5')
    # exception handling to catch any errors that might occur
    try:
        
        # taking user input of car_ID
        ID = int(input("Enter a car ID b/w 1 and 205: "))
        
        # using if conditional statement to limit the user response within the car_ID's available
        if ID >=0 and ID <206:     
            value = df[df['car_ID'] == ID]
            # using integer based indices to retrieve only the specified columns
            value = value.iloc[:,1:5]
            print(value)  
        else:
            print("Enter a valid Id")
    
    except (KeyError, NameError, ValueError, IOError) as e:
            print("Error: Invalid Id: ",e)

    tui.completed()



# function initialization
def carnames_alphabetically(df):
    
    tui.started('carnames_alphabetically')
    # exception handling to catch any errors that might occur
    try:
        # using sort_values() function from Pandas to sort a column in ascending/descending form
        car_names = df[['CarName']].sort_values(by = 'CarName', ascending = True, inplace = False)
        print(car_names)

    except (KeyError, NameError, ValueError, IOError) as e:
        print("Error: ",e)
       
    tui.completed()

    



# function initialization
def car_body_prices(df):
    tui.started('car_body_prices')
    # exception handling to catch any errors that might occur
    try:
        
        # using groupby() function from Pandas to group types of carbodies available
        carbody = df.groupby('carbody')

        # iterating over the groups
        for group,item in carbody:
            #print(f'Group {group}')
            #print(item)

            print("Choose a carbody type - sedan, hatchback, wagon, hardtop, convertible")
            print()
            # taking user input on the type of carbody to be selected
            body_type = input("")

            # using the get_group method to find the sum() of the selected carbody group
            total_car_price = carbody.get_group(body_type)['price'].sum()
            print(f"Total car price of {body_type} is: {total_car_price}")          
            break
        
    except (KeyError, NameError, ValueError, IOError) as e:
        print("Error: Select a valid option")

    tui.completed()    


# function initialization
def top_5_car_sale(df):
    tui.started('top_5_car_sale')
    # exception handling to catch any errors that might occur
    try:
        
        # using groupby() function to group dofferent types of carbodies available
        carbody = df.groupby('carbody')

        # A nested function which takes the groups as a parameter and returns top-5 rows of the group in descending order
        def price_5(group):
            sorted_price = group.sort_values(by = 'price', ascending = False)
            return sorted_price.head(5)

        # using the apply method from the groupby() object on the carbody variable which contains the groups of carbodies
        top_cars = carbody.apply(price_5)

        carbody_prices = top_cars[['carbody','price']]
        print(carbody_prices)
    
    except (KeyError, NameError, ValueError, IOError) as e:
        print("Error: ",e)
        
    tui.completed()
        
        
#initializing function
def self_selected_data(df):
    tui.started('selected_data')
    
    try:
        
        # getting the types of carbody available and number of times they have occured in the dataset
        carbody = df['carbody'].value_counts().index
        bodyvals = df['carbody'].value_counts().values
        #plotting pie chart
        plt.pie(x=bodyvals, labels = carbody, autopct='%1.2f%%')
        plt.show()

        body_type = input("Select a carbody type: sedan,hatchback,wagon,convertible,hardtop: \n\n")
        # finding the max price and min price of the selected body type
        max_price = df[df['carbody']==body_type]['price'].max()
        min_price = df[df['carbody']==body_type]['price'].min()
        min_max = print(f"The maximum car price of {body_type} is {max_price} and minimum is {min_price}")
        
    
    except (KeyError, NameError, ValueError, IOError) as e:
        print("Error: ",e)
        
    tui.completed()
    
        
    

# function initialization
def cars_per_fuelsystem(df):
    tui.started('cars_per_fuelsystem')
    # exception handling to catch any errors that might occur
    try:
        
        # Using groupby() function to group the different types of fuelsystems
        group_fuelsystem = df.groupby(['fuelsystem'])
        
        # iterating over the groups
            
        #Using the value_counts() method to count the unique values in a series,
        #and index attribute to return a series with the labels of the Series
        fuelsystem_names = df['fuelsystem'].value_counts().index
        counts = df['fuelsystem'].value_counts()

        # creating a figure
        fig = plt.figure(figsize=(14,9))

        plt.bar(fuelsystem_names, counts, label = 'Cars X Fuelsystem',color='violet') # plotting the graph
        # creating x and y axis
        plt.xlabel('Fuelsystems')
        plt.ylabel('Number of cars')
        # creating a title
        plt.title('Num of cars per fuelsystem')

        plt.legend() # create a legend
        fig.savefig('my_figure.png')
            
            
        plt.show()
        #Saving the figure to png
    
        
    
    except (KeyError, NameError, ValueError, IOError) as e:
        print("Error: ",e)
        
    tui.completed()     
        
        
# function initialization
def hp_5cheapest_cars(df):
    tui.started('hp_5cheapest_cars')
    # exception handling to catch any errors that might occur
    try:

        # Using sort_values() function to sort the price column in ascending order and get first 5 values
        cheapest_priced_5cars = df.sort_values(by='price',ascending = True).head()
        hp = cheapest_priced_5cars[['CarName','horsepower','price']]

        # creating a figure and subplots and initializing figure size
        fig, ax = plt.subplots(figsize=(15,12))
        # using the subplot_adjust method to adjust the vertical and horizontal height of subplots
        fig.subplots_adjust(hspace=0.5, wspace=0.5)
        plt.suptitle("Horsepower of the 5 cheapest cars",fontsize=16, y=0.90)

        # acquiring values from columns and appending it to list
        cars_name = hp['CarName'].to_list()
        cars_hp = hp['horsepower'].to_list()

        # iterating over length of CarName and creating that many subplots
        for i in range(len(hp['CarName'])):
            ax = plt.subplot(1,5,i+1)
            ax.bar(cars_name[i],cars_hp[i])
            ax.set_ylim(0,75) # set y-xais limit value
            ax.set_ylabel("HP")
            
        plt.show()

    except (KeyError, NameError, ValueError, IOError) as e:
            print("Error: ",e)
            
            
    tui.completed()
    
    
    

# function initialization
def buying_patterns(df):
    tui.started('buying_patterns')
    # exception handling to catch any errors that might occur
    try:
        
        # importing necessary libraries
        import matplotlib.pyplot as plt
        get_ipython().run_line_magic('matplotlib', 'inline')
        
        # Querying fueltype by 'gas' and 'diesel'
        df_gas = df.query("fueltype == 'gas' ")
        df_diesel = df.query("fueltype == 'diesel' ")

        # creating a figure and subplots and initializing figure size
        fig , (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,5))
        fig.subplots_adjust(hspace=0.3, wspace=0.3)
        fig.suptitle("How engine size can influence customers buying pattern")

        
        # first axis 
        # selecting necessary data using Pandas on the Queried DataFrame
        gas_car_price = df_gas[['price']]
        gas_engine_size = df_gas[['enginesize']] 

        diesel_car_price = df_diesel[['price']]
        diesel_engine_size = df_diesel[['enginesize']]

        # initializing scatter plot on axis-1
        ax1.scatter(gas_engine_size,gas_car_price, label = 'gas')
        ax1.scatter(diesel_engine_size, diesel_car_price, label = 'diesel')
        # setting title, labels and customizations to axis-1
        ax1.set(title = 'price vs enginesize', xlabel='Size of engine', ylabel='Price')
        ax1.legend()
        ax1.grid(True)
        ax1.set_facecolor("whitesmoke")

        # second axis
        # selecting necessary data using Pandas on the Queried DataFrame
        gas_car_price = df_gas[['price']]
        gas_hp = df_gas[['horsepower']]

        diesel_car_price = df_diesel[['price']]
        diesel_hp = df_diesel[['horsepower']]
        # initializing scatter plot on axis-2
        ax2.scatter(gas_hp,gas_car_price, label = 'gas', marker = '*')
        ax2.scatter(diesel_hp,diesel_car_price, label = 'diesel', marker = '*')
        # setting title, labels and customizations to axis-1
        ax2.set(title = 'price vs hp', xlabel = 'Horsepower', ylabel = 'Price')
        ax2.set_facecolor("pink")
        ax2.legend()
        ax2.grid(True)


        # third axis
        # selecting necessary data using Pandas on the Queried DataFrame
        gas_car_price = df_gas[['price']]
        gas_citympg = df_gas[['citympg']]

        diesel_car_price = df_diesel[['price']]
        diesel_citympg = df_diesel[['citympg']]
        # initializing scatter plot on axis-2
        ax3.scatter(gas_citympg, gas_car_price, label = 'gas')
        ax3.scatter(diesel_citympg, diesel_car_price, label = 'diesel', marker = '*')
        # setting title, labels
        ax3.set(title = 'price vs citympg', xlabel = 'Citympg', ylabel = 'Price')
        ax3.legend()
        
        
        #returns plt.show() when function is called
        plt.show()

    except (KeyError, NameError, ValueError, IOError) as e:
        print("Error: ",e)
 
    tui.completed()

