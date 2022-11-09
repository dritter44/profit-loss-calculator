#this is the profit and loss calculator that i needed to code for the tastyworks job
'''
the inputs look the folowing way:
[["10", "5.0", "Buy"] ["12", "2.0" "Sell"]], 9 price, number of shares, and buy or sell

'''

def pandl(orders_list, curr_price):          #orders is an array of arrays containing the types of orders you see above
    #initiate position int. negtive int indicates a short position, positive indicates a long position
    pos_size = 0
    # initiate avg price of position
    avg_prc = 0
    # initiate answer list. contains 2 values, unrealized gains and realized
    gains = []
    # initiate var for size of order
    order_size = 0
    # initiate var for 
    #initiate loop through order list
    for x in range(len(orders_list)):



    return orders_arr

print(pandl([["10", "5.0", "Buy"], ["12", "2.0", "Sell"]], 9))