import sys
import time
import os
import random
import json
import re

def clear_screen():
    """Clears the terminal screen
    
    Will work on both windows/mac systems
    
    Note: The professor gave us guidance on this function.
    
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Pizza:
    """Represents a customer's pizza order with size, toppings, sauce, and order number
    
    Attributes:
        size: Size of the pizza (small, medium, large, extra-large)
        toppings: List of toppings on pizza
        sauce: Type of sauce on the pizza
        order_number: Unique order tracking number
        
    Primary Author: Angela Vaught
    """
    def __init__(self, size, toppings, sauce, order_number):
        """_summary_

        Args:
            size (str): size of the pizza
            toppings (list): list of toppings
            sauce (str): type of sauce
            order_number (int): order tracking number
        
        Primary Author: Angela Vaught
        Techniques: None
        """
        self.size = size
        self.toppings = toppings
        self.sauce = sauce
        self.order_number = order_number
        
    def __str__(self):
        """Return a formatted string representation of the pizza order.

        Returns:
            str: Formatted order details with order number, size, toppings, and sauce
            
        Primary Author: Angela Vaught 
        """
        return f"Order #{self.order_number}: {self.size} pizza with {', '.join(self.toppings)} and {self.sauce} sauce"

    
def load_pizza_menu():
    """Load pizza options from JSON file
    
    Returns:
        dict: Pizza menu containing sizes, sauces, toppings, and preset pizzas
    
    Primary Author: Angela Vaught
    Techniques: json.load()
    """
    with open("pizza_data.json", "r") as file:
        pizza_menu = json.load(file)
        return pizza_menu

    
# Problem A: Creating Customer Orders based on the type of pizzas

def customer_order(order_type = None):
        """Identifies the customer's order through searching different types of pizzas they wished to order
        
        Returns:
            size = selected pizza size
            sauce = selected type of sauce (if desired) 
            topping =  selected type of toppings (if desired) 
        
        Primary Author: Neil Vu (Edited: Angela)
        Techinques: Optional Parameters
    
        Side Effects:
            Modifes the different orders for each customer type (by each round of the game)
    
        """
        pizza_data = load_pizza_menu()
        
        if order_type is None:
            order_type = random.choice(["preset","custom"])
        
        if order_type == "preset":
            preset_name = random.choice(list(pizza_data["preset_pizzas"].keys()))
            preset_info = pizza_data["preset_pizzas"][preset_name]
            sauce = preset_info["sauce"]
            toppings = preset_info["toppings"][:3]
            size = random.choice(pizza_data["sizes"])
            return {"size": size, "sauce": sauce, "toppings": toppings}
        else:
            size = random.choice(pizza_data["sizes"])
        #2). Sauce Type
            sauce = random.choice(pizza_data["sauces"])
            cheese_options = ["cheese", "extra cheese"]
            cheese = random.choice(cheese_options)
        #how many toppings to choose
            amt_top = random.randint(1,8)
        #3). Topping Type (how many toppings to choose)
            toppings = random.sample(pizza_data["toppings"], k=amt_top)
        #return a dictionary
            return {"size": size, "sauce": sauce, "toppings": toppings}
        
def count_completed_orders(delivery_system):
    """Count how many completed orders are there and whether if it is there.
    Arg:
        Delivery_System - tracks the delivery system
    
    Return:
        Int: number of completed orders (by how many)
    
    Primary Author: Neil Vu (Assisted by Angela)
    
    Techinques: Conditional Expression.
    """
    count = len(delivery_system.completed)
    return count if count > 0 else 0
    
    # Problem B.1) assembling pizza with a timer countdown
def time_countdown():
        """Time how long it takes to assemble the pizza and check if under 3 min
        
        Args:
            time_limit (int, optional): Max time allowed in seconds and defaults to 180.
            
        Returns:
            bool: True if under time limit, false if over
        
        Primary Author: Angela Vaught
        Techniques used: F-strings
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
    
    ## PROBLEM C: Delivery
    #Probelm C - Jaena Manalo
    #Pizza Delivery
    #deliveries are based on priority/order number
        #if the order number is smaller then the next one, then that order should be 
        #delivered first before the next one
    #sort list of orders based on priority with lambda to sort from least to
    #greatest
    
