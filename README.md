# Work at a Pizza Place!



## Attribution Table

## Attribution Table

Method/Function | Primary Author | Techniques Demonstrated
----------------|----------------|-------------------------
clear_screen | Angela Vaught | os.system, cross-platform functionality
load_pizza_menu | Angela Vaught | json.load()
customer_order | Neil Vu | optional parameters, randomization
count_completed_orders | Neil Vu | conditional expression
time_countdown | Angela Vaught | f-strings, time measurement
PizzaDelivery.add_order | Jaena Manalo | list append, print formatting
PizzaDelivery.complete_order | Jaena Manalo | set operations
PizzaDelivery.show_deliveries | Jaena Manalo | lambda with sorted(), set difference
PizzaGame (main loop) | Group | user interaction loop






Files in repository:
"Inst326Project" is the main code of the Pizza Game
"pizza_data.json" is the file that stores the pizza data from the menu. It
    includes all necessary pizza objects such as the sauces, toppings, sizes along
    with their corresponding types
"README.md" is the written documentation of how our project functions


#### Purpose of the Game:

To create a memory style game where it tests whether you can remember the customer's order to make the right pizza within a given time.

#### How to Run the Game:

Because this is a memory game, you need to register what the order is saying so that you can recall it easily in order to create the right pizza for the customers

Here's how it works

##### STEP 1: Ask if the customer would like to take an order

Picture yourself as a pizza worker at a popular pizza store branch. A customer comes to you to ask and ask for an order. 

This question asks if you can accept an order. You can make two choices.

- If you say YES, you will receive an order request from the customer, stating their preferred size and dough, sauce and topping.
- If you say NO, the game formally ends.


##### STEP 2: Memorize what the customer requested for a specific pizza order.

Once you accept the request, you will be given a task that will test your memory in order to make the pizza.

The process of this step will be as folowing

A). First it will appear with a given type of pizza from one of the most common list in the pizza branch. ###### Your task is to memorize the description of the pizza for about 10 seconds, then you will need to retrieve the information by typing exactly what it says from that description. 

B). If you got it right, it will accept that response - which will then start the pizza oven. If completed on time within 15 seconds or less, that pizza is successfully delivered to the customer. If you get incorrect response, you will receive an error message, meaning you will need to try again until you get the correct type of pizza as specified.

WARNING: If you continue to fail the process and you finally got the step correct, that order will be declined and you will lose the game.

Now that you know the process, you will need to know the specific types of pizzas in order to begin this memory game

###### SPECIFIC PIZZA TYPES YOU NEED TO MEMORIZE

- 1). Size (small, medium or large)
- 2). Sauce Type
- 3). Toppings




#### References

All ideas were generally made from our own and do not reflect from given sources in this classroom (unless otherwise stated).
