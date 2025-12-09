import sys
import time
import os
import random
import json
import re

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
def customer_order():
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
        pizza_date = load_pizza_menu()
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

def validate_topping_count(toppings):
    if len(toppings) <= 3:
        print(f"Enough Amount of Toppings: {len(toppings)}/3")
        return True
    else:
        print(f"Too many toppings! {len(toppings)}/3")
        return False




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
    
class PizzaDelivery:
    def __init__(self):
        self.orders = []
        self.completed = set()
        
    def add_order(self, pizza):
        self.orders.append(pizza)
        print(f"Added: {pizza}")
    
    def complete_order(self, order_number):
        self.completed.add(order_number)
        print(f"order #{order_number} completed!")
    
    def show_deliveries(self):
        print("\n" + "="*60)
        print("Delivery queue (sorted by priority)")
        print("="*60)
        
        #lambda function
        sorted_orders = sorted(self.orders, key=lambda p: p.order_number)
        #set operations
        all_order_numbers = set(p.order_number for p in self.orders)
        pending = all_order_numbers - self.completed
        
        for pizza in sorted_orders:
            status = "Completed" if pizza.order_number in self.completed else "Pending"
            print(f"{pizza} - {status}")
        
        print("="*60)
        print(f"Total: {len(all_order_numbers)} | Pending: {len(pending)}\n")
        print(f"Completed: {len(self.completed)}")
        print("="*60)

#play the game
def PizzaGame():
    delivery = PizzaDelivery()
    order_counter = 100
    
    #starting screen
    print("Work at a Pizza Place!")
    
    while True:
        print("Main Menu")
        print("Would You Like to Take a Customer's order?")
        choice = input("\nYes or No\n")
        
        if choice.lower() == "yes":
            #problem A
            order_counter += 1
            order_details = customer_order()
        
        #pizza amt selection
            if order_details:
                if validate_topping_count(order_details['toppings']):
                    confirm = input("press enter to make pizza")
                    #time countdown
                    success = time_countdown()
                    if success:
                        #transfer to deliveries if success
                        pizza = Pizza(
                            order_details['size'],
                            order_details['toppings'],
                            order_details['sauce'],
                            order_counter
                        )
                        delivery.add_order(pizza)
                        print("deliver this pizza")
                        
        elif choice.lower() == "no":
            print("thanks for playing!")
            print("goodbye!")
    
            
    
if __name__=="__main__":
    PizzaGame()

#clear the screen once finished
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