class PizzaDelivery:
    """This is a system where the pizza deliveries will be tracked and organized
    based on priority. It has completed orders and pending orders.
    
    Attributes: 
    orders(list): a list of pizza objects representing active orders
    completed(set): set of order numbers that are completed.
    Primary author: Jaena Manalo
    """
    
    def __init__(self):
        """This will initialize the PizzaDelivery.
        Sets up the orders and completed as data structures to properly track 
        the orders.
        Primary author: Jaena Manalo
        """
        self.orders = []
        self.completed = set()
        
    def add_order(self, pizza):
        """this adds a new order to the queue.

        Args:
            pizza (obj): represents the actual order
            Primary author: Jaena Manalo
        """
        self.orders.append(pizza)
        print(f"Added: {pizza}")
    
    def complete_order(self, order_number):
        """this represents the completed orders in the queue

        Args:
            order_number (int): marks the order as completed
            Primary author: Jaena Manalo
        """
        self.completed.add(order_number)
        print(f"order #{order_number} completed!")
    
    def show_deliveries(self):
        """this will display the orders and pending ones. Shows the delivery
        queue with the order numbers listed by priority as well as the status of
        the orders. 
        
        Lambda function: sorts the orders by priority
        Set operations: displays the orders that are pending and completed
        
        Returns:
        None: only prints the delivery function
        Primary author: Jaena Manalo
        Techniques used: Lambda function and set operations
        """
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
    """This is the main game loop. It will start the order counter and ask the 
    player/employee if they would like to take and order in which the answer is
    yes or no. Then you will make a new pizza from what the customer ordered and
    will check whether it was assembled right. The time countdown function is also
    implemented that starts the countdown of the assembly and rules are also
    implemented. Finally, the orders are tracked from the delivery queue. When 
    the player inputs "no" the game ends.
    
    Returns:
        None: only inputs are implemented and there are no return values.
    
    Primary author: Jaena Manalo
    """
    delivery = PizzaDelivery()
    order_counter = 100
    
    #starting screen
    print("Work at a Pizza Place!")
    
    while True:
        print("Would You Like to Take a Customer's order?")
        choice = input("\nYes or No\n")
        
        if choice.lower() == "yes":
            #problem A
            order_counter += 1
            order_details = customer_order()
            pizza = Pizza(order_details["size"], order_details["toppings"], order_details["sauce"], order_counter)
            print(pizza)
            time.sleep(20)
            clear_screen()
            
            start_time = time.time()
            
            while True:
                player_input = input("please start assembling the pizza, start with size and dough (ex. medium dough) (separate with spaces, no commas): ")
                ingredients_list = player_input.split()
                # Have the player type in dough for the assembly
                if len(ingredients_list) < 4:
                    print("Make sure you fully assemble the pizza! Format: size dough sauce cheese [toppings]")
                    continue
                elif len(ingredients_list) < 2 or ingredients_list[1] != "dough":
                    print("Error! 'dough' must come first!")
                    continue
               
                playerin_size = ingredients_list[0]
                playerin_sauce = ingredients_list[2]
                playerin_cheese = ingredients_list[3]
                playerin_toppings = ingredients_list[4:]
                
                if len(playerin_toppings) > 8:
                    print("Too many toppings! Max is 8.")    
                    continue
                
                player_all_toppings = [playerin_cheese] + playerin_toppings
            
                if playerin_size == order_details["size"] and playerin_sauce == order_details["sauce"] and set(player_all_toppings) == set(order_details["toppings"]):
                    print("Perfect! The pizza assembly is correct")
                    print("The pizza is now cooking...")
                    time.sleep(10)
                    
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    
                    if elapsed_time <= 180:
                        delivery.add_order(pizza)
                        print("Pizza was completed and sent for delivery!")
                    else:
                        print("Too slow! Pizza took too long.")   
                    break
                else:
                    print("Wrong pizza, try again")
                
                        
        elif choice.lower() == "no":
            total_completed_orders = count_completed_orders(delivery)
            print(f"You have completed {total_completed_orders} orders.")
            print("thanks for playing!")
            print("goodbye!")
            break
    
            
    
if __name__=="__main__":
    PizzaGame()


    
