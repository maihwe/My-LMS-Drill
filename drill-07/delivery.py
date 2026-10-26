""" **Wrong Answer**
**FAIL member free deliveryInput: [5000,20,true]Expected: 0File "solution.py", line 3 def delivery_fee(order_total, distance_km, is_member): ^^^ IndentationError: expected an indented block after function definition on line 68**
**FAIL short distanceInput: [1000,5,false]Expected: 500File "solution.py", line 3 def delivery_fee(order_total, distance_km, is_member): ^^^ IndentationError: expected an indented block after function definition on line 68**
**FAIL medium distanceInput: [1000,10,false]Expected: 1000File "solution.py", line 3 def delivery_fee(order_total, distance_km, is_member): ^^^ IndentationError: expected an indented block after function definition on line 68**"""

def delivery_fee(order_total, distance_km, is_member):
    if order_total < 0 or distance_km < 0:
        return "Invalid Number"

    if is_member and order_total >= 5000:
        return 0

    if distance_km >= 5:
        return 500
    elif distance_km >= 15:
        return 100
    else:
        return 2000
print(delivery_fee(5000, 20, True))   
print(delivery_fee(1000, 5, False))   
print(delivery_fee(1000, 10, False))  