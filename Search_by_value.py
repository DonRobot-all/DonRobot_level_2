def search_by_value():
    dictionary = {}
    for i in range(int(input())):
        city, country = input().split()
        dictionary[city] = country
    cities = []
    find = input()
    for city, country in dictionary.items():
        if country == find:
            cities.append(city)
    return ' '.join(cities)



print(search_by_value())
