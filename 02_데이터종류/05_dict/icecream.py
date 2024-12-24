icecream = {'Tankboy': [1200, 5], 'Pollapo': [1200, 7],
            'Ppangppare': [1800, 6], 'Worldcorn': [1500, 3],
            'Melona': [1000, 10], 'Heathunting': [1200, 4]}

print(icecream['Worldcorn'][0])
print(icecream['Worldcorn'][1])

rest_list = []
for name in icecream:
    if icecream[name][1] == 7:
        rest_list.append(name)

print(rest_list)

price_list = []
for name in icecream:
    if icecream[name][0] == 1200:
        price_list.append(name)

print(price_list)
