fruit_count = 0
not_fruit_count = 0

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}

key_to_find = 'sandwiches'

sorted_basket = dict(sorted(basket_items.items(), key = lambda item: item[1], reverse = True))
print(sorted_basket)

#Working with dictionaries
#Today do we have any questions reguarding dictionaries?

print(sorted_basket.items())
print(sorted_basket.keys())