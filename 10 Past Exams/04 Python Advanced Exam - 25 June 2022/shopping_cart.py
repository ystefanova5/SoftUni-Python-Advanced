def shopping_cart(*args):
    result = ""
    limits = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    meals = {"Soup": [], "Pizza": [], "Dessert": []}

    for element in args:
        if element == "Stop":
            break
        meal_type, product = element
        if limits[meal_type] > 0 and product not in meals[meal_type]:
            meals[meal_type].append(product)
            limits[meal_type] -= 1

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    for meal in sorted_meals:
        meal_type, products = meal[0], meal[1]
        result += f"{meal_type}:\n"
        for item in sorted(products):
            result += f" - {item}\n"

    if meals["Soup"] or meals["Pizza"] or meals["Dessert"]:
        return result
    return "No products in the cart!"
