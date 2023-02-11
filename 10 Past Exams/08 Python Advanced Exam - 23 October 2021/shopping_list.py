def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    result = ""
    product_types = 0

    for product_name, info in kwargs.items():
        if product_types == 5:
            break
        price, quantity = info
        total_price = price * quantity
        if budget >= total_price:
            product_types += 1
            budget -= total_price
            result += f"You bought {product_name} for {total_price:.2f} leva.\n"

    return result
