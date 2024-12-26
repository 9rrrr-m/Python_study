citys = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

citys_len = [len(i) for i in citys]
max_citys_len = max(citys_len)
min_citys_len = min(citys_len)

long_name_city = []
short_name_city = []
for city in citys:
    if len(city) == max_citys_len:
        long_name_city.append(city)
    if len(city) == min_citys_len:
        short_name_city.append(city)

print("Long Name City :", long_name_city)
print("Short Name City :", short_name_city)
