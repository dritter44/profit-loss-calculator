#this is the profit and loss calculator that i needed to code for the tastyworks job
'''
the inputs look the folowing way:
[["10", "5.0", "Buy"] ["12", "2.0" "Sell"]], 9 price, number of shares, and buy or sell

'''

def pandl(orders_list, curr_price):          #orders is an array of arrays containing the types of orders you see above
    #initiate position int. negtive int indicates a short position, positive indicates a long position
    #initiate these variables from the first order
    # initiate var for size of order
    order_size = float(orders_list[0][1])
    # initiate var for order price
    order_price = float(orders_list[0][0])
    # long orders will have positive values, short orders will be negative
    if orders_list[0][2] == "Sell":
            order_size *= -1
    pos_size = order_size
    # initiate avg price of position
    avg_prc = order_price
    #initiate position value
    pos_val = pos_size*avg_prc
    # initiate answer list. contains 2 values, unrealized gains and realized
    unreal = pos_size*avg_prc
    realized = 0
    #add gains/losses value to gains list
    gains=[]
    gains.append(unreal)
    gains.append(realized)
    
    #initiate loop through order list, starts at second order 
    for x in range(1,len(orders_list)):
        # attribute info in order lists to order variables
        order_size = float(orders_list[x][1])
        if order_size == 0.0:
            continue
        order_price = float(orders_list[x][0])
        # long orders will have positive values, short orders will be negative
        if orders_list[x][2] == "Sell":
            order_size *= -1

        # add condition for if the net number of shares is lower with new trade, a realized gain or loss is generated
        if abs(pos_size + order_size) < abs(pos_size):
            #initialize realized gain variables
            #realized gain is the order size of the shares times the averag
            realized = (order_price-avg_prc)*order_size
            #check if an order reverses the position
            if abs(order_size) > abs(pos_size):
                pos_size += order_size

        # update avg price of shares; weigthed average of position size and price
        avg_prc = ((pos_size*avg_prc)+(order_size*order_price))/(order_size+pos_size)
        # calculate unrealized profit or loss
        




    return orders_list

print(pandl([["10", "5.0", "Buy"], ["12", "2.0", "Sell"]], 9))