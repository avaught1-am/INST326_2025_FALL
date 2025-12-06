import sys
import time
import os
import random
import json

class Pizza:
    def __init__(self, size, toppings, sauce, order_number):
        self.size = size
        self.toppings = toppings
        self.sauce = sauce
        self.order_number = order_number
        
    def __str__(self):
        return f"Order #{self.order_number}: {self.size} pizza with {', '.join(self.toppings)} and {self.sauce} sauce"

    
def load_pizza_menu():
    """Load pizza options from JSON file"""
    with open("pizza_data.json", "r") as file:
        pizza_menu = json.load(file)
    return pizza_menu

    # Problem A: Creating Customer Orders based on the type of pizzas
def customer_order(self):
        """Identifies the customer's order through searching different types of pizzas they wished to order
        
        Args:
            self = reflects from lists of pizzas that each customer had specifcially ordered
            pizza = a json file list that shows the different kinds of pizza
        
        Returns:
            size = selected pizza size
            meat = selected type of meat (if desired) 
            veg =  selected type of veggies (if desired) 
    
        Side Effects:
            Modifes the different orders for each customer type (by each round of the game)
    
        """
        pizza_date = load_pizza_data()
        #load json file 
        pizza = {self}
        
        #group following files
        size = group(size)
        meat = group(meat)
        veggies = group(veggies)
        
        
        #find the specific pizza using regular expression
        ## a). based on size 
        for spec_types in pizza:
            for size_search in pizza: 
                size_search = re.search(r"\b(P<size>)")
                #match the size
                try:
                    size_search == size
                    #return with the size
                    size 
                #otherwise return None
                except:
                    NameError = "Incorrect Size"
            
            ## b). based on any meat type (if not none)
            while True:
                for meat_search in pizza: 
                    meat_search = re.search(r"\b(P<meat>)")
                    #match the size
                    if meat_search == meat:
                        #return with the meat
                        order = meat 
                    #otherwise return None
                    else:
                       "Try Again"
            ## c). based on any veggies (if not none)
            while True:
                for veg_search in pizza: 
                    veg_search = re.search(r"\b(P<veggies>)")
                    #match the size
                    if veg_search == veg:
                        #return with the veggies
                        order = veg 
                    #otherwise return None
                    else:
                        "Try Again"
        
        #do a couple of rounds as well for each customer
        spec_types += 1
        #return with the description of the order list the given customer ordered by dictionary
        return Cus_Order == (size, meat, veg)






    ##### PROBLEM B: PIZZA ASSEMBLY
    
    
    # Problem B.1) assembling pizza with a timer countdown
    def time_countdown():
        """Time how long it takes to assemble the pizza and check if under 3 min
        
        Returns:
            bool: True if under time limit, false if over
        
        """
        time_limit = 180
        print("Timer has started please start assembling your pizza...")
        print("Press Enter when finished!")
        start_time = time.time()
        
        input()
        
        end_time = time.time()
        time_taken = end_time - start_time
        
        minutes = 0
        remaining = int(time_taken)
        while remaining >= 60:
            minutes += 1
            remaining -= 60
        seconds = remaining
        
        print(f"\nTime: {minutes}:{seconds:02d}")
        
        if time_taken <= time_limit:
            print("Success! Good job!")
            return True
        else:
            print("Ran out of time!")
            return False
    
    
    #Problem B)2. Max Amount of Selection of Toppings
    
    #### 2). This section asks for how many max amount opping selections that each player can use for the game (MOST CAN BE ESTABLISHED USING SELF CLAUSE)
            
    def pizza_amount_selection(self, pizza_type):
        """Sets the max amount of toppings in the pizza assembly
        
        Args: 
            pizza_type = connects from the assembly line and in prev. functions on type of pizzas
            
        Return:
            self.ingreidents = the ingridents represented
            apply_ingr = the ingridents applied
    
        """
        #make a dict that shows the lists
        self.pizza_type = {self.name_pizza:self.ingridents}
        pizza_type = self.pizza_type
        #Make a for loop that decides how many ingredients that they need 
        for amt_ing in pizza_type:
            #Filter based on the ingredients and the quantity of it
            self.ingridents, amt_ing
            #Choose how many toppings we need for max (one says three), then apply it
            #[EXP1 if COND1 else COND2]
            [apply_ingr if amt_ing <= 3 else f"Must meet 3 toppings max"]
            #Apply to the following 
            return self.ingridents, apply_ingr
    
    
    
    ## PROBLEM C: Delivery
    #Probelm C - Jaena Manalo
    #Pizza Delivery
    #deliveries are based on priority/order number
        #if the order number is smaller then the next one, then that order should be 
        #delivered first before the next one
    #sort list of orders based on priority with lambda to sort from least to
    #greatest
    
    
    orders = [
        {'customer_name': 'Jaena', 'order_number': 7},
        {'customer_name': 'Neil',  'order_number': 9},
        {'customer_name': 'Angela', 'order_number': 12}
    ]
    
    #sort the list with lambda
    sorted_orders = sorted(orders, key=lambda x: x['order_number'])
    print(f"sorted orders: {sorted_orders}")
    
    #set operations for tracking the order and deliver it based the sorted order
    all_orders = {order['customer_name'] for order in sorted_orders}
    completed = set()
    
    for order in sorted_orders[:2]:
        name = order['customer_name']
        print(f"Deliver to {name} Order #{order['order_number']})")
        completed.add(name)
    
    pending = all_orders - completed
    
    #status of the deliveries
    print("All Customer Deliveries:", all_orders)
    print("Completed deliveries:", completed)
    print("Pending deliveries:", pending)


#clear the screen once finished
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
