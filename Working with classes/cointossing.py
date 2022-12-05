# this program imports the coin module and
# creates an instance of the Coin class.

import coin

def main():
    # create an object from the Coin class.
    my_coin = coin.Coin()
    
    # display the side of the coin that is facing up.
    print("This side is up:", my_coin.get_sideup())
    
    # toss the coin.
    print("I am going to toss the coin ten times:")
    sides = []
    for count in range(10):
        my_coin.toss()
        sideup = my_coin.get_sideup()
        print(sideup)
        sides.append(sideup)
        
    count_head = 0 # Store the count of the number of heads
    count_tail = 0  # Store the count of the number of tails gotten
    for i in sides:
        if i == "Heads":
            count_head += 1
        else:
            count_tail += 1
            
    print(f"The number of Heads are {count_head} and the number of tails are {count_tail}")
        
        
# call the main function
main()
    