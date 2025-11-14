import sys
import time













# Problem B.) assembling pizza with a timer countdown
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
    
    