def calculatePrice(cart):
    if len(cart) == 0:
        return 0
        
    totalPrice = 0
    for key, value in cart.items():
        totalPrice += value
        
    return f'Total Price: ${totalPrice:,}' if len(cart) <= 5 else f'Total Price: ${totalPrice - totalPrice * 0.1:,.0f}'
        

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(calculatePrice(cart_items))