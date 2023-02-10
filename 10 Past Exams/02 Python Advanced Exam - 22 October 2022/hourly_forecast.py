def forecast(*args):
    locations = {"Sunny": [], "Cloudy": [], "Rainy": []}
    result = ""

    for city, weather in args:
        locations[weather].append(city)

    for weather, cities in locations.items():
        for city in sorted(cities):
            result += f"{city} - {weather}\n"

    return result

